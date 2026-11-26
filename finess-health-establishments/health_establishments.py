"""French health and social establishments (FINESS) as a CSV: nursing homes, clinics, laboratories, by department.

Runs the "FINESS Scraper" Actor on Apify and writes one row per establishment: name, category, address, SIRET,
phone, opening date. Useful for suppliers, recruiters and software vendors that sell to care homes, clinics
and laboratories. With --new-since it lists only recent openings.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python health_establishments.py --categories EHPAD --departments 69 38 --new-since 2025-01-01

Runs are billed to your own Apify account (first 10 establishments of every run are free).
"""
import argparse
import csv
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--categories", nargs="*", default=[], help='words of the FINESS category: EHPAD, hospital, clinic, laboratory, SSIAD, or numeric codes')
parser.add_argument("--departments", nargs="*", default=[], help="French department codes, e.g. 75 69 2A 971; empty = all France")
parser.add_argument("--new-since", default="", help="only establishments opened on or after this date (YYYY-MM-DD)")
parser.add_argument("--max", type=int, default=200, help="stop after this many establishments")
parser.add_argument("--out", default="establishments.csv")
args = parser.parse_args()

run_input = {
    "categories": args.categories,
    "departments": args.departments,
    "maxItems": args.max,
}
if args.new_since:
    run_input["openedSince"] = args.new_since

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/finess-scraper").call(run_input=run_input)
rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())

fields = ["name", "category", "address", "postCode", "city", "department", "siret", "phone", "openingDate"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in rows:
        w.writerow(r)

print(f"{len(rows)} establishment(s) written to {args.out}")
for r in rows[:10]:
    print(f"  {r.get('name')}  {r.get('city')} ({r.get('department')})  {r.get('category')}")
