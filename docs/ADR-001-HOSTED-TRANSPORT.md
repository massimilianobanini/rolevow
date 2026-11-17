# ADR-001 — Hosted Multiplayer Transport for RoleVow V1

**Status: ACCEPTED BY OWNER on 2026-11-15, NOT FUNCTIONALLY VALIDATED.**
**Release:** RC-EN-0.9 public technical test; independent English multiplayer validation pending.

## Decision

V1 supports multiple human tabletop participants through exactly **one human host and one ChatGPT conversation**. A host relays attributed actions and player-safe responses to the group. The host can be in person or on an external voice/video call; RoleVow supplies no synchronizer, login, shared multi-account chat or private player channels.

## Options explicitly rejected from V1

- Multiple users typing concurrently into a synchronized RoleVow chat, backed by a server/state store: different architecture, maintenance, authentication and privacy risks.
- Sharing account credentials: unacceptable account/security model.
- Treating a shared ChatGPT link as bidirectional synchronization: unsupported.
- AI-generated private player notes hidden from the human host: the same chat cannot enforce that confidentiality.

## V1 behavioral requirements

1. **Actor authority:** host messages must identify which player/PC is acting for any consequential intent, roll or character choice. Unattributed ambiguous action → ask for attribution rather than assign it.
2. **Player ownership:** no silent action, emotional response, build choice or dice mode for a quiet, absent or non-consenting PC. Delegation must be player-authorized and scoped.
3. **Consent to dice:** each player establishes their own dice source at their first needed roll. Numeric values are results, not menu options. AI permission is not proof of randomness.
4. **Simultaneous situations:** when intents interact, collect the necessary attributed intentions before resolving; preserve rule-triggered reactions and voluntary abstention.
5. **Information:** PC knowledge is tracked separately even if humans hear table-wide narration. Player-visible checkpoints never expose unrevealed DM truths. Host visibility is always disclosed.
6. **Split party:** keep independent location, fictional time, resource and PC-known facts; merge only after plausible in-world rejoining.
7. **PvP and safety:** table consent before escalating coercive inter-PC action. Any participant can stop/skip/veil/rewind. A human interpersonal problem is not a narrative subplot.
8. **Ruleset lock:** follow the selected 2014, 2024 or Daggerheart adapter for every procedural interaction; no edition mixing. Any source-dependent adapter must satisfy applicable third-party rights and applicable requirements.
9. **Data:** do not request real player names, contacts, accounts or other personal information to route game actions.

## Evidence necessary before GO

Reference fixtures and deterministic checks are necessary but insufficient. Run actual independent English ChatGPT sessions with two and four human players using one host; retain only consented, redacted evidence and capture per-PC dice attribution, absent players, split-party secrecy, conflicts, interruptions, FUN, Desire to Return, and error/correction burden. Only a tested fresh chat with exact frozen Markdown proves behavior of that configuration.

## Revisit trigger

Separate accounts become a potential **new release** only if user value and evidence justify a backend, authentication, data-processing arrangements, and associated cost. This ADR must not be silently reinterpreted as multi-account support.
