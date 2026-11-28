"""French food hygiene inspection results (Alim'confiance) for your area, as a CSV: restaurants, bakeries, butchers, shops.

Runs the "France Food Hygiene Inspections" Actor on Apify. With a monitor name, each run returns only the inspections it
has not delivered before: schedule it weekly (cron, GitHub Actions or an Apify schedule) and get the new "to be improved"
results in your départements every Monday. Useful for hygiene and pest-control suppliers, HACCP trainers, kitchen
equipment sellers, franchisors watching their network, insurers and local journalists.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python hygiene_leads.py --locations 69 --levels "To be improved" "Urgent corrective action"
    python hygiene_leads.py --locations 75008 Annecy --activities Restaurants --days 30
    python hygiene_leads.py --locations 33 --levels "To be improved" --monitor gironde-weekly

Runs are billed to your own Apify account (first 10 inspections of every run are free).
"""
import argparse
import csv
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--locations", nargs="*", default=[], help="department codes (69, 2A, 971), post codes (69003) or town names (Annecy)")
parser.add_argument("--activities", nargs="*", default=[], help="source labels: Restaurants, Boulangerie-Pâtisserie, Boucherie-Charcuterie, Restauration collective...")
parser.add_argument("--levels", nargs="*", default=[], help='"Very satisfactory", "Satisfactory", "To be improved", "Urgent corrective action"')
parser.add_argument("--days", type=int, default=90, help="only inspections dated within this many days (the source keeps about 12 months)")
parser.add_argument("--max", type=int, default=200, help="maximum inspections per run")
parser.add_argument("--monitor", default="", help="monitor name: later runs return only inspections not delivered before")
parser.add_argument("--out", default="hygiene_inspections.csv")
args = parser.parse_args()

run_input = {
    "locations": args.locations,
    "activities": args.activities,
    "levels": args.levels,
    "inspectedSinceDays": args.days,
    "maxItems": args.max,
}
if args.monitor:
    run_input["monitorName"] = args.monitor

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/france-food-hygiene").call(run_input=run_input)
rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())

fields = ["inspectionDate", "rating", "establishmentName", "activity", "address", "postcode", "city", "department",
          "siret", "context", "latitude", "longitude", "sourceUrl"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in rows:
        w.writerow(r)

by_rating = {}
for r in rows:
    by_rating[r.get("rating")] = by_rating.get(r.get("rating"), 0) + 1
print(f"{len(rows)} inspections written to {args.out}")
for k, v in sorted(by_rating.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
