"""French schools, collèges and lycées from the official education directory, as a CSV, with monthly change alerts.

Runs the "France Schools Directory" Actor on Apify. Filter by département, town, post code or académie, by type
(Ecole, Collège, Lycée, EREA), by status (public, private) and by features (boarding, canteen, apprenticeship, sections…).
With a monitor name, each run returns only the schools that are new or changed since the previous run: schedule it monthly.
Useful for edtech and textbook publishers, school catering and equipment suppliers, tutoring companies, local authorities.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python schools_list.py --locations 35 --types Lycée --status public
    python schools_list.py --locations Rennes 44 --types Collège Lycée --features boarding
    python schools_list.py --academies Lyon --types Lycée --monitor lycees-lyon

Runs are billed to your own Apify account (first 10 schools of every run are free).
"""
import argparse
import csv
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--locations", nargs="*", default=[], help="department codes (69, 2A, 971), post codes (69003) or town names (Rennes)")
parser.add_argument("--academies", nargs="*", default=[], help="académies (Lyon, Rennes, Versailles...)")
parser.add_argument("--types", nargs="*", default=["Ecole", "Collège", "Lycée"], help="Ecole, Collège, Lycée, EREA")
parser.add_argument("--status", default="all", help="all, public or private")
parser.add_argument("--features", nargs="*", default=[], help="features every school must have, as listed in the Actor input (boarding, canteen, apprenticeship...)")
parser.add_argument("--max", type=int, default=500, help="maximum schools per run")
parser.add_argument("--monitor", default="", help="monitor name: later runs return only new or changed schools")
parser.add_argument("--out", default="schools.csv")
args = parser.parse_args()

run_input = {
    "locations": args.locations,
    "academies": args.academies,
    "types": args.types,
    "status": args.status,
    "features": args.features,
    "maxItems": args.max,
}
if args.monitor:
    run_input["monitorName"] = args.monitor

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/france-schools-directory").call(run_input=run_input)
rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())

fields = ["uai", "name", "type", "nature", "status", "contractType", "address", "postcode", "city", "department", "academy",
          "phone", "email", "website", "siret", "priorityEducation", "features", "latitude", "longitude", "onisepUrl", "change"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in rows:
        feats = r.get("features")
        if isinstance(feats, dict):
            r = dict(r, features=", ".join(k for k, v in feats.items() if v))
        elif isinstance(feats, list):
            r = dict(r, features=", ".join(feats))
        w.writerow(r)

by_type = {}
for r in rows:
    by_type[r.get("type")] = by_type.get(r.get("type"), 0) + 1
print(f"{len(rows)} schools written to {args.out}")
for k, v in sorted(by_type.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
