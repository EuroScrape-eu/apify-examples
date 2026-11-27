"""French classified industrial sites (ICPE, Géorisques) in your départements, with their latest inspection report, as a CSV.

Runs the "France ICPE Installations" Actor on Apify. With a monitor name and --new-inspections, each run returns
the sites it has not delivered before, plus the sites that got a newer published inspection report: schedule it once a
week (cron, GitHub Actions or an Apify schedule). Useful for environmental consultants, insurers, industrial suppliers,
real estate due diligence and local journalists.

    pip install apify-client
    export APIFY_TOKEN=your_token
    python icpe_watch.py --departments 76 13 --seveso high
    python icpe_watch.py --departments 69 --types industry --with-report --new-inspections

Runs are billed to your own Apify account (first 10 installations of every run are free).
"""
import argparse
import csv
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--departments", nargs="*", default=[], help="department codes (69, 35, 2A, 971...)")
parser.add_argument("--insee", nargs="*", default=[], help="5-digit town codes (e.g. 69123)")
parser.add_argument("--regimes", nargs="*", default=[], help="Autorisation, Enregistrement, Déclaration...")
parser.add_argument("--seveso", nargs="*", default=[], help="high, low, none")
parser.add_argument("--types", nargs="*", default=[], help="wind, quarry, cattle, pigs, poultry, industry")
parser.add_argument("--names", nargs="*", default=[], help="words in the company name")
parser.add_argument("--with-report", action="store_true", help="only sites with a published inspection report")
parser.add_argument("--new-inspections", action="store_true", help="return a site again when a newer report is published")
parser.add_argument("--max", type=int, default=500, help="maximum installations per run")
parser.add_argument("--monitor", default="", help="monitor name: keeps track of installations already delivered")
parser.add_argument("--out", default="icpe_sites.csv")
args = parser.parse_args()

run_input = {
    "departments": args.departments,
    "inseeCodes": args.insee,
    "regimes": args.regimes,
    "sevesoStatus": args.seveso,
    "installationTypes": args.types,
    "nameKeywords": args.names,
    "inspectionReport": "with" if args.with_report else "any",
    "maxItems": args.max,
}
if args.monitor:
    run_input["monitorName"] = args.monitor
    run_input["newInspectionsAsNewRows"] = args.new_inspections

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/france-icpe-installations").call(run_input=run_input)
sites = list(client.dataset(run["defaultDatasetId"]).iterate_items())

fields = ["aiotCode", "companyName", "siret", "address", "postCode", "city", "regime", "sevesoStatus", "ied",
          "activityStatus", "inspectionService", "inspectionCount", "lastReportDate", "lastReportUrl", "latitude", "longitude"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for s in sites:
        w.writerow(s)

print(f"{len(sites)} installation(s) written to {args.out}")
for s in sites[:10]:
    print(f"  {s.get('postCode') or '':<6} {(s.get('city') or '')[:18]:<18} {(s.get('companyName') or '')[:45]:<45} {s.get('sevesoStatus') or ''}  last report: {s.get('lastReportDate') or '-'}")
