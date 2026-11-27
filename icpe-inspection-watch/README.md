# French classified industrial sites (ICPE) and their inspection reports as a CSV

France lists 139,049 installations classified for environmental protection (ICPE) in Géorisques: factories, Seveso sites, quarries, wind farms, large livestock farms. `icpe_watch.py` runs the [France ICPE Installations](https://apify.com/euroscrape/france-icpe-installations?fpr=53ztcw) Actor and writes the sites of your départements to a CSV: company name, SIRET, address, regime, Seveso status, IED, activity status, inspection service, number of inspections and the date and link of the latest published inspection report.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python icpe_watch.py --departments 76 13 --seveso high
python icpe_watch.py --departments 69 --types industry --with-report
python icpe_watch.py --departments 59 62 --with-report --monitor nord-reports --new-inspections
```

Options: `--departments`, `--insee` (5-digit town codes), `--regimes` (`Autorisation`, `Enregistrement`, `Déclaration`…), `--seveso` (`high`, `low`, `none`), `--types` (`wind`, `quarry`, `cattle`, `pigs`, `poultry`, `industry`), `--names` (words in the company name), `--with-report`, `--monitor`, `--new-inspections`, `--max`, `--out`.

With `--monitor`, each run returns only the sites it has not delivered before; add `--new-inspections` and a site comes back when a newer inspection report is published. Schedule it once a week (cron, GitHub Actions or an Apify schedule). Useful for environmental consultants, insurers, industrial suppliers, real estate due diligence and local journalists.

Notes:

- Runs are billed to your own Apify account: $0.003 per installation plus $0.003 per run, and the first 10 installations of every run are free.
- Texts are in French, as published by Géorisques. Not every site has a published inspection report.

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
