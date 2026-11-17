# EuroScrape Apify examples

Small, ready-to-run Python scripts built on [EuroScrape Actors](https://apify.com/euroscrape?fpr=53ztcw) on Apify. Each one runs an Actor, turns its output into something useful and writes a CSV.

| Example | Actor | What it does |
|---|---|---|
| [flight-fare-calendar](flight-fare-calendar/fare_calendar.py) | [Google Flights Scraper](https://apify.com/euroscrape/google-flights-prices?fpr=53ztcw) | Cheapest day to fly on one or more routes, as a calendar |
| [hotel-rate-parity-monitor](hotel-rate-parity-monitor/parity.py) | [Google Hotels Scraper](https://apify.com/euroscrape/google-hotels-prices?fpr=53ztcw) | Is the hotel's own website the cheapest place to book it? |
| [eu-tenders-slack-alerts](eu-tenders-slack-alerts/tenders.py) | [EU Public Tenders Scraper](https://apify.com/euroscrape/eu-public-tenders?fpr=53ztcw) | New public tenders matching your keywords, posted to Slack |
| [shop-complaint-rate](shop-complaint-rate/complaints.py) | [Trusted Shops Scraper](https://apify.com/euroscrape/trusted-shops-scraper?fpr=53ztcw) | Online shops of a niche ranked by their share of unhappy customers |

## Run one

```bash
pip install apify-client requests
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python flight-fare-calendar/fare_calendar.py LIS-AMS MAD-ROM --days 30 --nonstop
```

Usage for each script is in its docstring. Runs are billed to your own Apify account.

More: [euroscrape.com](https://euroscrape.com/) · [all Actors](https://apify.com/euroscrape?fpr=53ztcw) · [MCP server for AI agents](https://github.com/EuroScrape-eu/euroscrape-mcp)

## License

MIT

## Comparison guides

Honest comparisons of the tools for a few common jobs, with prices and public success rates read on the Apify Store (EuroScrape included, and said so when it is not the best fit):

- [Best Vinted Scraper 2026: 5 Options Compared](guides/best-vinted-scraper.md)
- [Best Kleinanzeigen Scraper 2026: 5 Options Compared](guides/best-kleinanzeigen-scraper.md)
- [Best Tool to Find Local Businesses Without a Website (2026)](guides/best-tool-businesses-without-website.md)
- [Best French Company Data API 2026 (SIRENE, NAF Code)](guides/best-french-company-data-api.md)
- [Alternative à l'API Pappers : liste d'entreprises par code NAF](guides/alternative-api-pappers.md)

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
