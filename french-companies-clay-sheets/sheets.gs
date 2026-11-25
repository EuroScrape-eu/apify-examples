// Enrich SIREN numbers in column A (from row 2) with the Apify Actor euroscrape/france-companies.
// Script property APIFY_TOKEN = your Apify API token. First 50 companies free per Apify account, then $0.004 each.
function enrichSirens() {
  const sheet = SpreadsheetApp.getActiveSheet();
  const last = sheet.getLastRow();
  if (last < 2) return;
  const sirens = sheet.getRange(2, 1, last - 1, 1).getValues().map(r => String(r[0]).trim()).filter(Boolean);
  const token = PropertiesService.getScriptProperties().getProperty('APIFY_TOKEN');
  const url = 'https://api.apify.com/v2/acts/euroscrape~france-companies/run-sync-get-dataset-items?timeout=280';
  const res = UrlFetchApp.fetch(url, {
    method: 'post', contentType: 'application/json', headers: { Authorization: 'Bearer ' + token },
    payload: JSON.stringify({ sirens: sirens, maxItems: sirens.length }), muteHttpExceptions: true,
  });
  if (res.getResponseCode() >= 300) throw new Error(res.getContentText().slice(0, 300));
  const bySiren = {};
  JSON.parse(res.getContentText()).forEach(c => { bySiren[c.siren] = c; });
  const header = ['legalName', 'status', 'nafCode', 'employees', 'revenue', 'director', 'vatNumber'];
  sheet.getRange(1, 2, 1, header.length).setValues([header]);
  const rows = sheet.getRange(2, 1, last - 1, 1).getValues().map(r => {
    const c = bySiren[String(r[0]).replace(/\D/g, '').slice(0, 9)] || {};
    const d = (c.directors || [])[0] || {};
    return [c.legalName || '', c.status || '', c.nafCode || '', (c.employees || {}).label || '',
            (c.latestFinances || {}).revenue || '', [d.firstNames, d.lastName].filter(Boolean).join(' ') || d.name || '', c.vatNumber || ''];
  });
  sheet.getRange(2, 2, rows.length, header.length).setValues(rows);
}
