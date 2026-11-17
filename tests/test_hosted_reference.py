"""Deterministic hosted-transport and three-ruleset FIXTURES, not actual play."""
from __future__ import annotations
import json
from pathlib import Path
import unittest
from tests.reference_hosted_oracle import (
    HostedReference, Ruleset, DiceMode, ContractViolation,
    dnd2024_grapple_dc, dnd2014_ordinary_check, half_caster_slot_index,
    daggerheart_duality)


class HostedFixtureTests(unittest.TestCase):
    def setUp(self):
        self.s = HostedReference(Ruleset.DND_2024)
        self.s.register("hosted_1", "Moss", "Moss")
        self.s.register("hosted_2", "Finch", "Finch")

    def test_H01_actor_attribution_not_one_character(self):
        self.s.stage_intent("hosted_1", "Attack the guard")
        self.s.stage_intent("hosted_2", "Inspect the window")
        actions = self.s.commit_window({"hosted_1", "hosted_2"})
        self.assertEqual({a['pc_id'] for a in actions}, {"Moss", "Finch"})

    def test_H02_unidentified_actor_not_invented(self):
        with self.assertRaises(ContractViolation):self.s.stage_intent("unknown", "Attack")

    def test_H03_absent_pc_never_acts_by_default(self):
        self.s.players["hosted_2"].absent = True
        with self.assertRaises(ContractViolation):self.s.stage_intent("hosted_2", "The AI attacks")

    def test_H04_commit_waits_for_interacting_second_actor(self):
        self.s.stage_intent("hosted_1", "Pull lever")
        with self.assertRaises(ContractViolation):self.s.commit_window({"hosted_1", "hosted_2"})
        self.assertEqual(len(self.s.chronological_actions),0)
        self.assertEqual(self.s.pending_intents["hosted_1"],"Pull lever")

    def test_H05_independent_first_roll_consent(self):
        self.s.roll("hosted_1", human_roll=14)
        self.assertEqual(self.s.players["hosted_1"].dice_mode,DiceMode.HUMAN)
        self.assertEqual(self.s.players["hosted_2"].dice_mode,DiceMode.UNKNOWN)
        with self.assertRaises(ContractViolation):self.s.roll("hosted_2")

    def test_H06_roll_for_me_consent_is_not_a_fabricated_die(self):
        r=self.s.roll("hosted_1",ai_authorized=True)
        self.assertEqual(r["status"],"AI_ROLL_AUTHORIZED_BUT_NOT_GENERATED")
        self.assertIsNone(self.s.players["hosted_1"].last_roll)

    def test_H07_numbers_are_dice_results_not_menu_numbers(self):
        r=self.s.roll("hosted_1",human_roll=1)
        self.assertEqual(r["raw_result"],1)

    def test_H08_split_branches_no_knowledge_merge(self):
        self.s.split_to("hosted_1","cellar")
        self.s.split_to("hosted_2","tower")
        self.s.reveal_known("hosted_1","A door under the cellar stairs")
        self.assertNotIn("A door under the cellar stairs",self.s.players["hosted_2"].knowledge)

    def test_H09_player_checkpoint_does_not_serialize_gm_truth(self):
        self.s.gm_truth.add("The innkeeper is the villain")
        out=json.dumps(self.s.safe_checkpoint())
        self.assertNotIn("innkeeper",out)
        self.assertIn("no per-player private channel",out)

    def test_H10_ooc_pause_preserves_fictional_time(self):
        self.s.move_fiction_time(10)
        self.s.pause_ooc()
        with self.assertRaises(ContractViolation):self.s.move_fiction_time(1)
        with self.assertRaises(ContractViolation):self.s.commit_window(set())
        self.assertEqual(self.s.fictional_time,10)

    def test_H11_pvp_requires_both_consents(self):
        with self.assertRaises(ContractViolation):self.s.authorize_pvp("hosted_1","hosted_2",{"hosted_1"})
        self.assertTrue(self.s.authorize_pvp("hosted_1","hosted_2",{"hosted_1","hosted_2"}))

    def test_H12_roster_rejects_pc_alias_collapse(self):
        with self.assertRaises(ContractViolation):self.s.register("hosted_3","Finch","Other")

    def test_H13_hosted_4_people_independent(self):
        for i in range(3,5):self.s.register(f"hosted_{i}",f"PC_{i}",f"PC_{i}")
        self.assertEqual(len(self.s.safe_checkpoint()["players"]),4)
        self.assertEqual(len({p['pc_id'] for p in self.s.safe_checkpoint()["players"]}),4)

    def test_H14_2014_natural20_ordinary_check_can_fail(self):
        self.assertFalse(dnd2014_ordinary_check(20,0,25))

    def test_H15_2014_natural1_ordinary_check_can_succeed(self):
        self.assertTrue(dnd2014_ordinary_check(1,12,12))

    def test_H16_2014_multiclass_slot_rounds_each_class_down(self):
        self.assertEqual(half_caster_slot_index([3,2],ruleset=Ruleset.DND_2014),2)

    def test_H17_2024_multiclass_slot_rounds_each_class_up(self):
        self.assertEqual(half_caster_slot_index([3,2],ruleset=Ruleset.DND_2024),3)

    def test_H18_2024_grapple_str_save_formula(self):
        self.assertEqual(dnd2024_grapple_dc(3,2),13)

    def test_H19_daggerheart_hope_8_fear_5_without_mod_is_not_auto_success(self):
        r=daggerheart_duality(8,5,0,14)
        self.assertFalse(r['success']);self.assertEqual(r['tag'],"HOPE")

    def test_H20_daggerheart_action_vs_reaction_resources(self):
        a=daggerheart_duality(8,5,1,14,roll_type="ACTION")
        b=daggerheart_duality(8,5,1,14,roll_type="REACTION")
        self.assertTrue(a['success']);self.assertTrue(a['generates_action_roll_resources'])
        self.assertFalse(b['generates_action_roll_resources'])

    def test_H21_daggerheart_dual_tie_critical(self):
        self.assertEqual(daggerheart_duality(8,8,0,30)["tag"],"CRITICAL_SUCCESS")

    def test_H22_daggerheart_dice_mode_is_dual_not_single_d20(self):
        s=HostedReference(Ruleset.DAGGERHEART)
        s.register("p","pc","PC")
        with self.assertRaises(ContractViolation):s.roll("p",human_roll=16)
        self.assertEqual(s.roll("p",human_roll=(8,5))["raw_result"],(8,5))

    def test_H24_resource_state_kept_separate_per_pc_in_checkpoint(self):
        self.s.set_explicit_resource('hosted_1','HP',7)
        self.s.set_explicit_resource('hosted_2','HP',12)
        p={p['pc_id']:p for p in self.s.safe_checkpoint()['players']}
        self.assertEqual(p['Moss']['resources']['HP'],7)
        self.assertEqual(p['Finch']['resources']['HP'],12)
        self.assertNotEqual(p['Moss']['resources'],p['Finch']['resources'])

    def test_H25_resource_cannot_be_silently_negative(self):
        with self.assertRaises(ContractViolation):self.s.set_explicit_resource('hosted_1','HP',-1)
        self.assertFalse(self.s.players['hosted_1'].resources)

    def test_H26_batch_order_never_switches_ownership(self):
        import random
        rng=random.Random(20261115)
        for party_size in (2,3,4):
            for _ in range(80):
                s=HostedReference(Ruleset.DND_2014)
                people=[f'p{i}' for i in range(party_size)]
                for i,p in enumerate(people):s.register(p,f'PC{i}',f'Character {i}')
                order=list(people); rng.shuffle(order)
                for p in order:s.stage_intent(p,f'Intent from {p}')
                out=s.commit_window(set(people))
                self.assertEqual(len(out),party_size)
                self.assertEqual({(x['player_id'],x['intent']) for x in out},
                                 {(p,f'Intent from {p}') for p in people})

    def test_H23_2014_grapple_refuses_daggerheart(self):
        with self.assertRaises(ContractViolation):half_caster_slot_index([3],ruleset=Ruleset.DAGGERHEART)


if __name__=='__main__':unittest.main()
