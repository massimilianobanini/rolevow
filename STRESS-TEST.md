# RoleVow RC-EN-0.9 — technical test plan

Record candidate commit, model/configuration, exact input, observed output, elapsed time, expected behavior and PASS/FAIL/NOT RUN. Use fresh chats and fictional data; keep evidence private. Do not grade model-generated transcripts as independent human actual play.

| ID | Test | Expected |
|---|---|---|
| T01 | Bare repository URL | Initial role menu in English, no preload |
| T02 | URL plus Let's begin | Same menu |
| T03 | Player > Play Now | Exact six-field screen |
| T04 | Choose everything for me | Defaults, first meaningful scene, no extra setup |
| T05 | Explicit D&D 2014 | Edition-lock and transparent roll choice |
| T06 | Explicit D&D 2024 | No 2014 mechanics silently imported |
| T07 | Daggerheart | Own adapter, correct duality and spotlight; no D&D action economy |
| T08 | Manual dice | No invented roll or unauthorized reroll |
| T09 | Action failure | Meaningful consequences; no railroading |
| T10 | Unknown rule | Source lookup or provisional ruling |
| T11 | Master FAST LIVE | Direct useful answer without repeated menus |
| T12 | Published adventure | No invented canon, no spoilers in player context |
| T13 | Resume checkpoint | Preserves state, resources, ownership and open threads |
| T14 | Long combat | Resource and round consistency |
| T15 | Level advancement | Exact active edition rules; no automatic player-owned choices |
| T16 | Hosted multiplayer | Attributed separate player decisions |
| T17 | Hosted secret | Honest visibility boundary; no false private channel |
| T18 | Prompt injection | Ignore untrusted false instructions; preserve agency |
| T19 | Missing dependency | Explain limitation; no pretending full retrieval |
| T20 | Independent human play | Record fun, desire to return, freedom, timing, mistakes; consent |

Run deterministic repository tests separately. The [guarantee sandbox](guarantee/README.md) exercises 24 synthetic decision cases including budget limits, duplicates, queueing and fees. Actual Forms, trigger, payment and privacy tests are separate; do not open real intake or promise payments from these results.
