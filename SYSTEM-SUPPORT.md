# RoleVow — System support and evidence status

> **PUBLIC TEST CANDIDATE RC-EN-0.9 — NOT INDEPENDENTLY PLAYTEST VALIDATED.**
> Single source of truth for RoleVow player-facing support estimates. The provisional reference values below are authorized for display, inherited from the [Divertoscopio support matrix](https://github.com/massimilianobanini/divertoscopio/blob/main/SYSTEM-SUPPORT.md) consulted on 17 November 2026, not derived from English-language measurements.

## Current English system matrix — 17 November 2026

| System / edition | Provisional upstream support estimate | Independent English validation | State |
|---|---:|---|---|
| **D&D 5e 2014 (SRD 5.1)** | **85%** | **NOT EVALUATED** | Dedicated test adapter; English validation pending |
| **D&D 2024 (SRD 5.2.1)** | **75%** | **NOT EVALUATED** | Dedicated test adapter; English validation pending |
| **Daggerheart™ (unofficial experimental adapter, SRD 2.0)** | **70%** | **NOT EVALUATED** | Unofficial experimental test adapter; third-party source terms apply |
| **Other tabletop RPG systems** | **NOT EVALUATED** | **NOT EVALUATED** | No dedicated English adapter in this candidate |

The percentages are internal, provisional reference estimates from the Italian project (adapters, stress tests and actual play); they have not been independently established for RoleVow. They are not measured English rules coverage, a probability of fun, a probability of a correct ruling, or guarantee eligibility.

## Runtime routing — one-time, after the user chooses a system

1. Use `BOOTSTRAP.md` alone before the intent gate. Never add the support notice to the immutable six-field PLAY NOW screen or preload it before the gate.
2. Identify the active system once chosen or defaulted. Applies to Play Now, Customize First, Customize in Depth, direct starts and relevant resumed games.
3. Read this table and show the short canonical callout once in the first useful post-selection response, then proceed directly to play or preparation.
4. For unknown systems, or if the estimate cannot be retrieved, say not evaluated; never invent a percentage or silently switch rulesets.
5. Repeat only if the active system changes, the user asks for the support status, or a new session requires a material system decision. For human Game Master assistance, use the support text without a Player label.

### Canonical Player-facing callout

> **Game Master → Player (OOC)**
>
> **RoleVow system support — [SYSTEM]**
>
> Current support estimate: **[X%]** (provisional reference from Divertoscopio).
>
> *Independent English gameplay validation: not yet evaluated. This is not a guarantee of rules accuracy or enjoyment.*

For systems with no estimate:

> **Game Master → Player (OOC)**
>
> **RoleVow system support — [SYSTEM]**
>
> Current support estimate: **Not evaluated.** No reference percentage is available.

Use plain Markdown blockquotes, not interactive controls. Keep the story outside the callout.

## Updating the estimate

The reference estimate may change after a documented upstream update or new adapter evidence. A distinct RoleVow-specific measured estimate requires a documented metric definition, a versioned test protocol, sample sizes and dates, representative independent English tests, failure counts, correction burden and reproducibility limits. Never silently relabel an upstream number as English evidence. A static regression test or this single technical playtest does not establish a percentage.

## Ownership and release control

Only this document maintains the numeric support matrix. README, router, Player/Master guidance, runtime and marketing should reference it rather than duplicate values. Review against [KNOWN-LIMITATIONS.md](KNOWN-LIMITATIONS.md), [LEGAL-CLAIMS.md](LEGAL-CLAIMS.md) and source/adapter evidence when changing the estimate. No change to release approval or monetary guarantee status follows from this display.
