"""Every hotel, campsite and holiday residence classified by Atout France in your départements, as a CSV.

Runs the "France Classified Accommodation" Actor on Apify. With a monitor name, each run returns only the
establishments classified since the last run: schedule it once a week to follow new and renewed classifications.
Useful for hotel and campsite suppliers, booking and software companies, tourist offices, and as the list of
hotels to feed a price monitor (official site against booking sites).

    pip install apify-client
    export APIFY_TOKEN=your_token
    python classified_hotels.py --departments 06 83 --types hotel --stars 4 5
    python classified_hotels.py --departments 29 56 --types camping --min-capacity 300

Runs are billed to your own Apify account (first 10 establishments of every run are free).
"""
import argparse
import csv
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--departments", nargs="*", default=[], help="department codes (75, 06, 2A, 971...)")
parser.add_argument("--postcodes", nargs="*", default=[], help="exact 5-digit post codes")
parser.add_argument("--city", default="", help="part of the city name")
parser.add_argument("--types", nargs="*", default=[], help="hotel, camping, tourist-residence, holiday-village, collective-hostel, leisure-park")
parser.add_argument("--stars", nargs="*", type=int, default=[], help="1 to 5")
parser.add_argument("--min-capacity", type=int, default=0, help="minimum guest capacity")
parser.add_argument("--since", default="", help="only establishments classified on or after this date (YYYY-MM-DD)")
parser.add_argument("--max", type=int, default=1000, help="maximum establishments per run")
parser.add_argument("--monitor", default="", help="monitor name: returns only establishments not delivered before")
parser.add_argument("--out", default="classified_accommodation.csv")
args = parser.parse_args()

run_input = {"departments": args.departments, "postCodes": args.postcodes, "types": args.types, "stars": args.stars, "maxItems": args.max}
if args.city:
    run_input["city"] = args.city
if args.min_capacity:
    run_input["minCapacity"] = args.min_capacity
if args.since:
    run_input["classifiedSince"] = args.since
if args.monitor:
    run_input["monitorName"] = args.monitor

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/france-classified-accommodation").call(run_input=run_input)
rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())

fields = ["name", "type", "rating", "stars", "classifiedOn", "address", "postCode", "city", "department",
          "website", "capacity", "rooms", "pitches", "residenceUnits", "holidayVillageHousing"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in rows:
        w.writerow(r)

print(f"{len(rows)} establishment(s) written to {args.out}")
for r in rows[:10]:
    print(f"  {r.get('stars') or '-'}*  {(r.get('city') or '')[:20]:<20} {(r.get('name') or '')[:45]:<45} {r.get('capacity') or ''} guests")
