# RoleVow — D&D 5e 2014 / SRD 5.1: Advancement, Equipment, Spell Components and Environment

> **PUBLIC TEST CANDIDATE RC-EN-0.9 — NOT INDEPENDENTLY PLAYTEST VALIDATED.**
> Adapted and rephrased from public Divertoscopio `adapters/5e-srd51/ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md`, source commit `08814049a1d655d7ac31028b28239a67b08fe7cf`, source blob `342278a24a2d22c3a74fa15a1cab67ee373498c4`. Source version, attribution and modifications are documented in parent [`ADAPTER.md`](ADAPTER.md); include the formal SRD 5.1 notice in `../../THIRD-PARTY-NOTICES.md` before release. Compatibility is not official endorsement.

**Activation:** read **on demand**, not during pre-gate onboarding. Use when the character levels up, attempts an optional multiclass or feat, casts a spell with disputed components, handles an identified/attuned magic item, or moves/casts in a mechanically relevant environment. The 2014 source and agreed rules control; do not import 2024 mechanics. This guide is not a replacement for official 2014 rules or commercial books.

## A. Level-up, feats, multiclassing and the player's choices

Follow runtime **V0.3.2 BASE H5/H6/H10/H11** for meaningful-unit closure, progression initialization, player ownership and hit-point advancement. Keep **total character level** separate from the **level in each class**. XP and proficiency bonus generally follow **total level**, while class features, class-level subclass choices, class-based Ability Score Improvements (ASI) and preparation/learning of spells follow the **actual class-level rules**. Set level-up `PENDING` before asking for choices; a newly reached threshold must not silently fill in the player's build.

At an eligible level-up:

1. Reconcile `advancement_mode`, actual XP/milestone trigger, previous character and class levels and any pending choice. Do not treat an adventure's recommended level as automatic permission to level up.
2. Ask whether the player wants to continue in their present class or consider a legally available multiclass **if multiclassing is enabled**, unless they have already delegated or persisted the choice. No automatic same-class assumption.
3. Verify class/subclass unlocks, ASI/feat options, actual spell learning/preparation and other selections against the 2014 source. **Total level ≠ class level.**
4. Apply new Hit Die and HP advancement using a declared and persisted method. When a Constitution modifier changes, check the resulting max-HP adjustment for all relevant Hit Dice/character levels according to the 2014 rule.
5. Update derived proficiency bonus, attack/saving modifiers, spell save DC, slots, current/max resources, armor class and other materially affected fields as relevant. Do not silently skip difficult interactions.
6. Record source and player decisions, then clear pending state; do not duplicate XP, milestone triggers or rewards in the next checkpoint.

**Feats are an optional 2014 rule.** Only when enabled may a player substitute an appropriate class-granted ASI with a qualifying feat. A character with Fighter 3 / Wizard 1 is *total level 4* but has **not** acquired fighter level 4 or wizard level 4 ASI. Check prerequisites, repeatability restrictions, choice and active source; if ASI is chosen, verify permitted distribution and ordinary ability-score maximum 20 unless a rule specifically changes it. **War Caster** does not magically delete verbal/material components or make Silence irrelevant.

**Multiclassing is optional and has entry prerequisites for the existing and the new class.** Check the **actual ability scores**, not ability modifiers; for common 2014 examples Monk needs Dexterity and Wisdom 13, Paladin Strength and Charisma 13, Ranger Dexterity and Wisdom 13, Fighter Strength **or** Dexterity 13. Check other class prerequisites in the official 2014 multiclass table. Gaining a new class uses **multiclass proficiency gains**, not every first-level-class proficiency; do not award new first-level HP as if this were a newly created character. Extra Attack from multiple classes generally does not stack. Alternative Unarmored Defense/AC calculations do not automatically accumulate.

