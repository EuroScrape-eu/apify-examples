"""New French associations (Journal officiel, JOAFE) in your départements, as a weekly CSV of leads.

Runs the "French Associations" Actor on Apify with a monitor name, so each run only returns notices it has not
delivered before. Schedule it once a week (cron, GitHub Actions or an Apify schedule): useful for banks, insurers,
accountants, software publishers for associations, sports or culture suppliers and town halls.
The first run returns the notices published since --since (default: the last 30 days).

    pip install apify-client
    export APIFY_TOKEN=your_token
    python new_associations.py --departments 69 38 --domains sport
    python new_associations.py --departments 75 --keywords theatre --types creation modification

Runs are billed to your own Apify account (first 10 notices of every run are free).
"""
import argparse
import csv
import os

from apify_client import ApifyClient

parser = argparse.ArgumentParser()
parser.add_argument("--departments", nargs="*", default=[], help="department codes (75, 69, 2A, 971...); empty = all France")
parser.add_argument("--types", nargs="*", default=["creation"], help="creation, modification, dissolution, suspension")
parser.add_argument("--domains", nargs="*", default=[], help="words of the declared activity domain (sport, culture, santé...)")
parser.add_argument("--keywords", nargs="*", default=[], help="words searched in the name and purpose")
parser.add_argument("--since", default="", help="first run: only notices published on or after this date (YYYY-MM-DD)")
parser.add_argument("--max", type=int, default=500, help="maximum notices per run")
parser.add_argument("--monitor", default="my-new-associations", help="monitor name: keeps track of notices already delivered")
parser.add_argument("--out", default="new_associations.csv")
args = parser.parse_args()

run_input = {
    "noticeTypes": args.types,
    "departments": args.departments,
    "activityDomains": args.domains,
    "keywords": args.keywords,
    "maxItems": args.max,
    "monitorName": args.monitor,
}
if args.since:
    run_input["publishedSince"] = args.since

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("euroscrape/french-associations").call(run_input=run_input)
notices = list(client.dataset(run["defaultDatasetId"]).iterate_items())

fields = ["publicationDate", "noticeType", "rnaNumber", "name", "purpose", "activityDomain",
          "address", "postCode", "city", "department", "website", "latitude", "longitude"]
with open(args.out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for n in notices:
        w.writerow(n)

print(f"{len(notices)} new notice(s) written to {args.out}")
for n in notices[:10]:
    print(f"  {n.get('publicationDate')}  {n.get('city') or '':<20}  {(n.get('name') or '')[:50]}  ({(n.get('activityDomain') or '').split('/')[0][:40]})")
