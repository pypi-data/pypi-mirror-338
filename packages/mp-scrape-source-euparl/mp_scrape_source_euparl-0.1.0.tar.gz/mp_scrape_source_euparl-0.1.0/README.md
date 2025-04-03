<!--
SPDX-FileCopyrightText: 2025 Sofía Aritz <sofiaritz@fsfe.org>

SPDX-License-Identifier: AGPL-3.0-only
-->

# MP Scrape EUParl

Part of the [MP Scrape](https://git.fsfe.org/mp-scrape/mp-scrape) project.

Data Source for the European Parliament.

## Where to get it

You can get it through the [Python Package Index (PyPI)](https://pypi.org/project/mp_scrape_core/):

```sh
$ pip3 install mp_scrape_source_euparl
```

## Arguments

- (Optional) `display_browser` When enabled, a browser window is opened displaying the actions being performed.
- (Optional) `mep_url_template` URL template to obtain data from each MEP, `{ID}` will be replaced with the MEP ID.
- (Optional) `full_list_url` URL from where the full list of MEPs is extracted.
- (Optional) `retrieve_emails` When enabled, e-mails will be retrieved. This takes a long time.
- (Optional) `retrieve_committees` When enabled, membership to committees will be retrieves. This takes a long time.
- (Optional) `timeout` Only valid when `retrieve_emails` or `retrieve_committees` are true, time to wait between pages.