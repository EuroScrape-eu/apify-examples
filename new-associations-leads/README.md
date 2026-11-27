# New French associations (Journal officiel) as a weekly CSV of leads

About 79,000 associations were created in France between January and November 2026, each one published in the Journal officiel des associations (JOAFE). `new_associations.py` runs the [French Associations](https://apify.com/euroscrape/french-associations?fpr=53ztcw) Actor and writes the notices for your départements, activity domains or keywords to a CSV: RNA number, name, declared purpose, activity domain, seat address, city, website and GPS position.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python new_associations.py --departments 69 38 --domains sport
python new_associations.py --departments 75 --keywords theatre --types creation modification
python new_associations.py --types dissolution --since 2026-11-01
```

Options: `--departments` (75, 69, 2A, 971…; empty = all France), `--types` (`creation`, `modification`, `dissolution`, `suspension`; default `creation`), `--domains` (words of the declared activity domain), `--keywords` (words in the name or purpose), `--since` (first run only; default the last 30 days), `--max`, `--monitor`, `--out`.

The script uses a monitor name, so each run returns only notices it has not delivered before: schedule it once a week (cron, GitHub Actions or an Apify schedule) and you get the new associations of your area. Useful for banks, insurers, accountants, software publishers for associations, sports or culture suppliers and town halls.

Notes:

- Runs are billed to your own Apify account: $0.003 per notice plus $0.003 per run, and the first 10 notices of every run are free.
- Texts are in French, as published. Notices never name the founders; publication follows the declaration by one to three weeks.
- The seat address is sometimes a volunteer's home: use the data for professional prospecting in line with GDPR.

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
