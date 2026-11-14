# EuroScrape Apify examples

Small, ready-to-run Python scripts built on [EuroScrape Actors](https://apify.com/euroscrape) on Apify. Each one runs an Actor, turns its output into something useful and writes a CSV.

| Example | Actor | What it does |
|---|---|---|
| [flight-fare-calendar](flight-fare-calendar/fare_calendar.py) | [Google Flights Scraper](https://apify.com/euroscrape/google-flights-prices) | Cheapest day to fly on one or more routes, as a calendar |
| [hotel-rate-parity-monitor](hotel-rate-parity-monitor/parity.py) | [Google Hotels Scraper](https://apify.com/euroscrape/google-hotels-prices) | Is the hotel's own website the cheapest place to book it? |
| [eu-tenders-slack-alerts](eu-tenders-slack-alerts/tenders.py) | [EU Public Tenders Scraper](https://apify.com/euroscrape/eu-public-tenders) | New public tenders matching your keywords, posted to Slack |
| [shop-complaint-rate](shop-complaint-rate/complaints.py) | [Trusted Shops Scraper](https://apify.com/euroscrape/trusted-shops-scraper) | Online shops of a niche ranked by their share of unhappy customers |

## Run one

```bash
pip install apify-client requests
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python flight-fare-calendar/fare_calendar.py LIS-AMS MAD-ROM --days 30 --nonstop
```

Usage for each script is in its docstring. Runs are billed to your own Apify account.

More: [euroscrape.com](https://euroscrape.com/) · [all Actors](https://apify.com/euroscrape) · [MCP server for AI agents](https://github.com/EuroScrape-eu/euroscrape-mcp)

## License

MIT