**2014 multiclass spellcasting:** calculate shared spell slots according to the correct 2014 multiclass spellcaster table and actual spellcasting classes. Full spellcasters contribute their levels; Paladin and Ranger contribute half their class levels **rounded down per class**; eligible Fighter/Rogue spellcasting subclasses contribute one third of their class levels **rounded down**, only if that actual subclass exists and has been legally selected. Spells known/prepared remain determined **separately per class**; having a higher shared-level slot can permit upcasting but does not grant earlier knowledge of higher-level spells. Warlock Pact Magic uses the relevant separate slot pool and interaction rules. Verify each class's casting ability, focus and spell source. A commercial-book-only option cannot be synthesized into a purported SRD option.

## B. Inventory provenance, components, casting focus and hands

First apply runtime **H3 INVENTORY PROVENANCE**. An item is usable only if it appears in recorded inventory, a specific previously selected and established starting pack, an actual acquisition, or an explicit recorded correction/ruling. Possible statuses: `CONFIRMED | SOURCE-DEFINED PACK | OPEN/UNRESOLVED | CONSUMED | LOST`. Do not conjure currency, arrows, diamonds, focuses, spell materials or magic items merely because they seem plausible in an adventurer's backpack.

For each cast, inspect only relevant fields: `spell/source/class`, permitted spell level and casting resource, casting time and action/bonus action/reaction, verbal/somatic/material (`V/S/M`), material description, listed cost, whether consumed, legal class focus or component pouch actually possessed, hand occupancy, range/target/line of sight, concentration/duration, and environmental restrictions.

**Material substitution (2014):** a possessed and permitted spellcasting focus or component pouch can ordinarily replace material components **without listed monetary cost and not consumed**; it does **not** replace materials that require a specified cost or are consumed. A component listed as consumed can require the actual quantity even if not priced. Do not invent a missing expensive gem or turn a focus belonging to one class into an all-classes focus. Holy symbols for Cleric/Paladin and instrument focuses for Bard use the relevant class-specific rules; check how an actual symbol must be held, worn or carried. A focus never removes separate `V` or `S` requirements by itself.

**Hands (2014):** a spell with `S` needs a free hand under the relevant rules. For `S+M`, the same hand may handle the focus/material and somatic component; for `S` **without `M`**, merely holding a focus does not by itself satisfy the free-hand requirement. Equipped shield, weapon and other held items occupy real hands. Check any valid War Caster exception only if the character actually has the feat and it covers the situation. Do not assume gear is dropped, stowed or summoned for free without an action-economy check.

**Verbal component:** an appropriate utterance must be possible. The magical **Silence** effect or being unable to speak can prevent `V` under 2014 rules; an ordinary quiet room is not the Silence spell. Whispering does not automatically make verbal magic inaudible while satisfying all conditions. A spell without `V` may remain usable under Silence if its other prerequisites hold.

**Beginner-friendly ≠ free components.** For beginners, do not ask them to name every mundane, already-substitutable ingredient when a legal owned pouch/focus is confirmed. If an abbreviated sheet omitted an item from a **genuinely chosen** initial pack, reconcile and record it transparently. If something has not been owned, offer an actual in-fiction opportunity to obtain it **before casting**, or a clearly agreed house rule for a trivial non-costly/non-consumed edge case; neither silently creates a retroactive possession. A strict table may inspect every slot, hand and consumed component. **Both modes preserve the same actual rules and genuine consequences.**

## C. Magic items and attunement

For a meaningful magic item, track: `item_id`, provenance, verified 2014 source, owner, properties known/unknown, identified state, `requires_attunement`, `attuned_to`, prerequisites, carried/equipped/worn/held state, current/max charges, recharge timing, activation action, associated ability/DC, concentration, consumable amount, and hidden curse/GM-only truth where applicable.

