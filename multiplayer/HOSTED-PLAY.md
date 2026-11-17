# RoleVow — Hosted Multiplayer Contract (ChatGPT single-chat transport)

> **PUBLIC TEST CANDIDATE RC-EN-0.9 — NOT INDEPENDENTLY PLAYTEST VALIDATED.**
> Sources: Divertoscopio `player/PLAYER.md`, `protocols/PROTOCOLS.md` P0-18 and `KNOWN-LIMITATIONS.md` at commit `08814049a1d655d7ac31028b28239a67b08fe7cf`. Feature goal for RoleVow V1: multiple human participants, one human ChatGPT host, separate character ownership and knowledge.

**Owner-approved architecture decision:** RoleVow V1 uses a single human ChatGPT host for the group; synchronized multi-account play is OUT OF SCOPE. See [ADR-001](../docs/ADR-001-HOSTED-TRANSPORT.md) for scope and rationale. This is an architectural decision, **not** evidence of a successful hosted session.

## 1. Honest transport contract

**Hosted / single chat** means ONE human host uses their own ChatGPT conversation. Other humans may be together in person or communicate via call/voice/another channel; the host relays their **attributed** actions and the assistant's player-safe responses. This does NOT mean multiple users can type into one synchronized ChatGPT room, does not create separate private ChatGPT channels, and never requires people to share passwords or accounts. Shared links are not a synchronized multiplayer transport.

The hosted workflow is a PLAYER mode with an AI Game Master. A human GM asking for advice instead follows `master/MASTER.md`. A GM-controlled human table with AI assisting is not the same as AI-GM hosted play.

## 2. Entry and consent (no seventh mandatory Play Now field)

The canonical six-field Play Now screen must offer **Solo** and **Hosted Group** within **field 1 (Play mode)**, retaining the six-field order. If Hosted Group is selected, ask **one concise question only when necessary**: number of participating humans and short non-identifying PC labels/names, or accept an already attributed group message. The group may establish details incrementally. Do not request participants' real names, emails, addresses, ages, account credentials, voice recordings, individual chat exports or personal contact information. An optional table covenant can establish tone/limits, dice preferences, PvP and shared screen practices when relevant; avoid a long mandatory form.

For a new group, state in one sentence that the host can see and relay messages, so genuine player-to-player secrecy requires an independent private channel agreed by the people involved. Never promise confidentiality that the transport cannot provide.

## 3. Stable roster and actor ownership

Maintain `player_id` (non-identifying stable handle), `pc_id`, `pc_name/aliases`, active/absent status, source/system/edition, `PC_KNOWN`, optional `dice_mode` and `dice_source`, and recent spotlight. Bind all meaningful messages and rolls to their actor. Names can be silly; do not change mechanics or invalidate a party name merely because it is a pun.

An aggregated message such as “Moss attacks the guard; Finch checks the window; Rook stays back” is valid and should be split by known actors. Clarify only ambiguity that changes the outcome. The AI must **not** independently choose voluntary actions, dialogue, build options, tactics or emotional reactions for absent/silent PCs. A human may explicitly delegate a narrow action for their PC; record scope and allow revocation.

## 4. Dice and fairness per PC

Apply FIRST PLAYER ROLL CONSENT independently for each participating player/PC, at their first roll that requires a source. For **each PC**, prompt at the roll itself to enter the raw result or say “Roll for me”; a numeric reply is a result, not a menu option. If a preference already exists, do not ask again. Distinguish player dice from GM/adversary dice. The host may relay another player's declared roll without photographs or proof unless the group explicitly adopts a competitive verification covenant.

For group checks, Help, contest, simultaneous tests or Daggerheart Group/Tag Team Actions, use the **active system's procedure**. Do not merge independent rolls mechanically without a real rule. AI-generated dice may only be described as verifiably random if a genuine supported random source was used, with actual provenance.

## 5. Shared Decision Commit Window

