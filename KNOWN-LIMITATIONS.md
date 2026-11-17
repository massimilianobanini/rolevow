# RoleVow — Known limitations and readiness (English RC-EN-0.2)

> **PUBLIC TEST CANDIDATE RC-EN-0.9 — NOT INDEPENDENTLY PLAYTEST VALIDATED.**
> Scoped adaptation of Divertoscopio `KNOWN-LIMITATIONS.md`, public commit `08814049a1d655d7ac31028b28239a67b08fe7cf`. Italian test evidence cannot be reused as proof that RoleVow works in English.

## Current status: PUBLIC TECHNICAL TEST, NOT VALIDATED

The complete English test candidate is published for controlled technical playtests, not independently validated public use. No English end-to-end human Player or Game Master session has been certified.

## At a glance

| Area | Scope of the first proposed English candidate | Evidence/status |
|---|---|---|
| Platform | ChatGPT text conversations | **Planned; English runtime not deployed or tested end-to-end** |
| Player route | Solo or one-host Hosted Group, D&D 2014/SRD 5.1, D&D 2024/SRD 5.2.1 or Daggerheart™ (unofficial experimental adapter, SRD 2.0) | **Draft implementation only; NOT VALIDATED** |
| Game Master route | Bounded quick improvisation, prep help, published-adventure assistance where sources are available | **Draft; NOT VALIDATED in live English sessions** |
| D&D 2024/SRD 5.2.1 | Private edition-specific adapter prepared | **NOT ENGLISH GAMEPLAY VALIDATED** |
| Daggerheart/SRD 2.0 | Unofficial experimental adapter | **NOT ENGLISH GAMEPLAY VALIDATED** |
| Hosted multiplayer | Single human host relays all players through one ChatGPT chat | **PRIVATE CONTRACT / NOT HUMAN-TESTED**; no synchronized multi-account play promised |
| Screens, images and media | Text-first; other media only on explicit request when platform supports them | **No automatic media or map promise** |
| Runtime V0.4 | Ten design candidates + four research-only ideas | **Draft adaptations; NOT FUNCTIONALLY VALIDATED** |
| Negative Price Ultra-Guarantee | International scheme not activated | **NO MONEY, PAYOUT, CLAIM, TERMS OR COMPENSATION OFFER** |
| Feedback | No verified public English form | **Do not send to Italian Form or claim a functioning English survey** |

## 1. What this does and does not do

RoleVow is an AI-assisted tool for *existing* tabletop RPGs. It is **not a new standalone ruleset**, not a replacement for player choice, not a certified authoritative rules engine, and not an official D&D/Wizards product. A request to roll a die must follow the user's chosen dice source; a language model's improvised number is not proof of a fair random number generator.

The design objective is more enjoyable play with less unnecessary friction; *fun, correct rules and return intention are outcomes to test*, not guaranteed facts.

## 2. Gameplay and rules limitations

- **Edition and rules:** separate adapters for D&D 2014/SRD 5.1, D&D 2024/SRD 5.2.1, and Daggerheart™/SRD 2.0 (unofficial experimental adapter). None is validated in independent English actual play.
- **Solo balance:** A single level-1 character may be fragile. High risk may include permanent failure or death; there is no hidden plot armour. Challenge balance, encounter difficulty, tactically precise maps and high-level combinations remain unvalidated in English.
- **Magic and resources:** Multiclassing, concentration, spell slots, components, inventories, rare class features, conditions and level-up choices can be mishandled by an AI; use the selected system's actual adapter/source, confirm player-owned decisions and correct errors transparently.
- **Dice:** Always ask at the first Player-character die roll unless explicit mode already exists; no silent AI roll. If no reliable permitted randomness source is available, say so and offer an agreed fallback.
- **Narrative state:** The model can forget canon, alter an NPC's knowledge, invent items or turn a player's suspicion into world fact. Snapshots/checkpoints reduce risk but cannot guarantee perfect cross-chat continuity.
- **Adventure endings:** A pause is not a chapter completion; chapter completion is not automatic level-up. V0.4 state recombination, salience, callback-scoping and sidecast rules are research candidates, not proven product performance.

## 3. Game Master assistance

The six-intention Game Master menu includes an urgent **FAST LIVE** output contract: usually 50–100 words for a single issue, or 120–250 for a more involved unexpected location. These are guidance for the *shape of the answer*, not guaranteed response latency or usability. Rule disputes, real-person safety concerns and legal-source questions may require slower, verified handling. The English Master toolbox and pattern index are **included in this test candidate as condensed drafts**; independent source-parity and usability reviews remain OPEN before they can be described as validated. The optional Italian educational Master PDF is not an English-language deliverable.

