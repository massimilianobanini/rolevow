"""Extra deterministic contract cases for RC-EN-0.5.

Important: these are independent arithmetic examples and textual presence checks;
NOT LLM playtests, copyright clearance, proof of language equivalence, or participant satisfaction.
"""
from __future__ import annotations
from pathlib import Path
import math
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
ROLEVOW_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdBBYqPZkuFF0t1OeLhqHa8k2UKefT0HbHWXGabX4KDjyJuGw/viewform"
def read(rel):return (ROOT/rel).read_text('utf-8')

class EditionAndScopeGuards(unittest.TestCase):
    def test_51_dnd2014_half_caster_is_rounded_down_per_class(self):
        paladin,ranger=3,2
        self.assertEqual(paladin//2 + ranger//2,2)
        self.assertIn('rounded down',read('adapters/5e-srd51/ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md').lower())

    def test_52_dnd2024_half_caster_rounds_up_per_class(self):
        paladin,ranger=3,2
        self.assertEqual(math.ceil(paladin/2)+math.ceil(ranger/2),3)
        self.assertIn('rounded UP',read('adapters/5e-srd521/ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md'))

    def test_53_dnd2024_grapple_dc_not_2014_contest(self):
        str_mod,proficiency=3,2
        dc=8+str_mod+proficiency
        self.assertEqual(dc,13)
        s=read('adapters/5e-srd521/ADAPTER.md')
        self.assertIn('target chooses a Strength or Dexterity saving throw',s)
        self.assertNotIn('2014 Athletics contest',s.split('### Unarmed Strike / Grapple / Shove',1)[1].split('### Exhaustion',1)[0].replace('old contested-Athletics initiation',''))

    def test_54_dnd2024_hide_is_different_from_2014(self):
        self.assertIn('DC 15 Dexterity (Stealth)',read('adapters/5e-srd521/ADAPTER.md'))
        self.assertIn('Do not silently',read('adapters/5e-srd521/ADAPTER.md'))

    def test_55_dnd2024_resources_do_not_unlock_before_class_level(self):
        s=read('adapters/5e-srd521/COMBAT-CLASSES.md')
        self.assertIn('Fighter level 1 cannot use a level 3 subclass feature',s)
        self.assertIn('levels **per class**',s.lower())

    def test_56_daggerheart_hope_and_fear_both_retained(self):
        s=read('adapters/dh-srd20/ADAPTER.md')
        self.assertIn('Hope',s);self.assertIn('Fear',s)
        self.assertIn('success/failure',s.lower());self.assertIn('D&D',s)

    def test_57_daggerheart_reaction_is_not_action_roll(self):
        s=read('adapters/dh-srd20/ADAPTER.md')
        self.assertIn('Reaction Roll',s)
        self.assertIn('Group Action',s)

    def test_58_hosted_no_unapproved_shared_account(self):
        s=read('multiplayer/HOSTED-PLAY.md')
        for x in ('ONE human host','passwords','synchronized','PC_KNOWN'):
            self.assertIn(x,s)

    def test_59_hosted_first_roll_by_pc_independently(self):
        s=read('multiplayer/HOSTED-PLAY.md')
        self.assertIn('independently for each participating player/PC',s)
        self.assertIn('numeric reply is a result',s)

    def test_60_private_gm_secrets_are_transport_not_prompt_only(self):
        s=read('COME-OTTENERE-IL-MASSIMO.md')
        self.assertIn('not a security boundary',s)
        self.assertIn('the host may see everything',s)

    def test_61_active_guarantee_separate_from_gameplay_validation(self):
        brand=read('BRAND-POSITIONING.md')
        guide=read('COME-OTTENERE-IL-MASSIMO.md')
        readme=read('README.md')
        self.assertIn('ACTIVE since 19 November 2026',brand)
        self.assertIn(ROLEVOW_FORM,brand)
        self.assertIn('Ultra-Guarantee is active separately',guide)
        self.assertIn('public technical playtest',readme)
        self.assertIn('not yet ready for public use as a validated product',readme)

    def test_62_world_first_unverified_not_public(self):
        s=read('BRAND-POSITIONING.md')
        self.assertIn('does not claim a verified worldwide first',s)
        self.assertIn('No measured speed',s)

    def test_63_source_credits_not_claim_of_affiliation(self):
        s=read('CREDITS-AND-INSPIRATIONS.md')
        self.assertIn('not an endorsement',s.lower())
        self.assertIn('not a foundation AI model',s)

    def test_64_toolbox_label_reconciliation(self):
        s=read('library/MASTER-CRAFT-TOOLBOX.md')
        for x in ['MODULE PREP AS DIFF / SITUATION VIEW — ALEXANDRIAN P1',
                  'FALSE CHOICE / CAUSAL ATTRIBUTION GUARD',
                  'SYSTEM STUDY MODE → TABLE CUSTOMIZATION MODE',
                  'ONBOARDING ≠ SESSION ZERO',
                  'ELASTIC CONTENT BANDS — MUST / CUTTABLE / BUFFER']:
            self.assertIn(x,s)

    def test_65_pattern_source_distinctions(self):
        s=read('library/PATTERN-INDEX.md')
        for x in ['FICTIONAL DECEPTION ≠ FACILITATOR DECEPTION',
                  'REVELATION ≠ NAVIGATION — ALEXANDRIAN P0 REFINEMENT',
                  'SPEECH ≠ COMPREHENSION',
                  'VALUED EXPERIENCE ≠ POSITIVE AFFECT',
                  'STAT-BLOCK → BEHAVIOR COMPILER']:
            self.assertIn(x,s)

    def test_66_gm_techniques_not_new_system_rules(self):
        s=read('library/MASTER-CRAFT-TOOLBOX.md')+read('library/PATTERN-INDEX.md')
        self.assertIn('optional on-demand techniques',s)
        self.assertIn('not a universal rule',s.lower())

    def test_67_guide_links_exist(self):
        for f in ['KNOWN-LIMITATIONS.md','SYSTEM-SUPPORT.md']:
            self.assertTrue((ROOT/f).is_file())
        s=read('COME-OTTENERE-IL-MASSIMO.md');self.assertIn('KNOWN-LIMITATIONS.md',s)

    def test_68_no_private_urls_except_authorized_public_form(self):
        for f in ['COME-OTTENERE-IL-MASSIMO.md','CREDITS-AND-INSPIRATIONS.md','BRAND-POSITIONING.md']:
            s=read(f)
            self.assertNotRegex(s,r'docs\.google\.com/(?:document|spreadsheets)/|drive\.google\.com/file/d/')
            for url in re.findall(r'https?://docs\.google\.com/forms/[^\s\)\]<>\"]+',s):
                self.assertEqual(url.rstrip('.,;'),ROLEVOW_FORM,f)
            self.assertNotRegex(s,r'(?i)(?:sk-[A-Za-z0-9]{18,}|ghp_[A-Za-z0-9]{18,})')

    def test_69_files_are_source_locked(self):
        for f in ['COME-OTTENERE-IL-MASSIMO.md','CREDITS-AND-INSPIRATIONS.md','BRAND-POSITIONING.md']:
            self.assertIn('08814049a1d655d7ac31028b28239a67b08fe7cf',read(f))

    def test_70_release_needs_approval(self):
        s=read('BRAND-POSITIONING.md')
        self.assertIn('requires approval and evidence',s)
        self.assertIn('a public technical test is not that release',s)

if __name__=='__main__':unittest.main()
