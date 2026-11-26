"""French EV charging points (IRVE) as a CSV: fast chargers by department, city, operator or plug.

Runs the "France EV Charging Stations" Actor on Apify and writes one row per charging point: station, operator,
address, GPS position, power in kW, plugs, free or paid, opening hours. Useful for mobility apps, fleet managers,
retail sites choosing a location and anyone mapping the competition.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python fast_chargers.py --departments 69 38 --min-kw 50
    python fast_chargers.py --cities Lyon --operators ionity tesla --plugs ccs

Runs are billed to your own Apify account (first 10 charging points of every run are free).
"""
import argparse
import csv
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--departments", nargs="*", default=[], help="department codes, e.g. 75 13 2A 974; empty = all France")
parser.add_argument("--cities", nargs="*", default=[], help="city names, accents ignored")
parser.add_argument("--operators", nargs="*", default=[], help="words in operator, network or owner names, e.g. ionity tesla")
parser.add_argument("--min-kw", type=float, default=None, help="minimum power in kW (50 = fast charging)")
parser.add_argument("--plugs", nargs="*", default=[], help="type2, ccs, chademo, domestic, other")
parser.add_argument("--free-only", action="store_true")
parser.add_argument("--max", type=int, default=200, help="stop after this many charging points (most powerful first)")
parser.add_argument("--out", default="charging_points.csv")
args = parser.parse_args()

run_input = {
    "departments": args.departments,
    "cities": args.cities,
    "operators": args.operators,
    "plugTypes": args.plugs,
    "freeOnly": args.free_only,
    "maxItems": args.max,
}
if args.min_kw is not None:
    run_input["minPowerKw"] = args.min_kw

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/irve-charging-stations").call(run_input=run_input)
points = list(client.dataset(run["defaultDatasetId"]).iterate_items())

fields = ["stationName", "network", "operator", "address", "postalCode", "city", "departmentCode", "latitude", "longitude",
          "powerKw", "plugs", "free", "access", "openingHours", "pricing"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for p in points:
        w.writerow(p)

print(f"{len(points)} charging point(s) written to {args.out}")
for p in points[:10]:
    print(f"  {p.get('powerKw')} kW  {p.get('stationName')}  {p.get('city')}  ({p.get('operator')})")
