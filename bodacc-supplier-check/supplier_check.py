"""Check a list of French suppliers against the BODACC insolvency notices.

Reads SIREN (9 digits) or SIRET (14 digits) numbers from a CSV or text file (one per line, or a column named
"siren"), runs the "BODACC Scraper" Actor on Apify for insolvency notices, and writes one CSV row per notice.
Companies with no notice in the period are listed as clear.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python supplier_check.py suppliers.csv --days 365 --out insolvency_notices.csv

Runs are billed to your own Apify account (first 10 notices of every run are free).
"""
import argparse
import csv
import os
import re

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("file", help="CSV or text file with SIREN/SIRET numbers")
parser.add_argument("--days", type=int, default=365, help="look back this many days (1 to 365)")
parser.add_argument("--out", default="insolvency_notices.csv")
args = parser.parse_args()

ids = []
with open(args.file, newline="", encoding="utf-8-sig") as f:
    for line in f:
        for token in re.findall(r"\b\d[\d ]{7,16}\d\b", line):
            digits = token.replace(" ", "")
            if len(digits) in (9, 14) and digits not in ids:
                ids.append(digits)
if not ids:
    raise SystemExit("No SIREN or SIRET number found in the file.")

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/bodacc-scraper").call(run_input={
    "noticeTypes": ["insolvency"],
    "daysBack": args.days,
    "sirens": ids,
    "maxItems": 1000,
})
notices = list(client.dataset(run["defaultDatasetId"]).iterate_items())

hit = {str(n.get("siren")) for n in notices}
siren_of = lambda x: x[:9]
flagged = sorted({siren_of(i) for i in ids if siren_of(i) in hit})
clear = [i for i in ids if siren_of(i) not in hit]

fields = ["siren", "companyName", "publicationDate", "insolvencyEvent", "court", "judgmentDate", "sourceUrl"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for n in sorted(notices, key=lambda n: (str(n.get("siren")), str(n.get("publicationDate")))):
        w.writerow(n)

print(f"{len(ids)} companies checked, {len(flagged)} with an insolvency notice in the last {args.days} days, {len(clear)} clear.")
for s in flagged:
    last = max((n for n in notices if str(n.get("siren")) == s), key=lambda n: str(n.get("publicationDate")))
    print(f"  {s}  {last.get('companyName')}  {last.get('publicationDate')}  {last.get('insolvencyEvent') or last.get('noticeLabel')}")
print(f"Notices written to {args.out}. A notice is a public record, not a verdict: open sourceUrl before acting on it.")
