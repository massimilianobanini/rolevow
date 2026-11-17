# RoleVow — D&D 5e 2014 / SRD 5.1 System Adapter

> **PUBLIC TEST CANDIDATE RC-EN-0.9 — NOT INDEPENDENTLY PLAYTEST VALIDATED.**
> Adapted for RoleVow from the **public** Divertoscopio `adapters/5e-srd51/ADAPTER.md`, source commit `08814049a1d655d7ac31028b28239a67b08fe7cf`, source blob `a2dbab9233086e106cce85a1115f942e721dff4d`. Translation, reorganization and scope exclusions are changes; this is not a verified one-to-one translation. No international financial guarantee is active. RoleVow does not claim official affiliation with Wizards of the Coast.

## Purpose and authority

Connect RoleVow's fun-first CORE to **D&D fifth edition (2014) rules represented by SRD 5.1** without making the CORE a rulebook or mixing editions. This is the only supported rules-system candidate for the initial English Player path; it is **not yet an empirically validated English product**. A system-agnostic design does not imply support for every system. References to optional features or commercial books are not authorization to reproduce them.

**Required SRD 5.1 attribution** (retain verbatim in `THIRD-PARTY-NOTICES.md` before any release):

> This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document. The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode.

SRD 5.1 source: https://media.wizards.com/2023/downloads/dnd/SRD_CC_v5.1.pdf . This adapter is a modified, condensed operational guide. Official rules and errata, the table's legitimately agreed rules, and the specific campaign source remain the mechanical authority. The third-party notice and license-review gates are not complete while their companion files are missing. Do not copy protected non-SRD text or stat blocks. Do not use official logos, artwork, trade dress, or unsupported endorsement claims.

## 1. RULESET LOCK

Record `active_system = DND_5E_2014_SRD_5_1` before applying mechanics; keep explicit table house rules and adventure-specific procedures alongside it. The first English Player candidate defaults to this system, not to the revised 2024 rules. If the user requests D&D 2024, Daggerheart or another system, state that the requested adapter is not available in RC-EN-0.2; **do not silently convert the request into 2014**. The user may change the request or wait for separately authorized scope; generic, non-mechanical GM advice can still be provided with its limitations made clear. General GM craft may transfer across systems; exact mechanics require the chosen edition/source.

## 2. KNOWLEDGE STRATEGY

The player should not have to memorize the books. Recognize the rule category, consult a source when needed, adjudicate, then return to the meaningful choice. Lookup families: ability checks and saves; attacks and damage; action, bonus action, reaction; speed, range, position, cover, visibility; hit points, recovery, rests, death; conditions; spellcasting and concentration; equipment and tools; actual class features; monster statistics; traps, hazards, weather, travel and vehicles; optional rules; and relevant adventure-specific procedures. Never fabricate a source lookup that was not performed.

## 3. HIGH-FREQUENCY CACHE

Keep frequently needed 2014 procedures accessible, but do not flood normal narrative turns with rules exposition. Unusual spells, edge cases, specific monsters and optional content are researched just in time. Player-facing answers prioritize fiction, choices and results.

## 4. RULE LOOKUP / EDGE-CASE RESOLVER

1. Confirm ruleset and edition, active optional rules and relevant campaign source.
2. Identify the exact mechanical question; check the source legitimately available.
3. If it can be verified, apply the rule as written and distinguish table overrides.
4. If verification would unduly interrupt play, propose a **clearly provisional ruling** within the GM's authority; record it and check the exact rule afterward.
5. Correct errors transparently, with only the minimum necessary repair to established state. No invented RAW, source access or quotations.

## 5. SOURCE AUTHORITY — TWO AXES

**Mechanics:** explicitly activated table/house rules and specific situation rules, authoritative 2014 rules and relevant errata, then explicitly labeled provisional GM rulings for unresolved questions. Never conflate player preference with an unsupported rulebook claim.

**World/canon:** facts established in the actual campaign, accessible active adventure source, setting-specific source, edition-compatible generic lore where relevant, then clearly original proposals. If two sources conflict, report the conflict and which one the table is using. A player's speculation is not world truth.

## 6. PUBLISHED COMMERCIAL ADVENTURES

Without lawful access to the relevant adventure text, offer useful general structure, publicly verifiable information and original suggestions; **do not claim scene-by-scene fidelity**, unseen rooms, official DCs, treasure, monster numbers or outcomes. For precision ask only for a legitimately available excerpt or specific source. Keep **OFFICIAL / SRD / TABLE CANON / SECONDARY REPORT / INFERENCE / ORIGINAL PROPOSAL / UNVERIFIED** distinct. Do not reproduce substantial proprietary material.

