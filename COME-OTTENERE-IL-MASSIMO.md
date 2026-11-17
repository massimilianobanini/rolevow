# Get the Most Out of RoleVow

> **PUBLIC TEST CANDIDATE RC-EN-0.9 — NOT INDEPENDENTLY PLAYTEST VALIDATED.**
> Source: Divertoscopio `COME-OTTENERE-IL-MASSIMO.md` at commit `08814049a1d655d7ac31028b28239a67b08fe7cf`, source Git blob `0af45c94582bdb01335d041e93771ef6771519dd`. Adapted for RoleVow's three-system English scope and hosted multiplayer. This is an optional user guide, not a replacement for BOOTSTRAP/CORE/PLAYER or an active guarantee.

**You do not need to study this guide to start.** RoleVow is an AI-assisted companion for existing tabletop RPGs. The source is available for controlled technical playtests, not a validated public launch. No financial compensation programme is active.

The objective is **less friction on the way to an enjoyable session, without taking over what you like doing yourself**. These are optional practices, not prerequisites or guarantees of improvement.

## Three levels of involvement

| Level | What it means | When useful |
|---|---|---|
| 1 — Play Now | A short six-field screen, then the first meaningful fictional decision | You want to play quickly or have a simple Game Master question |
| 2 — Customize | State a few preferences, especially what you want to control | You have a preferred tone, system, risk level or creative role |
| 3 — Preserve a campaign | Keep versioned checkpoints and, if helpful, external TXT/Markdown files | You play across sessions or different chats |

The source framework uses roughly 1 minute, 5 minutes and 15+ minutes as **setup design targets**, not measured or guaranteed response times. You can change preferences during play without restarting the whole campaign.

## 1. Start without needless setup

**For a player, after an approved public release:** open ChatGPT and provide the official RoleVow repository URL `https://github.com/massimilianobanini/rolevow`, then write **Let's begin.** When the files are readable, choose **I'm a Player → Play Now**. The six fields are play mode, system, setting, tabletop RPG experience, tone and risk, in that order. Reply to as many as you wish or say **Choose everything for me**. The first default is D&D 5e 2014, not the only supported system: English V1 is intended also to cover D&D 2024 and the unofficial experimental Daggerheart adapter, subject to the same unpublished release checks as other source-dependent content. You can use natural language to describe what your character does; menu suggestions never restrict your choices.

**For a Game Master, after release:** describe a concrete problem rather than requesting a whole campaign unless that is what you want. Example: “I'm a Game Master. My players may get stuck in an investigation tonight. Ask only for details you need, then offer two or three rescue approaches that do not rewrite my prepared mystery.” You keep final authority over fiction, house rules and what you enjoy preparing. Use FAST LIVE for concise in-session assistance.

For a controlled test, use the repository URL and start command from README. Retrieval and gameplay quality are not guaranteed.

## 2. State what you want — and what you do not delegate

A few preferences are enough; do not turn onboarding into a survey. Useful categories are: ruleset and edition, beginner/expert guidance, atmosphere, stakes and character death, pacing, player agency, dice ownership, topics to avoid, and what creative preparation the human Game Master wishes to keep. For a group, say **Hosted Group** and distinguish each human participant's decisions.

**Player example:** “D&D 2024, mystery and dangerous combat, no unsolicited puzzle answers. I roll physical dice and report their raw results. I decide my character's actions and feelings.”

**Game Master example:** “I create my own maps and villains. Only check my session for contradictions, likely dead ends and usable alternatives. Don't invent established module facts.”

Do not ask for personal identifiers, sensitive details or private transcripts as part of basic setup. Limits can be communicated briefly and changed without explanation. PvP and real-person safety boundaries deserve explicit table consent.

## 3. Fast replies versus more reasoning

Use normal ChatGPT settings for routine starts and simple actions. If your account offers more reasoning effort, it may help with complex multi-class rule questions, large NPC/state lists, or deep preparation—but it can also slow down responses and does not guarantee correct rules or flawless memory. When momentum matters, prefer a short actionable ruling followed by the source and fuller explanation on request. Do not require a specific paid plan or model to begin.

## 4. Keep a gameplay checkpoint

Long conversations can lose state. Ask for a reusable, versioned **PLAYER-SAFE GAME MEMORY** at the end of a session or significant chapter, before a long break or after extensive context; not after each die roll. Record:

- active system, edition, source version, optional rules and house rules;
- player/PC roster (anonymous handles are fine), each character's resources, statuses, advancement, inventory and **dice source**;
- location, fictional time, open dangers, goals, the next playable situation, and unresolved decisions;
- NPCs met, relationships, verified events, clues actually known and consequential choices;
- per-PC knowledge for a split party (do not merge all player/PC knowledge);
- uncertainty, missing evidence and source attribution rather than invented continuity;
- checkpoint version/date and a precise resume point.

