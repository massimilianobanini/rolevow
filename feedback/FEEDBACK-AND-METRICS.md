# RoleVow — Feedback and Metrics: Technical Contract

> **PUBLIC TEST CANDIDATE RC-EN-0.9 — NOT INDEPENDENTLY PLAYTEST VALIDATED.**
> Adapted from Divertoscopio `feedback/FEEDBACK-AND-METRICS.md`, public commit `08814049a1d655d7ac31028b28239a67b08fe7cf`, blob `ea55bde1b9b5c65df56051aea6d5bfa6fdd0c0c5`. The Italian €1 claims flow, 100-claim cap, identifying fields and payment collection are **not** part of this English technical draft.

## Purpose

Measure whether people actually enjoy RoleVow, voluntarily want to play again and receive useful, mechanically faithful assistance at acceptable effort. The quality of the experience—not the amount of generated text or number of turns—is the object of measurement.

## Operating principle: ASK ONLY WHAT CANNOT BE OBSERVED

Do not interrupt play with repeated surveys. Use at most **one concise optional feedback invitation** after a significant unit or explicit dissatisfaction, using the published English survey and its privacy notice. The [official English form](https://docs.google.com/forms/d/e/1FAIpQLSdBBYqPZkuFF0t1OeLhqHa8k2UKefT0HbHWXGabX4KDjyJuGw/viewform) is available; conversational feedback must not be described as externally recorded, and no payment data should be collected in chat. A neutral break is not a failure claim.

## North Star measures

- **FUN (0–10):** “How much did you enjoy this session?”
- **DESIRE TO RETURN (0–10):** “How much would you want to come back for another session because you enjoyed this experience?”
- Optional **Best Thing** and **One Main Change**.

Desire to Return must not be manipulated using FOMO, forced cliffhangers or artificially endless play. Human-rated emotions are not inferred solely from the model's narrative descriptions.

## Observable diagnostics, when genuinely available

Track agency/player ownership; turns/time to first real decision; rolling and source integrity; mechanical corrections; state and memory contradictions; knowledge leaks and spoilers; false choices/railroading; pacing; natural closure; checkpoints/resume accuracy; extra model/tool/media latency; player corrections; and GM prep used. **UNKNOWN is allowed** and must never be replaced by an invented value.

For English V1, stratify by **active ruleset** (2014, 2024, Daggerheart) and play mode (Solo, hosted group) before comparing outcomes; small samples or different table types are not proof of product superiority.

## Context when already known

Product version, test date, role, exact ruleset/edition, solo/hosted, player count where voluntarily declared, source lock, adventure type, interaction mode and tool availability. Model/plan/settings are recorded only if exposed or volunteered—never guessed. Use non-identifying stable handles for group participants; no names or contact details are necessary to measure the play experience.

## Game Master metrics

Measure prep time where known, material genuinely used, correction burden, prep that saved or created effort, GM stress/friction and time to first genuinely actionable response. Do not add a second mandatory GM questionnaire.

## Evidence provenance

For each claim or measurement distinguish `DECLARED`, `OBSERVED`, `INFERRED` and confidence. A happy player can have needed many corrections: reported fun and mechanical accuracy are separate outcomes. Expert rescue by a capable human does not prove a beginner-baseline pass.

## Correction burden

Count, when the log is legitimately available, corrections of rules, continuity, resources/inventory, recovered player agency, reminders of already-established preferences, untriggered dice/rule gates and unsupported source assertions. Do not demand or store private transcripts by default. If a tester voluntarily offers a transcript later, apply the approved privacy data flow and redaction controls before collection.

## Hosted-group diagnostics

Measure fairness of spotlight, delay between meaningful opportunities per player, attribution errors, independent dice-mode integrity, PC knowledge leakage, absent-PC takeover, Shared Decision Commit Window friction, split-party time and the burden placed on the human host. A group score cannot be treated as each individual's score without evidence.

## Active international guarantee — separate from gameplay metrics

The RoleVow Negative Price Ultra-Guarantee is **ACTIVE since 19 November 2026** under its [published terms](../guarantee/TERMS.md) and the [official English form](https://docs.google.com/forms/d/e/1FAIpQLSdBBYqPZkuFF0t1OeLhqHa8k2UKefT0HbHWXGabX4KDjyJuGw/viewform): €1 NET per eligible person, a single payout across both RoleVow and Divertoscopio, a €20/month and €100 lifetime GROSS ALL-IN cap including fees and FX, and host-only monetary eligibility in hosted games. A complete form submission establishes chronological priority only; manual qualification plus binding full-cost reservation is the approved internal design, subject to legal review. **The English form is open; payout is conditional on eligibility, manual review, available funding and a lawful workable transfer route. No payment is automatic.** Do not solicit payee identity, account details, private chat exports or payment methods during ordinary play. Feedback remains independent of claim submission, and claim information belongs only in the official approved English process described in the [privacy notice](../guarantee/PRIVACY.md).

## Iteration

USE → (optional consented) FEEDBACK / OBSERVED FAILURE → classify by role, system, severity and actual cause → prioritize one to three changes with highest expected effect and lowest test cost → new version-locked tests.

Typical failures: excessive onboarding, unsupported rule, wrong edition, user action takeover, hidden fudging, knowledge leak, pacing drag, improper resource state, false choice, feature overload, premature NPC solution, arbitrary consequence, unfinished chapter, impossible legal claim or privacy leakage. Successes include player agency, fast meaningful choice, recognizable world consequences, faithful source decisions, interesting non-coerced emotions, useful GM assistance and voluntary Desire to Return.

## Release and version boundary

The official English form is active, while this document itself collects no identifying data. The exact RoleVow runtime and the currently published English form must each carry independent version identifiers. A 2014 test cannot automatically certify 2024 or Daggerheart. An Italian game test cannot certify English localization. Do not present data from the Italian public guarantee as RoleVow performance.