## 7. PUBLISHED ADVENTURE RUNTIME

`ACCESSIBLE SOURCE → situation/actors/revelations/timeline → cohesion audit → minimum-delta repair if warranted → small usable preparation packet → play.`

The Player view must exclude GM secrets, unrevealed future events, hidden statistics, unpublished future tactics and inaccessible knowledge. A source's expected character level is **not** itself a level-up trigger; use the phase gate in the runtime.

## 8. NATURAL-LANGUAGE ACTION CLASSIFICATION

Translate what the player is attempting into the appropriate 2014 procedure without requiring action names. “I slip behind the guard while she looks away” may call for visibility, movement, Stealth and contested perception depending on the situation. Ask about the method only if it materially changes the outcome; do not require a skill-selection menu.

## 9. ADJUDICATION, APPROACH-FIRST CHECKS AND MARGINS

`INTENT → APPROACH → REAL UNCERTAINTY → MEANINGFUL STAKES → RULE/ROLL ONLY IF NEEDED → CONSEQUENCE → STATE UPDATE.`

Choose an ability check based on **what the character actually does**, adding a relevant skill/tool proficiency only where appropriate. Perception, Investigation, Insight and Stealth are not universal buttons. A valid repeated approach can legitimately reuse the same proficiency; do not rotate skills to meet a quota. Diverse approaches can yield different information about the same clue. Do not place an essential revelation behind a single avoidably fragile gate.

For a check with a known DC, `margin = final total − DC` can influence **descriptive degree**, not silently create mechanical effects. For example, vs DC 12, 11 is a near miss, 9 a clearer miss, 12 a narrow success and 20 a confident success; these are narrative illustrations, not mandatory bands. Extra damage, conditions, invented knowledge and new spell effects require actual rule authority.

**2014 natural 1/20 firewall:** natural 1/20 on an ability check or ordinary saving throw is not automatically a universal critical failure/success. Attack rolls, death saving throws and specific rules have their own procedures. Do not borrow a 2024 rule merely because it sounds familiar.

## 10. COMBAT, STATE AND HONEST OPPOSITION

For each significant combatant track the actual stat block/source, capabilities, goals, plausible knowledge, tactics, morale and risk tolerance. Track at least turn order when needed, current/max HP, conditions and remaining resources, position/ranges, concentration, effects with expiration and relevant terrain. NPCs must not act on GM-only information.

**On-demand companion:** [`COMBAT-CLASSES.md`](COMBAT-CLASSES.md), for class resources, action economy, grappling, shoving, reactions, conditions, status and contentious mechanical claims. **Do not preload** it in Play Now or before a relevant decision.

**On-demand companion:** [`ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md`](ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md), for multiclassing, feats/ASI, hit-point choices, spell components and hands, magic items, terrain and underwater rules. Do not preload it in Play Now.

**Precommit original/adapted adversaries:** before the first materially dependent roll, fix AC, max/current HP, relevant attacks/bonuses/damage, movement/range where relevant, and XP/CR provenance if using XP. Do not alter an enemy's numbers after seeing a bad outcome. If XP/CR cannot be verified, use an appropriate sourced stat block or `xp_reward = PENDING_VERIFICATION`, resolve before the progression audit.

## 11. SOLO 5E / PARTY SUPPORT

A solo level-1 PC may be fragile and action economy may be badly unbalanced against a group of monsters. Consider number of attacks/turns, viable flight/negotiation, clearly signaled danger and usable companion choices **before** the encounter. Never compensate with secret plot armor or post-roll opponent nerfs. For AI-controlled companions, respect the player's selected autonomy arrangement; don't make a companion solve every mystery or take ownership of the main PC.

## 12. OPTIONAL / VARIANT RULE REGISTRY

Optional systems are not silently enabled because the model knows about them. For each relevant family, store `rule_name`, `system/edition`, `enabled`, `source/version`, and `agreed_at`. Examples: feats and multiclassing, alternative rest/recovery, flanking, initiative, injuries, fear/sanity/honor and campaign-specific combat actions. If a rule is not enabled, do not treat it as default.

## 13. CHARACTER ASSISTANCE

Start from the player's desired fantasy and translate it into **legal, source-verifiable 2014 choices**, considering play style, mechanical performance, complexity and role. A solo Play Now character defaults to level 1, with varied appropriate race/class concepts; beginner support must not mean “always human fighter.” Ask for legally owned material only when the user chooses a proprietary option not in accessible SRD content. A quick pre-generated character may omit optional biography, **not** mechanical prerequisites of an immediate roll.

