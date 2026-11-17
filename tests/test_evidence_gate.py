"""Evidence gates must never transform simulations into actual-play successes."""
import json
from pathlib import Path
import unittest
from tests.actual_play_evidence_gate import CASE_IDS,count_verified_actual_play
ROOT=Path(__file__).resolve().parents[1]


def placeholder():
    return [dict(id=i,status='NOT_RUN',mode='not_executed',reviewer_verdict='NOT_RUN') for i in CASE_IDS]


def passing(id='T03'):
    x=placeholder()
    x[int(id[-2:])-1]={
        'id':id,'status':'PASS','mode':'independent_fresh_chat',
        'candidate_sha256':'verified_sha_512','source_files':['BOOTSTRAP.md'],
        'user_input':'English case prompt','assistant_output':'Observed English actual output',
        'reviewer':'human independent reviewer','reviewer_verdict':'PASS',
        'privacy_reviewed':True,'human_participants':2,'participant_consent':True,
    }
    return x


class EvidenceGateTests(unittest.TestCase):
    def test_E01_real_template_starts_at_zero(self):
        records=placeholder()
        self.assertEqual(count_verified_actual_play(records),(0,[]))

    def test_E02_reference_model_is_not_a_fresh_chat(self):
        x=passing(); x[2]['mode']='deterministic_reference_oracle'
        count,errors=count_verified_actual_play(x)
        self.assertEqual(count,0);self.assertTrue(errors)

    def test_E03_missing_output_is_not_pass(self):
        x=passing(); x[2]['assistant_output']=''
        count,errors=count_verified_actual_play(x)
        self.assertEqual(count,0);self.assertTrue(errors)

    def test_E04_t20_without_humans_is_not_pass(self):
        x=passing('T20'); x[-1]['human_participants']=0
        count,errors=count_verified_actual_play(x)
        self.assertEqual(count,0);self.assertTrue(errors)

    def test_E05_one_valid_human_reviewed_case_can_count(self):
        count,errors=count_verified_actual_play(passing())
        self.assertEqual((count,errors),(1,[]))

    def test_E06_duplicate_ids_rejected(self):
        x=placeholder();x[1]['id']='T01'
        count,errors=count_verified_actual_play(x)
        self.assertEqual(count,0);self.assertTrue(errors)


if __name__=='__main__':unittest.main()
