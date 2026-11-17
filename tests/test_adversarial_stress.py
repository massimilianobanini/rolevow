"""Deterministic adversarial stress tests; no actual LLM, financial service, or payout."""
import random
import unittest
from guarantee.manual_gate import decide
from tests.reference_hosted_oracle import (HostedReference, Ruleset, ContractViolation,
    dnd2014_ordinary_check, daggerheart_duality, half_caster_slot_index)
from tests.actual_play_evidence_gate import count_verified_actual_play
from tests.test_evidence_gate import passing

class StressTests(unittest.TestCase):
    def test_absence_after_staging(self):
        s=HostedReference(Ruleset.DND_2014);s.register('p','pc','PC')
        s.stage_intent('p','Investigate');s.players['p'].absent=True
        with self.assertRaises(ContractViolation):s.commit_window({'p'})
        self.assertEqual(s.chronological_actions,[])
        with self.assertRaises(ContractViolation):s.roll('p',human_roll=10)

    def test_invalid_dice_and_state_numbers(self):
        s=HostedReference(Ruleset.DND_2014)
        for v in (True, 1.5, -1):
            with self.subTest(v=v),self.assertRaises(ContractViolation):s.move_fiction_time(v)
        for v in (True, 5.5, 0, 21):
            with self.subTest(v=v),self.assertRaises(ContractViolation):dnd2014_ordinary_check(v,0,10)
        for v in (True, 5.5, 0, 13):
            with self.subTest(v=v),self.assertRaises(ContractViolation):daggerheart_duality(v,4,0,10)
        for v in (True, 5.5, 0, 21):
            with self.subTest(v=v),self.assertRaises(ContractViolation):half_caster_slot_index([v],ruleset=Ruleset.DND_2024)

    def test_evidence_malformed_fields_fail_closed(self):
        for field,value in [('candidate_sha256','x'),('source_files','BOOTSTRAP.md'),('user_input',' '),('reviewer',{}),('source_files',[None])]:
            with self.subTest(field=field):
                x=passing();x[2][field]=value
                count,errors=count_verified_actual_play(x)
                self.assertEqual(count,0);self.assertTrue(errors)
        x=passing('T20');x[-1]['human_participants']='2'
        self.assertEqual(count_verified_actual_play(x)[0],0)
        self.assertTrue(count_verified_actual_play([None,{'id':[]}])[1])

    def test_financial_invariants_50000_randomized(self):
        rng=random.Random(20261117)
        for _ in range(50000):
            action=rng.choice(('RESERVE','PAY'));paid=rng.randrange(10501);binding=rng.randrange(3001)
            month=rng.randrange(2201);net=rng.choice((99,100,101));gross=rng.randrange(2201);reserve=rng.randrange(2201)
            eligibility,route,duplicate,earlier,intake,quote=(rng.random()<p for p in (.9,.9,.1,.1,.8,.9))
            result=decide(action,paid,binding,month,net,gross,reserve,eligibility,route,duplicate,earlier,intake,quote)
            if result in ('RESERVE_NOW','RESERVE_QUEUE','PAY_READY'):
                self.assertTrue(eligibility and route and quote and not duplicate and not earlier)
                self.assertEqual(net,100);self.assertTrue(100<=gross<=2000)
                self.assertLessEqual(paid+binding,10000);self.assertLessEqual(month,2000)
                if action=='RESERVE':
                    self.assertTrue(intake);self.assertLessEqual(paid+binding+gross,10000)
                    self.assertEqual(result,'RESERVE_NOW' if month+gross<=2000 else 'RESERVE_QUEUE')
                else:
                    self.assertTrue(gross<=reserve<=binding);self.assertLessEqual(month+gross,2000)
                    self.assertLessEqual(paid+gross+binding-reserve,10000)
            if duplicate:self.assertNotIn(result,('RESERVE_NOW','RESERVE_QUEUE','PAY_READY'))
            if action=='RESERVE' and not intake:self.assertNotIn(result,('RESERVE_NOW','RESERVE_QUEUE'))

    def test_hosted_2403_windows_no_owner_swap(self):
        rng=random.Random(20261117)
        for ruleset in Ruleset:
            for size in (2,4,8):
                for _ in range(267):
                    s=HostedReference(ruleset);people=[f'p{i}' for i in range(size)]
                    for p in people:s.register(p,'pc-'+p,p)
                    rng.shuffle(people)
                    for p in people:s.stage_intent(p,'intent-'+p)
                    got=s.commit_window(set(people))
                    self.assertEqual({(a['player_id'],a['pc_id'],a['intent']) for a in got},
                                     {(p,'pc-'+p,'intent-'+p) for p in people})
                    self.assertFalse(s.pending_intents)

    def test_duality_144_pairs_3_difficulties_2_roll_types(self):
        for h in range(1,13):
            for f in range(1,13):
                for dc in (6,14,24):
                    for roll_type in ('ACTION','REACTION'):
                        r=daggerheart_duality(h,f,0,dc,roll_type=roll_type)
                        self.assertEqual(r['success'],h==f or h+f>=dc)
                        self.assertEqual(r['generates_action_roll_resources'],roll_type=='ACTION')
                        self.assertEqual(r['tag'],'CRITICAL_SUCCESS' if h==f else ('HOPE' if h>f else 'FEAR'))
