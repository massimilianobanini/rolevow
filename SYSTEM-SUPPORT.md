# RoleVow — System support and evidence status (English RC-EN-0.2)

> **PUBLIC TEST CANDIDATE RC-EN-0.9 — NOT INDEPENDENTLY PLAYTEST VALIDATED.**
> Scoped adaptation of Divertoscopio `SYSTEM-SUPPORT.md`, commit `08814049a1d655d7ac31028b28239a67b08fe7cf`. This is the proposed **single source of truth** for future public RoleVow support claims; no Italian confidence percentages are inherited.

## Current English system matrix — 15 November 2026

| System / edition | RoleVow English support confidence | State |
|---|---|---|
| **D&D 5e 2014 / SRD 5.1** | **NOT YET EVALUATED** | Adapter and runtime **drafted privately**, no completed independent English actual-play validation; not publicly available |
| **D&D 2024 / SRD 5.2.1** | **NOT EVALUATED** | **Private adapter prepared**; not validated in English actual play |
| **Daggerheart™ (unofficial experimental adapter, SRD 2.0)** | **NOT EVALUATED** | **Private adapter prepared**; English gameplay not independently validated; third-party source terms apply |
| **Other tabletop RPG systems** | **NOT EVALUATED** | No English adapter available in the candidate |

**Important:** Do not display a confidence percentage such as 85%, 75% or 70% from the Italian Divertoscopio matrix. Those are not measured RoleVow English support scores. This table is a *scope and evidence declaration*, not a numerical quality score. It does not mean 0% fun or 0% technical accuracy; there simply is not validated English evidence for a number.

## Runtime routing — one-time, after the user chooses a system

1. Use `BOOTSTRAP.md` alone before the intent gate, including the immutable six-field **PLAY NOW** screen. **Never put this support notice into that locked screen.**
2. After a partial/full Play Now answer or after another route has opened the gate, identify `active_system`. An omitted Player system defaults to D&D 5e 2014 / SRD 5.1; respect an explicitly supplied supported system without asking again.
3. Read this file when available and deliver a short, **one-time, accurate support statement in the first suitable post-selection message**; do not make it another question or delay the first playable scene. State that this is a public technical test, not validated support.
4. If someone requests a different system, do **not** pretend it has a published RoleVow adapter, auto-fallback silently to 5e, or assign a fake percentage. For an unknown system, explain the absence of a dedicated adapter; for D&D 2014, D&D 2024 or Daggerheart route to its specific test adapter when accessible, without representing test status as validation.
5. Repeat the support statement only if the system changes, the user asks about support, or a new session requires a material system decision. Do not repeat it every turn or as a persistent warning.

**Canonical one-time wording for the proposed first English release after all gates:**

> **RoleVow system support — [the selected supported system and edition]**
> **Confidence: not yet evaluated in independent English actual play.** The chosen edition has its own adapter in the expanded test candidate; compatibility does not guarantee a correct ruling or a particular gameplay outcome.

**Wording for a system outside the candidate:**

> **RoleVow system support — [system/edition]**
> **Not yet evaluated in independent RoleVow English actual play.** An adapter can be prepared without being proven; no automatic conversion is made between rulesets.

## When a future percentage may be published

A numeric estimate requires: a documented metric definition (mechanical correctness vs onboarding quality vs player enjoyment, not a blended opaque score); test protocol; English human testers/sessions or suitably representative external evidence; sample counts; dates; test configuration; failure counts, correction burden, version lock, reproducibility and limitations. New independent evidence and serious regressions can change the estimate. An internal guess or familiarity of the model with a game is not sufficient.

If no defensible number exists, continue to publish **NOT EVALUATED**. Never conflate this with a probability of enjoyment, customer satisfaction, correct mechanical decisions or guarantee eligibility.

## Ownership and release control

Only the reviewed `SYSTEM-SUPPORT.md` should contain RoleVow support confidence values. README, adapter, player, Game Master, runtime and marketing must reference it rather than duplicate stale numbers. The exact dated version must be checked with [KNOWN-LIMITATIONS.md](KNOWN-LIMITATIONS.md), [LEGAL-CLAIMS.md](LEGAL-CLAIMS.md), the source adapter and the gate A–H. An update to public support claims is a controlled release change, never an implicit automatic translation from the Italian project.
