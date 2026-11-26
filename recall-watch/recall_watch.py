"""French consumer product recalls (RappelConso) for your brands, keywords or barcodes, as a CSV.

Runs the "RappelConso Scraper" Actor on Apify with a monitor name, so each run only returns recalls it has not
delivered before. Schedule it once a day (cron, GitHub Actions or an Apify schedule) and read the CSV: useful for
retailers, marketplaces, insurers and quality teams that need to know when a product they sell is recalled.
The first run returns the recalls published since --since.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python recall_watch.py --brands carrefour leclerc --categories food --since 2026-11-01
    python recall_watch.py --gtins 3017620422003

Runs are billed to your own Apify account (first 10 recalls of every run are free).
"""
import argparse
import csv
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--brands", nargs="*", default=[], help="brand names (any of them)")
parser.add_argument("--keywords", nargs="*", default=[], help="words in the product name, reason or sub-category, e.g. listeria")
parser.add_argument("--categories", nargs="*", default=[], help="food, cars, baby, home, electrical, beauty, clothing, sports, other")
parser.add_argument("--gtins", nargs="*", default=[], help="barcodes (8 to 14 digits)")
parser.add_argument("--since", default="", help="first run: only recalls published on or after this date (YYYY-MM-DD)")
parser.add_argument("--monitor", default="my-recall-watch", help="monitor name: keeps track of recalls already delivered")
parser.add_argument("--out", default="recalls.csv")
args = parser.parse_args()

run_input = {
    "brands": args.brands,
    "keywords": args.keywords,
    "categories": args.categories,
    "gtins": args.gtins,
    "maxItems": 500,
    "monitorName": args.monitor,
}
if args.since:
    run_input["publishedSince"] = args.since

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/rappelconso-scraper").call(run_input=run_input)
recalls = list(client.dataset(run["defaultDatasetId"]).iterate_items())

fields = ["publishedAt", "category", "subCategory", "brand", "title", "reason", "risks", "recallNature", "gtins", "distributors", "url"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in recalls:
        w.writerow(r)

print(f"{len(recalls)} new recall(s) written to {args.out}")
for r in recalls[:10]:
    print(f"  {(r.get('publishedAt') or '')[:10]}  {r.get('brand')}  {(r.get('title') or '')[:70]}  ({r.get('reason')})")
