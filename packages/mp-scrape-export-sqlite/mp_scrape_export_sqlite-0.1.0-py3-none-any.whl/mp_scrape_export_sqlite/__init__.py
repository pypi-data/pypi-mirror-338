# SPDX-FileCopyrightText: 2025 Sofía Aritz <sofiaritz@fsfe.org>
#
# SPDX-License-Identifier: AGPL-3.0-only

from mp_scrape_core import DataConsumer, ModuleDefinition, ModuleDescription, ModuleArgument, ModuleMaintainer
import pandas as pd

import logging
import sqlite3
import datetime
import math
import os

class SqliteExport(DataConsumer):
    def __init__(self, table_name: str, dest = "result.sqlite3", track_changes = True, overwrite = False, separate_sources = True):
        """
        Export the data in a SQLite database.

        Only integers, strings, and real numbers are supported.

        :param str dest: (Destination file) Where the SQLite database is (or will be) stored.
        :param bool track_changes: (Track changes) When enabled, instead of overwritting the existing tables, new tables will be created. These new tables define the data as was at a certain point in time. References to these tables and when were they created will be stored in a `time_mappings` table.
        :param str table_name: (Table name) Where will the data be stored
        :param bool separate_sources: (Separate sources) When enabled, each data source will have its own table
        :param bool overwrite: (Overwrite database) If the database already exists, overwrite all of the contents
        """
        self.dest = dest
        self.table_name = table_name
        self.track_changes = track_changes
        self.overwrite = overwrite
        self.separate_sources = separate_sources

    @staticmethod
    def metadata() -> ModuleDefinition:
        return ModuleDefinition({
            "name": "SQLite export",
            "identifier": "sqlite",
            "description": ModuleDescription.from_init(SqliteExport.__init__),
            "arguments": ModuleArgument.list_from_init(SqliteExport.__init__),
            "maintainers": [
                ModuleMaintainer({
                    "name": "Free Software Foundation Europe",
                    "email": "mp-scrape@fsfe.org"
                }),
                ModuleMaintainer({
                    "name": "Sofía Aritz",
                    "email": "sofiaritz@fsfe.org"
                }),
            ]
        })
    
    def _col_name_to_sql(self, val: str) -> str:
        return val.replace(" ", "__")
    
    def _new_table_query(self, base_table_name: str, data: pd.DataFrame, source: str = None) -> str:
        gen_table_name = base_table_name if source is None else f"{base_table_name}__{source}"

        query = f"CREATE TABLE IF NOT EXISTS {gen_table_name} ( "
        for col_name in list(data):
            data[col_name] = data[col_name].map(lambda x: None if ((isinstance(x, int) or isinstance(x, float)) and math.isnan(x)) else x)
            if bool(data[col_name].apply(lambda x: isinstance(x, str) or x is None).all()):
                query += f"{self._col_name_to_sql(col_name)} TEXT, "
            elif bool(data[col_name].apply(lambda x: isinstance(x, int) or x is None).all()):
                query += f"{self._col_name_to_sql(col_name)} INTEGER, "
            elif bool(data[col_name].apply(lambda x: isinstance(x, float) or x is None).all()):
                query += f"{self._col_name_to_sql(col_name)} REAL, "
            else:
                raise Exception("Unsupported or inconsistent data type")
        query += "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );"

        return gen_table_name, query

    async def consume(self, logger: logging.Logger, data: pd.DataFrame) -> None:
        os.makedirs(os.path.dirname(self.dest), exist_ok=True)
        con = sqlite3.connect(self.dest, isolation_level=None)
        con.execute("PRAGMA journal_mode=wal")

        cur = con.cursor()
        current_datestring = datetime.datetime.today().strftime("%Y_%m_%d__%H_%M_%S")

        if self.overwrite:
            logger.info("deleting all data from the database")
            cur.execute("PRAGMA writable_schema=1;")
            cur.execute("DELETE FROM sqlite_master WHERE type IN ('table', 'index', 'trigger');")
            cur.execute("PRAGMA writable_schema=0;")
            con.commit()

            logger.debug("claiming disk space from deleted tables")
            cur.execute("VACUUM;")
            cur.execute("PRAGMA INTEGRITY_CHECK;")
            con.commit()

        table_name = f"_{current_datestring}__{self.table_name}" if self.track_changes else self.table_name

        if self.track_changes:
            query = "CREATE TABLE IF NOT EXISTS table_mappings ( table_name TEXT NOT NULL, source TEXT, time_aware_table_name TEXT NOT NULL, creation TIMESTAMP NOT NULL );"
            cur.execute(query)
            con.commit()

        if self.separate_sources:
            for source, df in {key: group.reset_index(drop=True) for key, group in data.groupby("__mp_scrape__source_identifier")}.items():
                df = df.dropna(how='all', axis=1) # Remove empty columns
                gen_table_name, query = self._new_table_query(table_name, df, source)
                cur.execute(query)
                con.commit()

                values = df.values.tolist()
                placeholder = ("?," * len(values[0]))[:-1]
                cur.executemany(f"INSERT INTO {gen_table_name} VALUES ({placeholder}, CURRENT_TIMESTAMP);", values)
                con.commit()

                if self.track_changes:
                    cur.execute("INSERT INTO table_mappings VALUES (?,?,?,CURRENT_TIMESTAMP);", (self.table_name, source, gen_table_name))
                    con.commit()
        else:
            gen_table_name, query = self._new_table_query(table_name, data)
            cur.execute(query)
            con.commit()

            values = data.values.tolist()
            placeholder = ("?," * len(values[0]))[:-1]
            cur.executemany(f"INSERT INTO {table_name} VALUES ({placeholder}, CURRENT_TIMESTAMP);", values)
            con.commit()

            if self.track_changes:
                cur.execute("INSERT INTO table_mappings VALUES (?,NULL,?,CURRENT_TIMESTAMP);", (self.table_name, gen_table_name))
                con.commit()