Example instruction:

> We've finished the session. Create PLAYER-SAFE GAME MEMORY V0.1 as Markdown for our next chat. Distinguish verified events, hypotheses and unknowns. Include only information these players/characters are allowed to know. Do not reveal hidden Game Master truth or assume a roll/payout occurred.

At the next session: supply the checkpoint and ask RoleVow to reconcile the system/edition, characters, inventory, conditions, dice choices and last scene before play. A summary can still omit facts; keep more detailed notes for long or consequential campaigns. There is no demonstrated general superiority over ChatGPT plus a carefully maintained text file.

## 5. Separate players' notes from Game Master secrets

| Information store | Contents | Appropriate access |
|---|---|---|
| **PLAYER-SAFE MEMORY** | Visible events, PC knowledge, inventory, known relationships, party decisions | Players and the assistant in a suitable player session |
| **PRIVATE GAME MASTER NOTES** | Unsolved mystery answers, hidden NPC agendas, secret stat blocks, unrevealed future events | Human GM and contexts they explicitly authorize |

A different folder name is **not a security boundary**. If the player-facing assistant can read the GM's private notes, a “no spoilers” instruction cannot technically prevent disclosure. Restrict access to the actual files and connectors; inspect sharing permissions; keep separate contexts if necessary. In a hosted group, the host may see everything typed into that one ChatGPT conversation. RoleVow does not create private player subchannels or a multi-account synchronized room. Use an agreed independent private channel for secrets when needed, and never claim to provide secrecy that the transport cannot enforce.

Do not upload other players' sensitive information or full commercial books without a lawful basis and relevant permissions.

## 6. External files and Google Drive are optional

You can save checkpoints as TXT or Markdown on your own device and paste or re-upload them later. A connected Google Drive can be useful when your account has permitted access, but **connection does not imply automatic updates**. Verify reading and writing permissions; ask for a proposed change and confirmation before overwriting an important state file; verify its destination/version after writing. If the assistant cannot write, use the Markdown it gives you and save it manually.

An optional directory:

- `01-PREFERENCES.md` — tone, ruleset, character ownership, limits, dice preferences;
- `02-PLAYER-SAFE-MEMORY.md` — only information shareable with participants;
- `03-CHRONOLOGY.md` — dated events and corrections;
- `04-PRIVATE-GM-NOTES.md` — only if genuinely restricted from player-facing contexts.

For split parties, store each PC's knowledge separately when needed. The filenames are examples, **not files that RoleVow creates by itself**. Do not assume a later conversation has access to the newest version until you check.

## 7. Images, maps, music and other tools

Default to text for speed and continuity. Ask for maps or illustrations when they materially improve your table's experience, and only if the platform and the rights allow it. Generating media can introduce delay or spoilers and must not silently create new canon. A map is a reference until the current game rules and table actually give it mechanical authority. There is no verified live AI-to-VTT sync for token positions, hit points or conditions.

## 8. Reduce interruptions

Notification controls, a focused window and fewer unnecessary media requests may help keep a session moving. Browser extensions are optional, can have side effects, and are not a RoleVow requirement. ChatGPT's own interface and usage restrictions are outside RoleVow's control. Do not spend more time setting up distractions countermeasures than you would save during play.

## 9. Recover from a mistake

- **Wrong rule:** confirm system, edition, source and scope; mark uncertain rulings as provisional rather than inventing RAW.
- **Forgotten state:** supply the last checkpoint and make the minimal transparent correction.
- **Spoiler or private data leak:** pause and separate the actual information access before proceeding.
- **AI takes over your PC:** reassert character ownership; restore the last unresolved human decision.
- **Slow pacing:** stop optional media/encyclopedic detail and request only what matters now.
- **Ruleset contamination:** do not import 2014 Grapple/Surprise/Hide into 2024 or D&D action economy into Daggerheart.
- **Different preferences:** revise the table contract without silently retroactively changing old outcomes.

For active system support evidence, see [SYSTEM-SUPPORT.md](SYSTEM-SUPPORT.md), and for release limitations see [KNOWN-LIMITATIONS.md](KNOWN-LIMITATIONS.md).

## Final rule

**Getting the most out of RoleVow is not maximizing the amount of AI you use.** It is getting useful assistance without losing your own play, creativity, choices and control. This optional guide does not change rules, activate any compensation scheme, or claim that the unreleased English tool has already been validated.
