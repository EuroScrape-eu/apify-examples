# French public tenders digest (BOAMP) as a CSV

French public buyers publish their calls for tender in the BOAMP, the official bulletin of public procurement. `tender_digest.py` runs the [BOAMP Scraper](https://apify.com/euroscrape/boamp-scraper?fpr=53ztcw) Actor and writes the open tenders matching your keywords to a CSV, sorted by bid deadline: buyer, city, value when published, CPV category, link to the tender documents.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python tender_digest.py --keywords logiciel "site web" --departments 75 92 --min-value 40000
```

Options: `--keywords` (any of the words, in the tender text), `--departments` (`75`, `69`, `2A`, empty = all France), `--cpv` (CPV prefixes such as `72` for IT services), `--min-value` (euros), `--days` (first run only), `--out`.

The script uses a monitor name, so each run returns only tenders it has not delivered before: schedule it once a day (cron, GitHub Actions or an Apify schedule) and you get a short CSV of what is new. The first run returns everything published in the last `--days`.

Notes:

- Runs are billed to your own Apify account: $0.003 per tender plus $0.003 per run, and the first 10 tenders of every run are free.
- Public buyers only: no company awards, no individuals. Personal-looking e-mail addresses are removed; service addresses are kept when the buyer publishes them.
- For tenders across Europe (TED and national portals), see [eu-tenders-slack-alerts](../eu-tenders-slack-alerts/).

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
