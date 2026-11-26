# French consumer product recalls (RappelConso) as a daily CSV

RappelConso is the official French register of consumer product recalls, run by the DGCCRF. `recall_watch.py` runs the [RappelConso Scraper](https://apify.com/euroscrape/rappelconso-scraper?fpr=53ztcw) Actor and writes the recalls matching your brands, keywords, categories or barcodes to a CSV: product, brand, reason, risks, recall nature, barcodes, distributors and the link to the official notice.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python recall_watch.py --brands carrefour leclerc --categories food --since 2026-11-01
python recall_watch.py --keywords listeria --since 2026-11-01
python recall_watch.py --gtins 3017620422003
```

Options: `--brands`, `--keywords` (words in the product name, reason or sub-category), `--categories` (`food`, `cars`, `baby`, `home`, `electrical`, `beauty`, `clothing`, `sports`, `other`), `--gtins` (8 to 14 digits), `--since` (first run only), `--monitor`, `--out`.

The script uses a monitor name, so each run returns only recalls it has not delivered before: schedule it once a day (cron, GitHub Actions or an Apify schedule) and you get a short CSV of what is new. Useful for retailers, marketplaces, insurers and quality teams.

Notes:

- Runs are billed to your own Apify account: $0.003 per recall plus $0.003 per run, and the first 10 recalls of every run are free.
- Texts are in French, as published. Recalls of cars and vehicles carry no lots, barcodes or distributors in the source file.
- Public data only; the contact phone numbers of the file are left out.

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
