# Classified hotels and campsites in France (Atout France) as a CSV

Atout France lists 21,382 classified tourist establishments: 13,267 hotels, 5,688 campsites, 1,602 holiday residences, 535 holiday villages and more (list of 26 November 2026). `classified_hotels.py` runs the [France Classified Accommodation](https://apify.com/euroscrape/france-classified-accommodation?fpr=53ztcw) Actor and writes the establishments of your départements to a CSV: name, type, stars, classification date, address, city, website, capacity, rooms or pitches.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python classified_hotels.py --departments 06 83 --types hotel --stars 4 5
python classified_hotels.py --departments 29 56 --types camping --min-capacity 300
python classified_hotels.py --departments 75 --types hotel --monitor paris-hotels
```

Options: `--departments`, `--postcodes`, `--city` (part of the city name), `--types` (`hotel`, `camping`, `tourist-residence`, `holiday-village`, `collective-hostel`, `leisure-park`), `--stars` (1 to 5), `--min-capacity`, `--since` (classified on or after), `--max`, `--monitor`, `--out`.

With `--monitor`, each run returns only the establishments not delivered before: schedule it once a week to follow new classifications. Useful for hotel and campsite suppliers, booking and software companies and tourist offices. To compare the prices of the hotels you found, official site against booking sites, see [Google Hotels Prices](https://apify.com/euroscrape/google-hotels-prices?fpr=53ztcw).

Notes:

- Runs are billed to your own Apify account: $0.003 per establishment plus $0.003 per run, and the first 10 establishments of every run are free.
- Classification is voluntary and lasts five years: an unclassified hotel is not in the list. Furnished holiday lets and bed-and-breakfasts are not included. No phone or e-mail, only the website when declared.

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
