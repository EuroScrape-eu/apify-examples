# French health and social establishments (FINESS) as a CSV

FINESS is the national register of French health, medico-social and social establishments: nursing homes (EHPAD), hospitals, clinics, medical laboratories, home-care services. `health_establishments.py` runs the [FINESS Scraper](https://apify.com/euroscrape/finess-scraper?fpr=53ztcw) Actor and writes one row per establishment: name, category, address, SIRET, switchboard phone and opening date.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python health_establishments.py --categories EHPAD --departments 69 38 --new-since 2025-01-01
```

Options: `--categories` (words such as `EHPAD`, `hospital`, `clinic`, `laboratory`, `SSIAD`, or numeric FINESS category codes), `--departments` (`75`, `69`, `2A`, `971`, empty = all France), `--new-since` (only establishments opened on or after that date), `--max`, `--out`.

Typical uses: a supplier, recruiter or software vendor building a regional list of care homes, or watching new openings.

Notes:

- Runs are billed to your own Apify account: $0.003 per establishment plus $0.003 per run, and the first 10 establishments of every run are free.
- Public data only (Licence Ouverte, Ministry of Health): establishments and their switchboard phone, no individuals, no pharmacies.
- Not every record has a SIRET or a phone number: empty cells are normal.

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
