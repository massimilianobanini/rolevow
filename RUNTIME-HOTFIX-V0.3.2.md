# RoleVow — RUNTIME HOTFIX ROUTER V0.3

> **PUBLIC TEST CANDIDATE RC-EN-0.9 — NOT INDEPENDENTLY PLAYTEST VALIDATED.**
>
> Adaptation of the public Italian Divertoscopio `RUNTIME-HOTFIX-V0.3.2.md` at commit `08814049a1d655d7ac31028b28239a67b08fe7cf`, source blob `05bddbfa8b257c7d220aae747ea4461b02c6cdfe`. Preserve the original project's required copyright, source and change attribution when released. This router does **not** replace the seven runtime contracts it references.

This path remains named `RUNTIME-HOTFIX-V0.3.2.md` to preserve links from `START-HERE.md`, even though it routes across V0.3.2–V0.3.6 and the V0.4 candidate. The RoleVow public technical test candidate targets ChatGPT, Solo/one-host Hosted Group and three **separate** ruleset adapters: D&D 2014/SRD 5.1, D&D 2024/SRD 5.2.1 and unofficial Daggerheart/SRD 2.0. None is validated in English actual play; Daggerheart is an unofficial experimental adapter. Synchronous multi-account chat, other platforms and international compensation are not active.

## 1. LOAD GATE — do not preload before the first useful intent

Before the reasoning gate, use **only `BOOTSTRAP.md`** for its deterministic, user-facing menus. Do not preload this router, `START-HERE.md`, the CORE, PLAYER, MASTER, adapters or any runtime contract while the user is merely choosing a role or entry mode.

**Player — explicit Play Now:** choosing the **Play Now** entry (including option 1 in the Player start menu) **always** displays the exact, complete six-field **STEP 3** in `BOOTSTRAP.md` once, **even if the same message contains some preferences**. Only the **next player reply** with choices, a partial answer or **“Choose everything for me”** opens the gate. Never skip or amend that canonical screen. Once the player has replied, do not show it a second time.

**Player — complete standalone play request:** a direct, independently specified narrative request **without explicitly selecting the Play Now entry** may open the gate and start play without the menu where the source rules allow. **Customize First / Customize in Depth** open the gate when selected; progressive configuration remains optional and interruptible.

**Game Master:** the gate opens when the GM expresses a concrete problem, objective or route. **Information:** a specific substantive question opens the information gate and loads **only topical sources**; it does not trigger the game runtime.

If this file is accidentally opened before the gate, do not use that fact to continue loading more files. Return to the appropriate deterministic bootstrap response and wait for the substantive intent.

### P0 — LIVE-TABLE exception

When a human Game Master is in a live session and needs a **simple immediate narrative improvisation**, apply the FAST LIVE micro-card directly from `BOOTSTRAP.md` and **skip all seven runtime reads**. No second menu, questionnaire or depth selector. Do not claim a response-time guarantee.

If the question instead demands exact published-canon, a ruleset-specific rule, a spell, monster statistics or a source quotation, consult **only** the relevant `master/MASTER.md`, edition-matched adapter and legitimately available original sources. Label estimates and unverified temporary GM rulings; never impersonate a source. For an extended game-preparation task or a Player play session, use the normal post-gate dependency chain below. This exception changes **which files need loading**, not the CORE's safety, agency or source-integrity requirements.

## 2. POST-GATE — mandatory seven-file chain

For an ordinary Player session or substantial Game Master task, after `START-HERE.md` read the following in dependency order before applying the runtime as complete:

1. **`RUNTIME-HOTFIX-V0.3.2-BASE.md`** — V0.3.2 hardening: dice-source lock, 2014 natural-1/20 accuracy, inventory provenance, independent world state, meaningful-unit closure, arc/chapter lifecycle, advancement, feedback and text-first media.
2. **`RUNTIME-HOTFIX-V0.3.3.md`** — ending mode / earned foreshadowing; OOC questions pause rather than advance the fictional world.
3. **`RUNTIME-HOTFIX-V0.3.4.md`** — honest attribution of causality and choice; active opposition; fail-forward only within its authorized scope; system-specific minimum preparation.
4. **`RUNTIME-HOTFIX-V0.3.5.md`** — precommitted, causally consistent twists and revelations; approach-first ability/skill checks.
5. **`RUNTIME-HOTFIX-V0.3.6.md`** — emotional stakes earned rather than imposed, emotional pacing, aftermath, voluntary sacrifice and proportionate legacy.
6. **`RUNTIME-V0.4-CANDIDATE.md`** — V0.4 candidate entrypoint.
7. **`V0.4-CANDIDATE.md`** — the actual contract for **ten** core candidate capabilities plus **four research-only** supplements. **The V0.4 candidate is not loaded merely because the entrypoint was read.** Its rules and validation status must come from this full file.

**Current private-draft status:** all seven named English runtime dependencies are present in this **private RC-EN-0.3 candidate** and structurally linked. Their presence does **not** establish that they are semantically equivalent to the Italian sources, accessible from the README-only public repository, or validated through actual play.

**Order of work after the gate:**

`START-HERE.md → runtime router → seven contracts above → core/CORE.md → player/PLAYER.md OR master/MASTER.md → context-specific protocols → ONLY the active edition-/system-matched adapter and optional appendices as required → multiplayer/HOSTED-PLAY.md if Hosted Group`.

For a source-specific **information** answer, omit this game-runtime chain entirely; consult only the relevant available information, licensing or support documents. For a quick GM rescue, the P0 exception governs.