When multiple PCs can respond to a material shared situation, make the state readable and accept **one attributed batch** of intents before resolving interacting outcomes. A practical request is “What does each character do? You can send all actions together or one at a time; I'll resolve once the needed intents are clear.”

Do not prematurely resolve the first player's action if the other's simultaneous choice would change risk, target selection, initiative, knowledge or available opportunity. The window is **not** a rigid mandatory turn order or a veto on spontaneous reactions; use it only when interaction matters. If an urgent source-defined trigger interrupts, resolve it as required by that ruleset. If an actor is absent or opts out, do not invent participation to fill the window.

## 6. Spotlight, split party and time

Track `last_meaningful_choice`, branch location, `fiction_time`, resources, open threats and per-PC knowledge. Prefer bringing attention back to a player who has been waiting, without forcing them into an action. When a group divides, preserve separate branches and reconnect through causal events—not by magically teleporting a PC or knowledge. Large parties may have longer real-time waits: compress empty travel and repetitive bookkeeping, but do not skip meaningful consent or mechanics.

## 7. Knowledge and privacy firewall

`PLAYER_VISIBLE`, `PC_KNOWN`, `NPC_BELIEF`, `DM_TRUTH`, `RUMOR` and `INFERENCE` are separate. A fact read aloud to the whole table is not automatically known diegetically by every PC; do not reveal a hidden opponent to the players just because the system tracked them. Conversely, if a player forgot a fact the PC should know, clarify without an arbitrary memory roll.

The host may have access to all participant inputs and visible outputs. A shared screen, shared ChatGPT chat or group relay does not implement per-player secrecy. For private notes, choose a real off-platform channel and explicitly agree what the host may see. **Never upload individual private secrets or logs to a public repository.**

## 8. PvP, disagreements and safety

Before mechanically resolving PC-versus-PC attacks, theft, betrayal or coercive social control when not already agreed, check the table's consent and stakes. Distinguish fictional disagreement from hostility among real people. Any participant may stop, skip, veil, rewind or ask for a brief out-of-character discussion without providing a personal explanation. Do not require a player to disclose sensitive details. The host may pause to address a real conflict; the AI does not impose a ruling about real people's motives or guilt.

## 9. System-specific overlays

- **D&D 5e 2014 / SRD 5.1:** track each PC's initiative, HP, condition/resource state, concentration and independently declared dice; apply real 2014 Help, group checks, contests and action economy.
- **D&D 2024 / SRD 5.2.1:** use the corresponding 2024 adapter and current actions, character schema and revised rules; do not silently reuse 2014 surprise, Hide, Grapple or weapon procedures.
- **Daggerheart / SRD 2.0:** keep Hope, Stress, armor state, Experiences, Duality/action vs reaction rolls and spotlight mechanics separate; Group Action/Tag Team procedures are source-defined, not 5e group checks. Daggerheart is an unofficial experimental adapter, not independently playtest validated.

## 10. Checkpoints and success tests

At a meaningful break, an optional PLAYER-SAFE checkpoint contains the stable roster, class/system/version, separate PC states and knowledge, dice source per PC, shared and branch-specific world state, unresolved decisions, and a concise factual log. Never put unrevealed GM truths into a player checkpoint. Use a separate internal GM state only if the hosting model can keep it private from players; do not pretend hidden chat messages can stay secret from the host.

**Test before public claim:** 2 and 4 humans, three systems, simultaneous declarations, absent PC, mixed dice preferences, split party, PvP consent and knowledge leaks; measure turns to first meaningful choice, fairness, correction burden, fun and Desire to Return. Human-run tabletop tests are not replaced by a static document audit.

## Release boundary

This is a technical implementation specification, not evidence that the hosted mode is already working reliably. The official ChatGPT Group Chat pilot is being retired, so do not promise a multi-account collaborative room. A new communication mechanism requires fresh platform verification before any public claim. A validated product launch requires separate evidence and approval.
