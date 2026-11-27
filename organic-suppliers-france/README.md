# Certified organic suppliers in France (Agence Bio) as a CSV

The Agence Bio directory lists 138,597 organic operators in France: farms, processors, wholesalers, retailers, importers, each with its certifier and certificate status. `organic_suppliers.py` runs the [France Organic Operators](https://apify.com/euroscrape/france-organic-operators?fpr=53ztcw) Actor and writes the operators matching your départements, activities or products to a CSV: business name, SIRET, NAF code, address, activities, certified products, certification status, certifier and certificate link.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python organic_suppliers.py --departments 69 01 --activities production --products miel
python organic_suppliers.py --departments 33 --activities distribution
python organic_suppliers.py --sirets 88176038300029
```

Options: `--departments`, `--activities` (`production`, `processing`, `distribution`, `storage`, `import`, `export`), `--products` (words of a certified product, in French), `--name`, `--sirets` (check whether given businesses are certified), `--direct-sales`, `--max`, `--monitor`, `--out`.

Useful for buyers sourcing organic suppliers, wholesalers and retailers checking that their suppliers are still certified, and food or farming businesses prospecting organic operators. With `--monitor`, each run returns only operators that are new or updated since the last run.

Notes:

- Runs are billed to your own Apify account: $0.003 per operator plus $0.003 per run, and the first 10 operators of every run are free.
- No phone numbers or manager names are returned. Some operators are sole traders, so a business name can be a person's name: use the data for professional purposes and in line with GDPR.

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
