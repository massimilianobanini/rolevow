"""Private deterministic REFERENCE ORACLE for hosted rules and state invariants.

IMPORTANT: This is NOT the RoleVow execution engine and does not run ChatGPT.
Passing tests here proves only reference-state transitions on supplied fixtures,
not LLM compliance, actual-play quality or rule fidelity in all edge cases.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from math import ceil
from typing import Any


class Ruleset(str, Enum):
    DND_2014 = "D&D 5e 2014 / SRD 5.1"
    DND_2024 = "D&D 2024 / SRD 5.2.1"
    DAGGERHEART = "Daggerheart / SRD 2.0"


class DiceMode(str, Enum):
    UNKNOWN = "UNKNOWN"
    HUMAN = "HUMAN"
    AI_AUTHORIZED = "AI_AUTHORIZED"


class ContractViolation(ValueError):
    """The proposed transition violates the hosted contract."""


@dataclass
class Player:
    player_id: str
    pc_id: str
    pc_label: str
    branch: str = "main"
    knowledge: set[str] = field(default_factory=set)
    resources: dict[str, int] = field(default_factory=dict)
    dice_mode: DiceMode = DiceMode.UNKNOWN
    last_roll: int | tuple[int, int] | None = None
    absent: bool = False


@dataclass
class HostedReference:
    """Pure in-memory reference: host acts as sole transport, not secret storage."""
    ruleset: Ruleset
    players: dict[str, Player] = field(default_factory=dict)
    pending_intents: dict[str, str] = field(default_factory=dict)
    chronological_actions: list[dict[str, str]] = field(default_factory=list)
    fictional_time: int = 0
    ooc_paused: bool = False
    gm_truth: set[str] = field(default_factory=set)

    def register(self, player_id: str, pc_id: str, label: str) -> None:
        if not player_id.strip() or not pc_id.strip() or not label.strip():
            raise ContractViolation("A non-identifying stable ID and PC label are required.")
        if player_id in self.players or any(p.pc_id == pc_id for p in self.players.values()):
            raise ContractViolation("Duplicate player_id or pc_id would merge character ownership.")
        self.players[player_id] = Player(player_id, pc_id, label)

    def _require_actor(self, player_id: str) -> Player:
        if player_id not in self.players:
            raise ContractViolation("Action/roll lacks a known owner; request attribution.")
        return self.players[player_id]

    def stage_intent(self, player_id: str, intent: str) -> None:
        actor = self._require_actor(player_id)
        if actor.absent:
            raise ContractViolation("Absent PC cannot be volunteered by the AI.")
        if not intent.strip():
            raise ContractViolation("Missing intent: do not fabricate a player's action.")
        self.pending_intents[player_id] = intent.strip()

    def commit_window(self, expected_participants: set[str]) -> list[dict[str, str]]:
        if self.ooc_paused:
            raise ContractViolation("Out-of-character pause freezes fiction and decisions.")
        if not expected_participants.issubset(self.players):
            raise ContractViolation("Unknown participant in the commit window.")
        if any(self.players[p].absent for p in expected_participants):
            raise ContractViolation("Absent PC cannot commit an action without renewed attribution.")
        missing = expected_participants - set(self.pending_intents)
        if missing:
            raise ContractViolation("Unresolved simultaneous choices: " + ", ".join(sorted(missing)))
        actions = [{"player_id": p, "pc_id": self.players[p].pc_id,
                    "intent": self.pending_intents.pop(p)} for p in sorted(expected_participants)]
        self.chronological_actions.extend(actions)
        return actions

    def roll(self, player_id: str, *, human_roll: int | tuple[int, int] | None = None,
             ai_authorized: bool = False) -> dict[str, Any]:
        actor = self._require_actor(player_id)
        if actor.absent:
            raise ContractViolation("Absent PC cannot make a new roll.")
        if self.ooc_paused:
            raise ContractViolation("A gameplay roll cannot advance an OOC pause.")
        if human_roll is None and not ai_authorized:
            raise ContractViolation("First roll requires actual result or explicit Roll for me consent.")
        if human_roll is not None and ai_authorized:
            raise ContractViolation("Choose one dice source per roll, never both.")
        if ai_authorized:
            actor.dice_mode = DiceMode.AI_AUTHORIZED
            return {"status": "AI_ROLL_AUTHORIZED_BUT_NOT_GENERATED", "player_id": player_id}
        if self.ruleset == Ruleset.DAGGERHEART:
            valid = isinstance(human_roll, tuple) and len(human_roll) == 2 and all(type(v) is int and 1 <= v <= 12 for v in human_roll)
        else:
            valid = type(human_roll) is int and 1 <= human_roll <= 20
        if not valid:
            raise ContractViolation("Roll shape or value not valid for selected ruleset.")
        actor.dice_mode = DiceMode.HUMAN
        actor.last_roll = human_roll
        return {"status": "HUMAN_RESULT_RECORDED", "player_id": player_id, "raw_result": human_roll}

    def reveal_known(self, player_id: str, fact: str) -> None:
        self._require_actor(player_id).knowledge.add(fact)

    def set_explicit_resource(self, player_id: str, key: str, value: int) -> None:
        """Model a recorded, attributed resource update; never invent values."""
        if not key.strip() or type(value) is not int or value < 0:
            raise ContractViolation("Resource name and nonnegative verified value required.")
        self._require_actor(player_id).resources[key] = value

    def split_to(self, player_id: str, branch: str) -> None:
        if not branch.strip():
            raise ContractViolation("Split-party branch is required.")
        self._require_actor(player_id).branch = branch

    def pause_ooc(self) -> None:
        self.ooc_paused = True

    def resume(self) -> None:
        self.ooc_paused = False

    def move_fiction_time(self, minutes: int) -> None:
        if self.ooc_paused or type(minutes) is not int or minutes < 0:
            raise ContractViolation("No time advances during an OOC pause, or backwards.")
        self.fictional_time += minutes

    def authorize_pvp(self, attacker_id: str, defender_id: str, consenting: set[str]) -> bool:
        self._require_actor(attacker_id)
        self._require_actor(defender_id)
        if not {attacker_id, defender_id}.issubset(consenting):
            raise ContractViolation("PvP requires explicit table consent in scope.")
        return True

    def safe_checkpoint(self) -> dict[str, Any]:
        """Player-facing facts only, no GM truths; host remains able to see output."""
        return {"ruleset": self.ruleset.value, "hosted": True, "single_chat": True,
                "fictional_time": self.fictional_time,
                "players": [{"player_id": p.player_id, "pc_id": p.pc_id,
                             "pc_label": p.pc_label, "branch": p.branch,
                             "PC_KNOWN": sorted(p.knowledge), "dice_mode": p.dice_mode.value,
                             "resources": dict(p.resources)}
                            for p in self.players.values()],
                "pending_attributed_intents": dict(self.pending_intents),
                "visibility_warning": "Host can see the shared conversation; no per-player private channel."}


def dnd2024_grapple_dc(strength_modifier: int, proficiency_bonus: int) -> int:
    return 8 + strength_modifier + proficiency_bonus


def half_caster_slot_index(levels: list[int], *, ruleset: Ruleset) -> int:
    if any(type(level) is not int or not 1 <= level <= 20 for level in levels) or sum(levels) > 20:
        raise ContractViolation("Invalid class levels for the reference calculation.")
    if ruleset == Ruleset.DND_2014:
        return sum(level // 2 for level in levels)
    if ruleset == Ruleset.DND_2024:
        return sum(ceil(level / 2) for level in levels)
    raise ContractViolation("Daggerheart has no D&D spell-slot multiclass procedure.")


def dnd2014_ordinary_check(d20: int, bonus: int, dc: int) -> bool:
    if type(d20) is not int or not (1 <= d20 <= 20):
        raise ContractViolation("Invalid d20 result.")
    return d20 + bonus >= dc  # Natural 1/20 are NOT universally automatic on 2014 checks.


def daggerheart_duality(hope_die: int, fear_die: int, modifier: int, difficulty: int,
                         *, roll_type: str = "ACTION") -> dict[str, Any]:
    if type(hope_die) is not int or type(fear_die) is not int or not (1 <= hope_die <= 12 and 1 <= fear_die <= 12):
        raise ContractViolation("Each Duality die must be d12, 1..12.")
    if roll_type not in {"ACTION", "REACTION"}:
        raise ContractViolation("Use a separate source-defined procedure for Group/Tag Team rolls.")
    critical = hope_die == fear_die
    total = hope_die + fear_die + modifier
    success = critical or total >= difficulty
    tag = "CRITICAL_SUCCESS" if critical else ("HOPE" if hope_die > fear_die else "FEAR")
    return {"total": total, "success": success, "tag": tag,
            "generates_action_roll_resources": roll_type == "ACTION",
            "roll_type": roll_type}
