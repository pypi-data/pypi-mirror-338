<!--
SPDX-FileCopyrightText: 2025 Sofía Aritz <sofiaritz@fsfe.org>

SPDX-License-Identifier: AGPL-3.0-only
-->

# MP Scrape Export SQLite

Part of the [MP Scrape](https://git.fsfe.org/mp-scrape/mp-scrape) project.

Data Consumer to export data in SQLite

## Where to get it

You can get it through the [Python Package Index (PyPI)](https://pypi.org/project/mp_scrape_core/):

```sh
$ pip3 install mp_scrape_export_sqlite
```

## Arguments

- `dest` Where the SQLite database is (or will be) stored.
- (Optional) `track_changes` When enabled, instead of overwritting the existing tables, new tables will be created. These new tables define the data as was at a certain point in time. References to these tables and when were they created will be stored in a `time_mappings` table.
- (Optional) `table_name` Where will the data be stored
- (Optional) `separate_sources` When enabled, each data source will have its own table
- (Optional) `overwrite` If the database already exists, overwrite all of the contents