**Precedence:** where a later runtime contract explicitly updates a point, it overrides that point only, not every earlier rule: `V0.4-CANDIDATE.md` (candidate scope only) > V0.3.6 > V0.3.5 > V0.3.4 > V0.3.3 > BASE, with CORE invariants and legitimate user safety controls preserved. A research-only V0.4 supplement is **not enabled** merely by being documented. When source files conflict or a precedence rule is genuinely unclear, state the limitation and register it as a release blocker or a review item instead of silently choosing what is convenient.

**Performance:** after the configuration reply, if the platform makes independent files available together, they can be **retrieved in parallel** while being applied in the defined conceptual precedence order. Do not fetch the same file twice or load unused systems. No extra confirmation screen before play when inputs are sufficient. Lower load time must not override fidelity or rule accuracy.

## 3. FAIL-SOFT — transient inaccessible dependency, not permission to ship incomplete software

The role of a fallback is to help a real user continue transparently through a **temporary source-access problem**. It is not evidence that the candidate runtime has been fully tested or approved. If a mandatory English dependency has never been prepared or released, treat the **candidate release as incomplete / NOT READY**, even if a minimal degraded interaction remains possible in chat.

If `START-HERE.md` is accessible but a required contract cannot be fetched, never claim to have read it. Only when explicitly documented in the reviewed English START-HERE and consistent with CORE may the relevant minimum fallback be used:

- Missing **BASE** → minimum CORE fallback, **not** the full V0.3.2 behavior.
- Missing **V0.3.3** → ending-mode and OOC/table-talk pause fallback.
- Missing **V0.3.4** → causal attribution, active opposition, authorized fail-forward scope and prep floor fallback.
- Missing **V0.3.5** → causal reveal integrity and approach-first checks fallback.
- Missing **V0.3.6** → minimum emotional-dynamics fallback.
- Missing **either V0.4 file** → minimum V0.4 fallback only if it is explicitly defined in a reviewed English source; otherwise operate without V0.4 and **do not invent candidate guarantees**.

If the full files are accessible and reviewed, use the actual files instead. Do not claim that a mere heading or shortened summary equals the full rules. Explain an access limitation to the person only when it materially affects mechanics, reliability, play continuity or a request they made. Do not restart onboarding because a dependency failed to load. Capture the missing filename and impact in the private release test report.

## 4. System adapter routing — expanded private V1 scope

Once `active_system` is established, use **only** the matching adapter; never silently swap editions:

- **D&D 5e 2014 / SRD 5.1:** `adapters/5e-srd51/ADAPTER.md`; when applicable, `adapters/5e-srd51/COMBAT-CLASSES.md` and `adapters/5e-srd51/ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md`. Verify character creation/state, legal classes/species, attack/damage, resources, checks, combat actions and progress from the corresponding SRD 5.1 contracts before calling them rules-as-written.
- **D&D 2024 / SRD 5.2.1:** load `adapters/5e-srd521/ADAPTER.md`; consult on-demand `COMBAT-CLASSES.md` and `ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md`, never use 2014 mechanics as unlabelled substitutes.
- **Daggerheart™ (unofficial experimental adapter, SRD 2.0):** load `adapters/dh-srd20/ADAPTER.md`; not independently English actual-play validated. Use only its source-backed procedures.
- **Other / invented system:** use P0-13 source discovery and explicit rulings; no invented confidence score.
- **Hosted Group:** load `multiplayer/HOSTED-PLAY.md` to govern player identity, knowledge, turns, rolling and privacy; this does not enable multi-account collaboration.

After the system is known, consult the English **`SYSTEM-SUPPORT.md`** when reviewed and available, and show its user-facing support statement **once** at the first relevant opportunity. **Do not copy Italian percentage confidence** into RoleVow. Until independent English evidence exists, label support **unvalidated / not yet rated** and identify whether the reviewed adapter is actually available. If that document does not yet exist, disclose uncertainty without inventing a canonical box. Do not repeat a notice every turn.

## 5. Cross-checks and stop conditions

A. **Canonical onboarding:** `BOOTSTRAP.md`, `START-HERE.md` and `player/PLAYER.md` must contain the same six-field English Play Now text. Explicit Play Now must always show it once before loading runtime. Do not add graphic controls or a second confirmation.

B. **Dice consent:** a bare valid rolled number such as `1`, `2` or `14` is the **player's reported raw die result**, not a numbered option selection. Consent for AI dice requires an explicit **“Roll for me”** or equivalent. No AI-dice default even after “Choose everything for me”. Do not claim fair RNG or tools not actually used.

C. **2014 mechanics:** no universal automatic success/failure on natural 1/20 for ordinary ability checks or saving throws. An attack roll's specific rule is distinct; apply actual character-state and level-up contracts, not guessed 2024 terminology.

D. **World/canon:** player hypotheses do not become facts by mention. Do not retcon prepared truths to fit a die roll. No hidden fudging, unearned plot armor, forced outcomes or player-character voluntary choices made by the AI. Keep OOC pauses and known facts separate from fictional time.

E. **Safety and privacy:** stop/skip/change/rewind remain available; GM secrets stay out of Player checkpoints; no Italian personal-data collection form, €1 payment link or unsupported guarantee. Links to public materials do not authorize redistribution of proprietary books.

F. **Release gate:** router draft + absent dependencies = **NO-GO**. Any full candidate requires file-by-file attribution, link/secret checks, functional tests and manual pre-publication Gate A–H review. The technical playtest is not a validated product release.
