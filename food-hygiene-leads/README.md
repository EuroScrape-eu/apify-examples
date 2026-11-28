# French food hygiene inspections (Alim'confiance) as a CSV, with weekly alerts

Since 2017 the French agriculture ministry publishes the result of every official hygiene inspection of a place that serves or sells food, on four levels: very satisfactory, satisfactory, to be improved, urgent corrective action. Over the last twelve months that is 70,901 inspections (count of 28 November 2026), of which 4,195 "to be improved" and 319 "urgent corrective action". This script pulls the inspections of your départements, towns or post codes into a CSV, and with a monitor name returns only the new ones each week.

Who uses it: hygiene and pest-control suppliers and HACCP trainers (an establishment rated "to be improved" has a formal notice and a re-inspection coming), kitchen equipment sellers, franchisors watching their network, insurers, local journalists.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python hygiene_leads.py --locations 69 --levels "To be improved" "Urgent corrective action"
python hygiene_leads.py --locations 75008 Annecy --activities Restaurants --days 30
python hygiene_leads.py --locations 33 --levels "To be improved" --monitor gironde-weekly
```

Options: `--locations` (department codes such as `69`, `2A`, `971`, post codes, town names), `--activities` (source labels: `Restaurants`, `Boulangerie-Pâtisserie`, `Boucherie-Charcuterie`, `Restauration collective`, `Alimentation générale`, `Traiteur`…), `--levels`, `--days` (default 90), `--max`, `--monitor`, `--out`.

With `--monitor`, each run returns only the inspections it has not delivered before: schedule the same command every Monday and the CSV holds the week's new results. The Actor can also post them to Telegram, Slack, Discord or a webhook (see its input).

Columns: inspection date, rating (English and French in the Actor output), establishment name, activity, address, post code, city, département, SIRET, inspection context, coordinates, source link.

Notes:

- Runs are billed to your own Apify account: $0.003 per inspection plus $0.003 per run, and the first 10 inspections of every run are free.
- The source keeps a rolling twelve months; an establishment never inspected over the period does not appear, and a later inspection replaces an earlier one. The operator's legal name is never returned, only the establishment's trade name, address and SIRET; a trade name that is a person's name is withheld.
- The same data, one town at a time and free, in the browser: [restaurant hygiene inspections in a French city](https://euroscrape.com/tools/restaurant-hygiene-france).

Actor: [France Food Hygiene Inspections](https://apify.com/euroscrape/france-food-hygiene?fpr=53ztcw)

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