If asked to improve a published adventure, distinguish the official reference (when actually read), existing campaign canon, secondary player reports, a model's inference and original suggestions. Do not promise exact room-by-room reproduction without the pertinent lawful source.

## 4. ChatGPT as a separate platform

RoleVow is designed for ChatGPT only in this first candidate; no claim is made about other LLM platforms. ChatGPT account status, tools, response times, context, availability, UI and subscription/usage restrictions may affect the experience. **No promise of infinite free play, no interruption, zero delays or permanent memory.** Accounts may have different features; do not require a particular plan, model setting, browser extension or account customization. The platform's privacy, content and usage policies still apply. Do not share accounts or passwords.

Do not claim that a shared ChatGPT link, a shared project or separate chats form a truly synchronized multiplayer session. If a future transport exists, it needs verification and independent tests before being offered.

## 5. Optional visuals, audio and tools

Text-only is the default to reduce latency and keep player agency clear. Images, maps, interactive widgets and audio **do not** appear automatically because a tool exists. If explicitly requested and the platform can provide them, keep fiction and game state as authoritative text and avoid visual spoilers. No tested end-to-end AI↔VTT synchronized position/HP/conditions loop exists. Music selection or uninterrupted soundtracks are not validated services.

## 6. Safety, social issues and private information

Stop, skip, change and rewind can be requested throughout play. Player decisions, voluntary PC emotions and the safety of real people take precedence over dramatic pacing. A Game Master request about harassment or interpersonal conflict is treated as a real-world concern, not in-character plot fuel. Do not request personally identifiable transcripts of other players or minors. Sensitive information should not be placed in public GitHub issues; consult [PRIVACY.md](PRIVACY.md).

## 7. Support confidence: no inherited percentages

**As of this test candidate there is no calibrated RoleVow English support percentage.** The 85% D&D 2014, 75% D&D 2024 and 70% Daggerheart values in the Italian project's separate support matrix are upstream/internal estimates, **NOT transferable** to English RoleVow. All three English system support percentages remain **NOT YET EVALUATED**; see [SYSTEM-SUPPORT.md](SYSTEM-SUPPORT.md). "Compatible", "implemented draft", "tested" and "validated" are different states.

## 8. International Negative Price Ultra-Guarantee: inactive

No English-language compensation programme or legally reviewed claims/payout path is active. There is no public offer to pay someone if the game disappoints them. The Italian €1 process, its eligibility, forms and records are **not** RoleVow terms. Do not represent the experimental positioning phrase "the first" as an established priority claim. Any future guarantee needs jurisdiction-specific review, terms, funding/fulfilment, privacy notices and operational tests **before** public advertising or collection.

## 9. Required regression evidence before release

1. URL-only start → exact English Master / Player / Information choices, with no pre-gate overloading.
2. Explicit Play Now → exact six fields, fixed order, one-time screen, defaults and free-text acceptance; no premature system-support notice.
3. After response → first meaningful playable choice, correct 2014 level-1 sheet and user-owned actions; no duplicate onboarding.
4. First Player die → explicit consent, exact source, raw result/modifiers, no fabricated random/tool usage.
5. 2014 combat and rules → action economy, grappling/shoving, natural 1/20, spells/materials/conditions, edition firewall.
6. Progression and closing → XP/milestone contract, no double award, source-owned level changes, player-owned level-up, checkpoint without GM spoilers.
7. Master emergency and published-adventure query → usable help, appropriate source fidelity and no leaked licensed material.
8. Out-of-character questions → fiction paused; no lost time or resources; original decision point preserved.
9. Multi-turn state and V0.4 candidate features → causal integrity, knowledge separation, no false retcon.
10. Privacy/legal/guarantee copy → no active international payout, no private links, correct notices, no unverified superiority claims.

**All release-critical English actual-play tests and independent semantic QA are still OPEN.** Static coverage of files or headings is not a PASS for any gameplay test.

## 10. Risk-ranked deployment gate

**NO-GO** if any mandatory runtime/adapter file is inaccessible, a core safety/ownership invariant is contradicted, an SRD attribution is missing, a real-world privacy flow is undocumented, or a public claim overstates the evidence. Version and release gates A–H must pass on the exact candidate, followed by the owner's **“SÌ, PUBBLICA”** authorization. The public test candidate is not a validated product launch.
