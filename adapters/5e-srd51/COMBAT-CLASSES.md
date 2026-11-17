# RoleVow — 2014 5e Combat, Class Features, Action Economy and Status Gate

> **PUBLIC TEST CANDIDATE RC-EN-0.9 — NOT INDEPENDENTLY PLAYTEST VALIDATED.**
> English adaptation of the public Divertoscopio `adapters/5e-srd51/COMBAT-CLASSES.md` at commit `08814049a1d655d7ac31028b28239a67b08fe7cf`, source blob `de755d9b67c376f169857e1d67f987d927c35251`. Material rearranged and rephrased; see parent [`ADAPTER.md`](ADAPTER.md) and the future `../../THIRD-PARTY-NOTICES.md` for SRD 5.1 CC BY 4.0 attribution and change notice. No official endorsement is implied.

## Activation: only when mechanically relevant

This is a **just-in-time** reference for a real class feature, disputed action, complex battle, condition or post-level-up state. It is **not** an onboarding checklist, not a replacement for a legally available 2014 rule source, and not an invitation to load every class feature. If a rule cannot be sourced, give the Game Master a clearly provisional ruling instead of inventing a published rule.

Before applying a class feature, internally verify: `active_system = 2014/SRD5.1`, exact class levels, actually selected subclass/feats, equipment, Action/Bonus Action/Reaction already used, attacks permitted by the Attack action, movement already spent, conditions and expiration timing, concentration, current limited resources and their recovery conditions. Explain to beginners only what they need now.

## 2014 action economy and universal combat actions

Common 2014 action options include **Attack, Dash, Disengage, Dodge, Help, Hide, Ready, Search, Use an Object** and actions permitted by specific rules. Do not conflate a general 2014 action with a named class feature or 2024 procedure.

- **Action:** ordinarily one action on your turn. A rule such as Action Surge may grant another, but does not automatically grant another bonus action or reaction.
- **Bonus action:** only if the character has a feature/spell/rule allowing it; ordinarily at most one bonus action in the same turn. Never spend the same bonus action on two features.
- **Reaction:** ordinarily one available until the start of the character's next turn, including on other creatures' turns. An opportunity attack, a readied action and a reaction feature can compete for that same resource. Check trigger, timing and range.
- **Dodge:** ordinarily consumes the action; under the 2014 rule it affects attacks by visible attackers and Dexterity saves as specified, and its benefits end if the dodging creature is incapacitated or its speed becomes 0. It is not a free defensive stance.
- **Ready:** spend the action now to prepare a specified response, and normally the reaction to perform it on the trigger; a readied spell has special casting, slot and concentration requirements. Do not hold an arbitrary spell without cost.
- **Extra Attack:** works with the **Attack action** according to actual feature level, not automatically with reaction attacks, spellcasting, opportunity attacks or unrelated attack triggers.
- **Movement/object interactions:** track separately from actions, including legal reach, distance, obstruction and equipped items.

## Grappling and shoving — 2014 only

A grapple or shove is a **special melee attack** replacing **one attack** within the Attack action, not automatically the whole Attack action where Extra Attack applies. Target must be in reach and no more than one size larger; grappling also requires a free hand. The attacker uses Strength (Athletics) against the defender's choice of Strength (Athletics) or Dexterity (Acrobatics). Apply the **actual 2014 errata** for special cases, including incapacitated targets, where verified. The 2014 shove can knock the target prone or push it **5 feet**.

**Grappled ≠ Restrained.** Grappled normally reduces speed to 0 (with additional effects subject to rules), but does not independently impose the restrained condition, paralysis, generic disadvantage on attacks, or advantage for all attacks against the target. Escaping normally costs an action and follows the appropriate contested procedure; release of a grapple normally requires no action. **Do not use 2024 grapple initiation saving throws** in a 2014 encounter. Ask whether “trip” means the universal 2014 shove-to-prone option or a *real subclass maneuver* already owned by the PC; they are not interchangeable.

## Class-specific high-risk gates — use only if feature is actually owned

**Fighter:** Second Wind uses a bonus action and a limited resource. Action Surge is not available at fighter level 1 (it begins at class level 2). Special maneuvers with superiority dice require an actual relevant subclass/feature; do not assign Battle Master options to every fighter. If the table uses PHB-only maneuvers, look up the specific legitimately available feature; do not fabricate damage dice, superiority costs or save DCs from the name.

