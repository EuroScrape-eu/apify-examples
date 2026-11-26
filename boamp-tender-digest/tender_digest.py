"""French public tenders digest: open BOAMP tenders matching your keywords, sorted by deadline, as a CSV.

Runs the "BOAMP Scraper" Actor on Apify with a monitor name, so each run only returns tenders it has not
delivered before. Schedule it once a day (cron, GitHub Actions or an Apify schedule) and read the CSV.
The first run saves the tenders of the last --days as the baseline and returns them all.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python tender_digest.py --keywords logiciel "site web" --departments 75 92 --min-value 40000

Runs are billed to your own Apify account (first 10 tenders of every run are free).
"""
import argparse
import csv
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--keywords", nargs="*", default=[], help="words searched in the tender text (any of them)")
parser.add_argument("--departments", nargs="*", default=[], help="French department codes, e.g. 75 69 2A; empty = all France")
parser.add_argument("--cpv", nargs="*", default=[], help="CPV prefixes, e.g. 72 (IT services), 45 (works)")
parser.add_argument("--min-value", type=int, default=0, help="only tenders with a published value of at least this many euros")
parser.add_argument("--days", type=int, default=7, help="first run: how far back to look")
parser.add_argument("--monitor", default="my-boamp-digest", help="monitor name: keeps track of tenders already delivered")
parser.add_argument("--out", default="tenders.csv")
args = parser.parse_args()

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/boamp-scraper").call(run_input={
    "keywords": args.keywords,
    "departments": args.departments,
    "cpvCodes": args.cpv,
    "minValueEur": args.min_value,
    "onlyOpen": True,
    "daysBack": args.days,
    "maxItems": 500,
    "monitorName": args.monitor,
})
tenders = list(client.dataset(run["defaultDatasetId"]).iterate_items())
tenders.sort(key=lambda t: t.get("deadline") or "9999")

fields = ["deadline", "title", "buyerName", "buyerCity", "department", "contractType", "mainCpvLabel",
          "estimatedValueEur", "buyerEmail", "documentsUrl", "sourceUrl"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for t in tenders:
        w.writerow(t)

print(f"{len(tenders)} new open tender(s) written to {args.out}")
for t in tenders[:10]:
    value = f"{t['estimatedValueEur']:,.0f} EUR" if t.get("estimatedValueEur") else "value not published"
    print(f"  {(t.get('deadline') or 'no deadline')[:10]}  {t.get('buyerName')}  {t['title'][:80]}  ({value})")
