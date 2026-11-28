# French schools, collèges and lycées as a CSV, from the official directory

The French education ministry publishes a directory of every school: 68,548 open establishments on 28 November 2026, of which 48,328 primary schools, 9,178 collèges and 5,647 lycées (53,752 public, 12,828 private under contract). This script pulls the schools of your départements, towns, post codes or académies into a CSV with address, phone, e-mail, website, SIRET and features (canteen, boarding, ULIS, apprenticeship, international or European section, priority education). With a monitor name, each run returns only the schools that are new or changed since the previous run.

Who uses it: edtech and textbook publishers, school catering and equipment suppliers, tutoring companies, local authorities, researchers.

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python schools_list.py --locations 35 --types Lycée --status public
python schools_list.py --locations Rennes 44 --types Collège Lycée --features boarding
python schools_list.py --academies Lyon --types Lycée --monitor lycees-lyon
```

Options: `--locations` (department codes such as `69`, `2A`, `971`, post codes, town names), `--academies`, `--types` (`Ecole`, `Collège`, `Lycée`, `EREA`; default: the first three), `--status` (`all`, `public`, `private`), `--features` (every listed feature must be present), `--max`, `--monitor`, `--out`.

Notes:

- Runs are billed to your own Apify account: $0.003 per school plus $0.003 per run, and the first 10 schools of every run are free.
- The directory is declarative and updated by the académies: a phone number or an e-mail can be missing or out of date, and it gives no pupil numbers. It lists establishments, never people: the e-mail is the school's institutional address.
- The same directory, one town at a time and free, in the browser: [schools, collèges and lycées in a French city](https://euroscrape.com/tools/french-schools-list).

Actor: [France Schools Directory](https://apify.com/euroscrape/france-schools-directory?fpr=53ztcw)

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
