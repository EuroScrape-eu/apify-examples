"""Certified organic suppliers in France (Agence Bio directory) by product, activity and département, as a CSV.

Runs the "France Organic Operators" Actor on Apify. Use it to find certified organic producers, processors or
wholesalers for a product in your area, or pass --sirets to check whether your suppliers are still certified.
With a monitor name, each run returns only operators that are new or updated since the last run.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python organic_suppliers.py --departments 69 01 --activities production --products miel
    python organic_suppliers.py --sirets 88176038300029

Runs are billed to your own Apify account (first 10 operators of every run are free).
"""
import argparse
import csv
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--departments", nargs="*", default=[], help="department codes (69, 2A, 971...)")
parser.add_argument("--activities", nargs="*", default=[], help="production, processing, distribution, storage, import, export")
parser.add_argument("--products", nargs="*", default=[], help="words of a certified product, in French (miel, vin, lait...)")
parser.add_argument("--name", default="", help="part of the business name")
parser.add_argument("--sirets", nargs="*", default=[], help="exact SIRET numbers to check")
parser.add_argument("--direct-sales", action="store_true", help="only operators selling directly to consumers")
parser.add_argument("--max", type=int, default=500, help="maximum operators per run")
parser.add_argument("--monitor", default="", help="monitor name: returns only new or updated operators")
parser.add_argument("--out", default="organic_operators.csv")
args = parser.parse_args()

run_input = {"departments": args.departments, "activities": args.activities, "products": args.products,
             "sirets": args.sirets, "sellsToConsumers": args.direct_sales, "maxItems": args.max}
if args.name:
    run_input["name"] = args.name
if args.monitor:
    run_input["monitorName"] = args.monitor

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/france-organic-operators").call(run_input=run_input)
rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())

fields = ["organicNumber", "name", "legalName", "siret", "nafCode", "address", "postCode", "city", "department",
          "activities", "products", "certificationStatus", "certifier", "certificateUrl", "engagedOn", "updatedOn"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in rows:
        w.writerow({k: "; ".join(v) if isinstance(v, list) else v for k, v in r.items()})

print(f"{len(rows)} operator(s) written to {args.out}")
for r in rows[:10]:
    print(f"  {r.get('postCode') or '':<6} {(r.get('city') or '')[:18]:<18} {(r.get('name') or '')[:40]:<40} {r.get('certificationStatus') or ''} ({r.get('certifier') or ''})")
