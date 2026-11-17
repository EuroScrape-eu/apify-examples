# Alternative à l'API Pappers pour extraire une liste d'entreprises par code NAF

*Canonical version, kept up to date: [https://euroscrape.com/guides/alternative-api-pappers](https://euroscrape.com/guides/alternative-api-pappers)*

**En bref :** l'alternative gratuite la plus directe à l'API Pappers est l'**API Recherche d'entreprises** de l'État : elle filtre le registre SIRENE par code NAF, département et effectif, sans clé (jusqu'à 7 requêtes par seconde). Pour toutes les entreprises, téléchargez les **fichiers SIRENE de l'INSEE**. Sans coder, l'outil Apify le plus utilisé est le **Pappers / Sirene Scraper de dltik** (0,008 $ par entreprise, 414 runs publics réussis sur 414 en 30 jours) ; le moins cher est le **French Company Data API de titoune33** (0,001 $ par fiche). **French Companies d'EuroScrape** (0,004 $ par entreprise) ajoute dirigeants, TVA, annonces BODACC et coordonnées vérifiées (0,025 $ avec contacts). Chiffres relevés le 16 novembre 2026.

## Le comparatif

| Solution | Prix | Runs publics sur 30 jours (réussite) | Pour qui |
|---|---|---|---|
| [API Recherche d'entreprises](https://recherche-entreprises.api.gouv.fr/) (DINUM) | gratuite, sans clé | service officiel | Développeurs : recherche par NAF, zone, taille |
| [Fichiers SIRENE (INSEE)](https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/) | gratuits | open data officiel | Toute la base, des millions de lignes |
| [dltik Pappers / Sirene Scraper](https://apify.com/dltik/pappers-sirene-scraper?fpr=53ztcw) | 0,008 $ par entreprise | 414 (100 %) | Export sans code le plus utilisé |
| [titoune33 French Company Data API](https://apify.com/titoune33/french-company-data?fpr=53ztcw) | 0,001 $ par fiche | 56 (100 %) | Export sans code le moins cher |
| [EuroScrape French Companies](https://apify.com/euroscrape/france-companies?fpr=53ztcw) | 0,004 $ par entreprise, 0,025 $ avec contacts, 0,003 $ par lancement | 102 (93,1 %) | Prospection : dirigeants, TVA, BODACC, contacts |
| API Pappers | crédits (offres payantes) | commercial | Comptes annuels, actes, documents |

## Comment choisir

- **Vous codez et il vous faut quelques milliers d'entreprises :** API Recherche d'entreprises.
- **Il vous faut toute la base :** les fichiers SIRENE.
- **Vous voulez un CSV tout de suite, sans code :** dltik (le plus utilisé) ou titoune33 (le moins cher).
- **Vous prospectez et cherchez qui appeler :** EuroScrape, qui ajoute dirigeants, numéro de TVA, annonces légales, e-mails et téléphones vérifiés de l'entreprise.
- **Vous avez besoin des comptes et des actes :** gardez Pappers.

## Quand ne pas choisir EuroScrape

Si le nom, le SIREN et le code NAF suffisent, l'API publique gratuite ou un outil moins cher fait l'affaire. Le taux de réussite d'EuroScrape sur 30 jours est de 93,1 % (102 runs), plus bas que celui des deux autres outils Apify du tableau.

Compter d'abord, gratuitement : le [compteur d'entreprises](https://euroscrape.com/fr/outils/compteur-entreprises) donne le nombre d'entreprises actives pour un code NAF et un département. Tous les codes : [codes NAF](https://euroscrape.com/fr/naf/).

*Méthode : prix et statistiques de runs relevés par l'API du Store Apify le 16 novembre 2026 ; limites de l'API publique d'après sa documentation. EuroScrape publie l'un des outils comparés ; il n'est pas classé premier.*

<sub>Links to apify.com carry EuroScrape's Apify affiliate code: if you take a paid Apify plan, Apify may pay EuroScrape a commission, at no cost to you.</sub>