**Possession ≠ identification ≠ attunement ≠ activation.** An item requiring attunement does not grant benefits gated on attunement before the necessary procedure. Ordinarily one creature can be attuned to **no more than three** items unless a specific feature provides an exception. Check the character's class/alignment prerequisites and the precise short-rest attunement rules. A wand or ring does not recharge every turn: use its own source-defined trigger (e.g. dawn), roll and cap. Item-granted spells may have **specific exceptions** for components, spell slots, activation economy or concentration; never apply ordinary class spellcasting costs mechanically where the item says otherwise. `Identify` does not automatically reveal every curse. An evocative description does not upgrade an item to legendary quality or give it unverified powers.

## D. Terrain, swimming, underwater combat and vocal casting

**Difficult terrain, 2014:** moving **1 foot costs 2 feet of movement** under the ordinary rule. Multiple sources of difficult terrain occupying one space do not automatically mean that the cost compounds again. Without a qualifying climbing/swimming speed, climbing or swimming ordinarily imposes extra movement cost; if swimming/climbing also occurs in difficult terrain, use the actual combined 2014 procedure rather than a blanket simplification. Track available movement, operational distances and specific movement modes. Visibility, cover and reach are separate questions. Do not demand an Athletics roll for every few feet of non-hazardous mud unless the circumstances make failure genuinely uncertain and consequential.

**Underwater combat, 2014:** a creature without a swimming speed ordinarily has disadvantage on underwater melee-weapon attacks, **except** with a dagger, javelin, shortsword, spear or trident. A ranged-weapon attack beyond normal range automatically misses. Within normal range, apply the normal underwater disadvantage except for crossbows, nets and weapons thrown like javelins, spears, tridents or darts according to the 2014 text. Creatures and objects immersed in water have resistance to **fire damage**. Do not import different 2024 weapon-category exceptions or treat the 2014 rule as universal across editions. Breathing, drowning/suffocation, swimming speed and environmental hazards are **separate** calculations; do not claim every character can hold their breath for exactly one round.

**Underwater verbal spells:** the 2014 Basic Rules do **not** provide a blanket universal ban on every `V` spell for every character submerged while holding breath. Examine whether the caster can actually speak, any special underwater-breathing capability, the active rules and the likely effect on remaining air. If no precise source controls the edge case, label an explicit provisional ruling. Water is not the magical Silence condition. A spell without `V` may still be legal if its other requirements are met.

**Combined example:** a character swimming underwater with shield and focus attempts a costly `V/S/M` spell and wants to move through submerged wreckage. Resolve separate constraints: edition, spell eligibility/resource, components/actual payment, hands/focus, verbal capability/air, concentration, swim movement and terrain cost, sight/cover, attacks and environmental damage. Do not say “yes to everything” for speed or “no to everything” for atmosphere.

## E. Final just-in-time control — not a user-facing form

`EDITION/CLASS LEVELS → eligible player-owned build choices → actual inventory and sources → V/S/M and occupied hands → environment/movement → action/slots/charges → correct result → persistent state update.`

If a precise rule is unavailable, either consult a legitimate 2014 source or give a transparent **PROVISIONAL** ruling; do not invent certainty. Keep explanations as simple as the player's actual need permits, **without** gifting new possessions or class abilities.

**Official 2014 references:**

- Multiclassing / feats: https://www.dndbeyond.com/sources/dnd/basic-rules-2014/customization-options
- Spellcasting: https://www.dndbeyond.com/sources/dnd/basic-rules-2014/spellcasting
- Combat: https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat
- Adventuring: https://www.dndbeyond.com/sources/dnd/basic-rules-2014/adventuring
- Magic items: https://www.dndbeyond.com/sources/dnd/basic-rules-2014/magic-items
- SRD 5.1 CC BY 4.0: https://media.wizards.com/2023/downloads/dnd/SRD_CC_v5.1.pdf

These are pointers for legitimate use, **not** a license to reproduce non-SRD class options or commercial text. The three RoleVow adapter files still require integrated runtime, first-roll and long-play tests before they are called reliable.
