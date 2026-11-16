# Best French company data API in 2026: SIRENE by NAF code

*Canonical version, kept up to date: [https://euroscrape.com/guides/best-french-company-data-api](https://euroscrape.com/guides/best-french-company-data-api)*

**In short:** if you can code, the best French company data API in 2026 is free: the government's **API Recherche d'entreprises** filters the SIRENE register by NAF code, département and size with no key (up to 7 requests per second). For the whole register, download **INSEE's SIRENE files**. If you want a spreadsheet without coding, the most used Apify tool is **dltik's Pappers / Sirene Scraper** ($0.008 per company, 414 of 414 public runs succeeded in 30 days), and the cheapest is **titoune33's French Company Data API** ($0.001 per record). **EuroScrape's French Companies** ($0.004 per company) adds directors, VAT, BODACC notices and verified contacts ($0.025 per company with contacts). Figures read on 16 November 2026.

## The comparison

| Option | Price | Public runs, last 30 days (success) | Best for |
|---|---|---|---|
| [API Recherche d'entreprises](https://recherche-entreprises.api.gouv.fr/) (DINUM) | free, no key | official service | Developers: search by NAF, area, size |
| [INSEE SIRENE files](https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/) | free | official open data | The whole register, millions of rows |
| [dltik Pappers / Sirene Scraper](https://apify.com/dltik/pappers-sirene-scraper) | $0.008 per company ($0.01 analysed) | 414 (100 %) | Most used no-code export |
| [titoune33 French Company Data API](https://apify.com/titoune33/french-company-data) | $0.001 per record | 56 (100 %) | Cheapest no-code export |
| [EuroScrape French Companies](https://apify.com/euroscrape/france-companies) | $0.004 per company, $0.025 with contacts, $0.003 start | 102 (93.1 %) | Directors, VAT, BODACC, contacts in one row |
| Pappers API | credits (paid plans) | commercial | Financial accounts and legal documents |

## How to choose

- **You code and need a few thousand companies:** API Recherche d'entreprises. Free and official.
- **You need every company:** the SIRENE files, loaded into your own database.
- **You want a CSV now, no code:** dltik (most used) or titoune33 (cheapest).
- **You prospect and need who to call:** EuroScrape, which adds directors, VAT number, legal notices and verified company emails and phones.
- **You need financial statements and legal documents:** Pappers.

## Who should not pick EuroScrape

If you only need names, SIREN and NAF codes, the free government API or a cheaper Apify tool is enough. EuroScrape's success rate over 30 days was 93.1 % (102 runs), lower than the two other Apify tools above.

Try the count first, free: the [French company counter](https://euroscrape.com/tools/french-company-counter) gives the live number of active companies for a NAF code and a département. More: [French company data API guide](https://euroscrape.com/guides/french-company-data-api) and [all NAF codes](https://euroscrape.com/fr/naf/).

*Method: prices and run statistics read from the Apify Store API on 16 November 2026; official API limits from its documentation. EuroScrape publishes one of the tools compared; it is not ranked first.*