**Monk:** 2014 Martial Arts can grant a bonus-action unarmed strike under its actual prerequisites. Ki starts at monk level 2. Flurry of Blows, Patient Defense and Step of the Wind require their actual Ki costs and bonus action; the character cannot combine incompatible bonus-action options in the same turn. Stunning Strike has its own higher-level requirement, hit trigger, Ki cost, saving throw and effect timing. **Do not import 2024 Focus** mechanics.

**Rogue:** Sneak Attack is generally limited to **once per turn**, not once per round, and its equipment/position conditions must hold. An appropriate reaction attack on another creature's turn can be eligible if the prerequisites are met. Cunning Action starts at rogue level 2 and uses the character's bonus action. Sneak Attack does not grant a free extra Attack action.

**Paladin:** 2014 Divine Smite starts at paladin level 2, follows the qualifying melee-weapon-hit/slot rule and is not itself an added bonus action under the 2014 procedure. **Do not import the revised 2024 bonus-action spell model.**

**Other classes, only as needed:** Barbarian (Rage), Bard (Bardic Inspiration), Cleric (Channel Divinity), Druid (Wild Shape), Ranger (actual 2014 class spells/features), Sorcerer (Metamagic), Warlock (Pact Magic/Invocations), Wizard (Arcane Recovery/spellcasting), etc. For each feature verify actual class and level, subclass/choice, source, prerequisite, action cost, remaining use, recovery timing, duration/concentration and interaction with existing resources. Do not assume that weapon proficiency grants 2024 Weapon Mastery.

## Conditions — effect-by-effect, not label shortcuts

Track each effect as `target / condition / source / applied_at / expires_or_save_trigger / active` and update at the correct timing. Do not stack duplicate effects as if they multiplied their disadvantages.

- **Poisoned:** disadvantage on attack rolls and ability checks under the 2014 condition, **not** automatically on every saving throw.
- **Prone:** standing and movement costs and attack advantage/disadvantage depend on the relevant distance and the actual 2014 rule; a ranged attack from far away is not the same as a melee attack from within 5 feet.
- **Grappled:** speed 0; other actions are not automatically prohibited.
- **Restrained:** additional movement, attack and Dexterity-save consequences beyond grappled; do not substitute the conditions for one another.
- **Stunned:** incapacitates, prevents movement, fails specified Strength/Dexterity saves and gives attackers advantage, **but not** an automatic critical hit from being stunned alone.
- **Paralyzed:** adds specific automatic critical-hit consequences **if an attack hits from within 5 feet**, subject to the actual rule. Do not apply those automatically to every attack regardless of range.
- **Unconscious:** separately check prone, awareness, saving throws and attack distance/critical-hit rules. Do not collapse unconscious into stunned.
- **Incapacitated:** prohibits actions and reactions; follow 2014 bonus-action restrictions where an action is unavailable. Check concentration loss and effect expiration by rule.

For all other conditions and immunities, consult the relevant official 2014 appendix; do not extrapolate from the names.

## End-of-turn and round state audit

When it matters, reconcile Action, Bonus Action, Reaction, movement, Ki/superiority dice/charges/spell slots, attack/damage results, conditions applied/removed, saves occurring at the prescribed time, concentration and ongoing effect durations. A reaction may change outside the PC's own turn. Keep the accounting in internal state; show only facts that impact player choice or explain a correction. Do not retroactively create a resource just to help an action succeed.

## Official references and limits

- 2014 combat: https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat
- 2014 conditions: https://www.dndbeyond.com/sources/dnd/basic-rules-2014/appendix-a-conditions
- 2014 classes: https://www.dndbeyond.com/sources/dnd/basic-rules-2014/classes
- SRD 5.1 CC BY 4.0: https://media.wizards.com/2023/downloads/dnd/SRD_CC_v5.1.pdf

Access to online rules does not mean every subclass, named maneuver, commercial adventure or proprietary stat block can be republished under SRD 5.1. **English actual-play status: not tested.** The 2014 source, agreed house rules and documented errata control exact mechanics.
