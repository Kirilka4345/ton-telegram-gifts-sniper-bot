# Fragment Gift Price Observer — Python Prototype

An experimental HTML scraper and local report generator for Fragment gift listings.

**Status: development starter / prototype.** Read the scope before integrating.

## Included

- Attempts to parse gift collection pages and compare the first two observed prices.
- Writes a local JSON report and escaped HTML dashboard.
- Running the script does not trade, sign transactions or publish repositories.

## Scope and limitations

- Live parsing depends on upstream HTML and has not been validated as a reliable data feed.
- No Getgems/Portals API integration, wallet execution, notifications or profitable arbitrage guarantee.
- A missing observation is not a zero market price; inspect fetch warnings.
- config.example.json is illustrative; thresholds are currently in the source.

## Quick start

Python 3.10+; run from the repository directory.

```sh
python ton_gifts_sniper.py
```

## Validation

```sh
python -m unittest discover -s tests -v
```

Offline tests cover report generation and HTML safety. Live marketplace access is not covered.

## Repository map

- `ton_gifts_sniper.py` — implementation.
- `tests/` — current checks and regression tests.
- [CHANGELOG.md](CHANGELOG.md) — changes and verification limits.
- [CONTRIBUTING.md](CONTRIBUTING.md) — issue and change guidelines.

## Downloads and usage terms

[Repository releases](https://github.com/Kirilka4345/ton-telegram-gifts-sniper-bot/releases) contain historical snapshots; use the current source for the documented fixes.
No LICENSE file is present. Earlier MIT badges and commercial-license claims did not establish usable license terms. License terms require clarification before redistribution.

## Questions

For reproducible technical issues, use [GitHub Issues](https://github.com/Kirilka4345/ton-telegram-gifts-sniper-bot/issues). Include the commit, runtime version, expected result and minimal reproduction. Never include tokens, cookies or customer data.