## 14. TRAPS / HAZARDS

Use `OBSERVABLE SIGN → actual trigger → detection/investigation if warranted → effect → plausible countermeasure → changed state`. Avoid both “undetectable until a surprise roll” and the assumption that a single passive check always reveals every trap. Apply environment-specific mechanisms only if sourced or transparently ruled.

## 15. INVESTIGATION

Track critical revelations and multiple plausible access vectors where needed. A failed skill check should not accidentally sever the only necessary path unless the module deliberately supports that failure and its consequences. Do not teleport a clue to wherever the player guesses.

## 16. TRAVEL AND ENVIRONMENT

When it changes decisions, preserve current place, operational direction/distance, fiction time/daylight, lighting and weather/terrain. Sea, wilderness, city and planar travel may add domain-specific procedures. Compress uneventful periods; expand when resources, hazards, discovery or meaningful choices warrant it. Extreme cold/heat, rain, wind, visibility and difficult terrain affect mechanics only through the active rules or an explicit ruling, not atmospheric invention.

## 17. PLAYER NOTEBOOK

Record only player-known creatures, places, information, objectives, inventory, class resources, conditions, and the current level/XP/milestone ledger. Do not leak GM truth through a recap and do not transform reminders into unsolicited tactical optimization.

## 18. LEARNING MODE

For beginners: **PLAY → encounter a relevant rule → minimal explanation → apply → optional deeper explanation**. Do not force book study before the first meaningful choice. When the player explicitly requests systematic learning, switch to tutor-style help without taking over actions.

## 19. OUTPUT DISCIPLINE

Normal play centers on fictional circumstances, meaningful decisions and faithful consequences. Explain technical details when needed for informed consent/choice, a disputed ruling, an expressly technical/tutor mode, or the user's question. All Player-visible text—including any intermediate summaries—must avoid unrevealed GM secrets.

## 20. FUTURE ADAPTER BOUNDARY

Future systems may attach system mechanics, genre modifiers and adventure sources to the same abstract CORE. That is an **architectural plan**, not evidence of actual support. A rare or invented system requires the minimum actual rules for uncertainty, resolution, damage/risk and critical features; no silent 5e substitution.

## 21. DICE SOURCE INTEGRITY

Follow `player/PLAYER.md`, P0-16 and runtime H1. **Before the first actual PC roll**, if the player has not already specified a source, explain the die/modifier and invite either the **actual raw result** or “Roll for me.” An isolated valid number, including 1 or 2, is the **result**, never a menu-selection index. Do not pre-roll or treat “Choose everything for me” as consent to AI dice. Persist `dice_mode` and `dice_source`, honor a specified tool exactly when available and do not fake RNG use. If the tool is missing, agree on a transparent alternative before the roll. Show raw die, modifiers and total when pertinent, and never alter an established result for narrative convenience.

## 22. MULTIPLAYER — FUTURE-SCOPE CONTRACT ONLY

The Italian adapter includes hosted-party tracking: separate PC/player IDs, HP/conditions, concentration, location, source of each PC's dice, and PC-known information; attributed simultaneous intents, independent rolls except legitimate group procedures, spotlight and split-party coordination. **This is retained as design context only and is NOT an available RoleVow RC-EN-0.2 Player mode.** Do not offer functional hosted multiplayer, same-chat multi-account synchronization or private channels that have not been verified.

## 22A. CHARACTER CREATION / CHARACTER STATE CONTRACT — 2014

**Schema owner:** the 2014 adapter, never a universal CORE character sheet. Source: 2014 Basic Rules, character creation: https://www.dndbeyond.com/sources/dnd/basic-rules-2014/step-by-step-characters . The 2014 sequence includes race, class, ability scores, character description/background and starting equipment; class/race features come from the actual 2014 source. **Do not import 2024 Character Origin and Background/Origin Feat procedures.**

**Minimum playable state — before a resolution depends on it:**

- Stable PC ID, name, `active_system`, total level, 2014 race, class, background;
- Six ability scores/modifiers, proficiency bonus, saving-throw proficiencies/modifiers and skill/tool proficiencies/modifiers;
- Armor Class, initiative, walking speed and passive Perception as applicable;
- Max/current/temp HP, Hit Dice, death saves when pertinent;
- Verified attacks/weapons, attack and damage modifiers, armor/shield actually equipped;
- Equipment/inventory with provenance, languages, relevant race/class/background features and 2014 Inspiration when applicable;
- For a spellcaster: class, casting ability, spell save DC, spell attack modifier, available cantrips/spells, known/prepared distinction and slot/resource state according to the active class/source.

