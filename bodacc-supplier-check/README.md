# Check your French suppliers against BODACC insolvency notices

A supplier in liquidation can stay "active" in company registers for months. The BODACC, the official journal of French commercial announcements, publishes the court decisions first.

`supplier_check.py` takes a list of SIREN or SIRET numbers (CSV or text file), runs the [BODACC Scraper](https://apify.com/euroscrape/bodacc-scraper?fpr=53ztcw) Actor and writes one CSV row per insolvency notice. It prints which companies have a notice in the period and which are clear.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python supplier_check.py suppliers.csv --days 365 --out insolvency_notices.csv
```

`suppliers.csv` can be a single column named `siren`, or any file with one number per line (spaces inside a number are fine).

Output columns: `siren`, `companyName`, `publicationDate`, `insolvencyEvent`, `court`, `judgmentDate`, `sourceUrl` (link to the official notice on bodacc.fr).

Notes:

- Runs are billed to your own Apify account: $0.003 per notice plus $0.003 per run, and the first 10 notices of every run are free.
- A notice is a public record, not a verdict. Open `sourceUrl` before acting on it.
- Companies only: notices about sole traders are never returned.
- To watch the same list every day, schedule the Actor in Apify with a `monitorName` and the same `sirens` input: each run then returns only notices not delivered before.

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
