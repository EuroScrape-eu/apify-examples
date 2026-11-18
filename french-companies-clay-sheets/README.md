# Enrich French companies from Clay or Google Sheets

Paste SIREN numbers (or SIRET, or Pappers / Societe.com links) and get back, for each company, its legal name, status, NAF code, headcount range, latest revenue, directors and VAT number. The data comes from the official French register (SIRENE / RNE) through the Apify Actor [French Companies](https://apify.com/euroscrape/france-companies?fpr=53ztcw).

**Cost:** your first 100 companies are free (once per Apify account), then $0.004 per company. Website, emails and phones are optional (`"findContacts": true`, $0.025 per company where a website is found).

You need an Apify account and its API token (Apify Console → Settings → API & Integrations). Keep the token secret: put it in Clay's secret field or in the Apps Script properties, never in a shared sheet.

## Clay: one HTTP API column

1. Add an **HTTP API** enrichment column.
2. Method `POST`, URL:
   `https://api.apify.com/v2/acts/euroscrape~france-companies/run-sync-get-dataset-items?timeout=120`
3. Header `Authorization: Bearer <your Apify token>` and `Content-Type: application/json`.
4. Body (map `/SIREN` to your column):
   ```json
   { "sirens": ["/SIREN"], "maxItems": 1 }
   ```
5. The response is a list with one company. Useful paths: `[0].legalName`, `[0].status`, `[0].nafCode`, `[0].employees.label`, `[0].latestFinances.revenue`, `[0].directors[0].lastName`, `[0].vatNumber`.

One run per row is the simplest setup. For more than a few hundred rows, send the SIRENs in batches of up to 1,000 from a script (below) instead: one run, one start fee.

## Google Sheets: Apps Script

Open Extensions → Apps Script, paste `sheets.gs`, then in Project Settings → Script properties add `APIFY_TOKEN`. SIRENs go in column A (from row 2); run `enrichSirens`.

## Notes

- `status` is `active` or `closed`. A company in liquidation can still be `active` in SIRENE: add `"legalProceedings": true` to get BODACC insolvency notices.
- Directors are those published in the register; individuals who opted out of public disclosure are not returned.
- Runs with no matching SIREN cost only the start fee ($0.003).
