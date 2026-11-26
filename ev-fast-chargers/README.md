# French EV charging points (IRVE) as a CSV

The French consolidated file of electric-vehicle charging points (IRVE) is published daily on data.gouv.fr. `fast_chargers.py` runs the [France EV Charging Stations](https://apify.com/euroscrape/irve-charging-stations?fpr=53ztcw) Actor and writes one row per charging point: station, network, operator, address, GPS position, power in kW, plugs, free or paid, access and opening hours.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python fast_chargers.py --departments 69 38 --min-kw 50
python fast_chargers.py --cities Lyon --operators ionity tesla --plugs ccs
```

Options: `--departments` (`75`, `13`, `2A`, `974`, empty = all France), `--cities` (accents ignored), `--operators` (words in operator, network or owner names), `--min-kw` (50 = fast charging), `--plugs` (`type2`, `ccs`, `chademo`, `domestic`, `other`), `--free-only`, `--max` (most powerful first), `--out`.

Typical uses: mobility apps, fleet managers, retail sites looking at charging offer around a location, competitor mapping.

Notes:

- Runs are billed to your own Apify account: $0.003 per charging point plus $0.003 per run, and the first 10 charging points of every run are free.
- Data comes from the operators' declarations: some power values are plainly wrong in the source (for example a station declared at 748 kW) and are returned as published, so check the top of a "most powerful first" list before trusting it.
- Public data only; operator contact details of the file are left out.

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