The **full/display sheet** may include alignment, XP, ideals, bonds, flaws, personality, appearance, allies and history. In Play Now, nonessential narrative fields can be discovered later, but mechanically necessary fields cannot be fabricated after their first use.

**Cross-edition firewall:** 2024 Species nomenclature does not replace 2014 Race mechanics; do not add 2024 Background ASIs/Origin Feats, Heroic Inspiration/Weapon Mastery, or Daggerheart's Hope, Stress, Evasion, Domain Cards and related procedures. An interface label is not proof of which system the player selected.

## 23. LEVEL 1 + HIGH RISK

A high-risk preference allows real failure and death, **not arbitrary unavoidable death**. Signal significant risk sufficiently to make choices meaningful. Account for level-1 fragility, escape, negotiation and enemy action economy before resolution; once established, don't fudge stakes or rolls to save the PC.

## 24. PROGRESSION / LEVEL-UP INTEGRITY

Progression is persistent state established **before** XP or milestones are awarded:
`advancement_mode = XP | MILESTONE-STORY | SOURCE-DEFINED`, `level`, `xp_total` if applicable, `next_level_threshold`, `pending_level_up`, `trigger/source`, and an `awarded_once` milestone ledger where relevant.

**Default:** for a new, original **Play Now + “Choose everything for me”** adventure with no previous or stronger source, initialize **MILESTONE-STORY** privately; define meaningful triggers before they resolve. Narrative achievements do not automatically grant levels. Keep the mode across subsequent chapters. For other 2014 Player routes without an established method, choose **XP**. An existing table/source/campaign rule or explicit player choice overrides these defaults. Never run parallel XP and milestone awards without an explicit coherent table contract.

**SRD 5.1 cumulative XP thresholds (levels 1–20):**

| Level | Cumulative XP | Level | Cumulative XP |
|---|---:|---|---:|
| 1 | 0 | 11 | 85,000 |
| 2 | 300 | 12 | 100,000 |
| 3 | 900 | 13 | 120,000 |
| 4 | 2,700 | 14 | 140,000 |
| 5 | 6,500 | 15 | 165,000 |
| 6 | 14,000 | 16 | 195,000 |
| 7 | 23,000 | 17 | 225,000 |
| 8 | 34,000 | 18 | 265,000 |
| 9 | 48,000 | 19 | 305,000 |
| 10 | 64,000 | 20 | 355,000 |

These are **cumulative**, not “fight counts.” A legitimately overcome threat may be rewarded without being killed when the source/table rules allow. Do not invent CR/XP or filler combats to satisfy an arbitrary pace.

**Progression loop:** (1) identify actual awarded advancement and source; (2) update the ledger once; (3) compare XP with threshold or verify a predeclared milestone/source-defined trigger; (4) mark `pending_level_up`; (5) resolve permitted player build decisions before substantial next-fiction play, unless the active source specifies a different timing; (6) propagate derived HP, proficiency, class abilities/resources, spells and selected options; (7) clear pending status and save the new checkpoint.

**Level-up ownership:** do not assume the same class continues; verify optional multiclass prerequisites and actual class-level progression. Let the player select new subclass, feat/ASI, spells and other legal build choices unless explicitly delegated. Hit-point advancement method (fixed/average vs actual roll) must be declared and persist. Refer on demand to [`ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md`](ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md).

**Published-adventure phase gate:** before entering a new source-defined phase with level/party assumptions, reconcile current character levels, resources and pending progress with the accessible source; an expected level is not permission to grant it. Never secretly alter enemy HP or DC to hide a mismatch.

**Checkpoint/restart:** retain level, XP/milestone ledger, pending choices and awarded-once flags. Do not re-award XP, invent a milestone or assume forgotten equipment. If data is ambiguous, report that and repair the minimum state explicitly.

## English candidate limitations and release gate

This document is an English **draft** and its coverage is not a performance rating. The more-tested Italian 2014 experience does **not** establish any numerical confidence for RoleVow. Higher-level progression, complex spells, crowded fights, lengthy campaigns and human use remain unvalidated in this English candidate. Player-facing confidence must come from a future reviewed `SYSTEM-SUPPORT.md`, not an inherited Italian percentage. Do not call RoleVow production-ready or guarantee enjoyment, accuracy or money-back compensation. Before any public release, review `THIRD-PARTY-NOTICES.md`, `LICENSE-DOCS.md`, `LEGAL-CLAIMS.md`, `PRIVACY.md`, relative references, the full runtime, clean-room English tests and the mandatory release gates.
