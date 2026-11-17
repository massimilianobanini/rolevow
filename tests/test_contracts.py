"""RoleVow deterministic documentation regression tests (no model/gameplay evaluation).

RC-EN-0.3: only checks frozen Markdown and project routing contracts.
These tests do NOT validate an AI's behaviour, rules interpretation, third-party licences,
privacy compliance, commercial claims or real players' satisfaction.
"""
from __future__ import annotations
import hashlib
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

def source(path):
    return (ROOT / path).read_text(encoding='utf-8')


def menu(path):
    s = source(path)
    assert 'START OF CANONICAL PLAYER-VISIBLE TEXT' in s
    return s.split('**START OF CANONICAL PLAYER-VISIBLE TEXT**',1)[1].split('**END OF CANONICAL PLAYER-VISIBLE TEXT**',1)[0].strip()

class TechnicalIntegrityTests(unittest.TestCase):
    def test_01_pre_release_readme(self):
        s=source('README.md'); self.assertIn('Pre-release',s); self.assertIn('not yet ready for public use',s)

    def test_02_public_test_status(self):
        s=source('README.md');self.assertIn('public technical playtest',s);self.assertIn('No monetary programme is active',s)

    def test_03_mit_git_blob_unchanged(self):
        b=(ROOT/'LICENSE').read_bytes()
        self.assertEqual(hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest(),'f652c8c9d355b7f2401255075c798e855dffec0f')

    def test_04_canonical_playnow_three_copies(self):
        self.assertEqual(menu('BOOTSTRAP.md'),menu('START-HERE.md'))
        self.assertEqual(menu('BOOTSTRAP.md'),menu('player/PLAYER.md'))

    def test_05_exact_six_fields_and_no_seventh(self):
        s=menu('BOOTSTRAP.md'); pos=[s.index(f'{i}. **') for i in range(1,7)]
        self.assertEqual(sorted(pos),pos);self.assertNotIn('7. **',s)

    def test_06_three_systems_menu(self):
        for name in ['D&D 5e 2014','D&D 2024','Daggerheart']:
            self.assertIn(name,menu('BOOTSTRAP.md'))

    def test_07_hosted_not_multiaccount_sync(self):
        s=menu('BOOTSTRAP.md').lower()
        self.assertIn('hosted group',s);self.assertIn('not a shared multi-account',s)

    def test_08_system_router_has_three_adapters(self):
        s=source('RUNTIME-HOTFIX-V0.3.2.md')
        for p in ('adapters/5e-srd51/ADAPTER.md','adapters/5e-srd521/ADAPTER.md','adapters/dh-srd20/ADAPTER.md'):
            self.assertIn(p,s)

    def test_09_all_seven_runtime_dependencies_exist(self):
        for p in ('RUNTIME-HOTFIX-V0.3.2-BASE.md','RUNTIME-HOTFIX-V0.3.3.md','RUNTIME-HOTFIX-V0.3.4.md','RUNTIME-HOTFIX-V0.3.5.md','RUNTIME-HOTFIX-V0.3.6.md','RUNTIME-V0.4-CANDIDATE.md','V0.4-CANDIDATE.md'):
            self.assertTrue((ROOT/p).is_file(),p)

    def test_10_no_stale_dependency_claims(self):
        s=source('RUNTIME-HOTFIX-V0.3.2.md')+'\n'+source('START-HERE.md')
        for bad in ('not all prepared in RC-EN-0.2','They are **not available in RoleVow at this draft stage**'):
            self.assertNotIn(bad,s)

    def test_11_player_uses_active_system_schema(self):
        s=source('player/PLAYER.md')
        self.assertIn('only the active system',s)
        self.assertNotIn("use the 2014 D&D adapter's character creation",s)

    def test_12_master_all_three_edition_sources(self):
        s=source('master/MASTER.md')
        self.assertIn('Daggerheart™ (unofficial experimental adapter, SRD 2.0)',s)
        self.assertNotIn('is the only system-specific supported target',s)

    def test_13_social_procedure_system_must_match(self):
        s=source('protocols/PROTOCOLS.md');self.assertIn("selected system and edition's",s)
        self.assertNotIn('Use a 2014 D&D social mechanic',s)

    def test_14_combat_procedure_system_must_match(self):
        s=source('protocols/PROTOCOLS.md');self.assertIn('only the active system and edition',s)
        self.assertNotIn('using **D&D 2014** rules',s)

    def test_15_environment_system_must_match(self):
        s=source('protocols/PROTOCOLS.md');self.assertIn("active system and edition's",s)
        self.assertNotIn('apply 2014 D&D environmental penalties',s)

    def test_16_system_agnostic_causality(self):
        s=source('RUNTIME-HOTFIX-V0.3.4.md')
        self.assertIn('D&D 2014, D&D 2024, or Daggerheart',s)

    def test_17_no_2014_only_known_limitations(self):
        s=source('KNOWN-LIMITATIONS.md');self.assertNotIn('D&D 5e 2014/SRD 5.1 only',s)
        self.assertIn('Daggerheart/SRD 2.0',s)

    def test_18_dnd2014_nat1_20_not_auto_check_crit(self):
        s=source('adapters/5e-srd51/ADAPTER.md').lower()
        self.assertRegex(s,r'2014 natural 1/20 firewall')

    def test_19_dnd2024_hide_dc15(self):
        s=source('adapters/5e-srd521/ADAPTER.md')
        self.assertRegex(s,r'DC 15 Dexterity \(Stealth\)')

    def test_20_dnd2024_grapple_save_distinct(self):
        s=source('adapters/5e-srd521/ADAPTER.md');self.assertIn('Strength or Dexterity saving throw',s)

    def test_21_dnd2024_heroic_inspiration_after_roll(self):
        s=source('adapters/5e-srd521/ADAPTER.md');self.assertIn('post-roll reroll',s)

    def test_22_dnd2024_round_up_vs_2014_round_down(self):
        e=source('adapters/5e-srd521/ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md')
        c=source('adapters/5e-srd51/ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md')
        self.assertIn('rounded UP',e);self.assertIn('rounded DOWN',e);self.assertIn('rounded down',c.lower())

    def test_23_no_italian_multiclass_in_2024(self):
        s=source('adapters/5e-srd521/ADVANCEMENT-EQUIPMENT-ENVIRONMENT.md')
        for bad in ('somma livelli','arrotondata PER ECCESSO','un terzo per difetto','Multiclasse 2024'):
            self.assertNotIn(bad,s)

    def test_24_2024_draft_not_presented_public(self):
        s=source('adapters/5e-srd521/ADAPTER.md')
        self.assertIn('not english actual-play validated',s.lower());self.assertNotIn('official adapter',s.lower().replace('unofficial adapter',''))

    def test_25_daggerheart_duality_spotlight(self):
        s=source('adapters/dh-srd20/ADAPTER.md')
        for t in ('Hope','Fear','spotlight','Reaction Roll','Loadout','Vault'):
            self.assertIn(t,s)

    def test_26_daggerheart_no_silent_dnd_transfer(self):
        s=source('adapters/dh-srd20/ADAPTER.md')
        self.assertIn('do not import',s.lower())
        self.assertIn('D&D',s)

    def test_27_daggerheart_license_go_no_go(self):
        s=source('adapters/dh-srd20/ADAPTER.md')+source('THIRD-PARTY-NOTICES.md')
        self.assertRegex(s,r'(?i)DPCGL');self.assertRegex(s,r'(?i)not affiliated|not endorsed');self.assertIn('DPCGL conditions',s)

    def test_28_host_roster_and_boundaries(self):
        s=source('multiplayer/HOSTED-PLAY.md')
        for t in ('player_id','pc_id','PC_KNOWN','player-to-player','one human host'):
            self.assertIn(t,s.lower() if t=='one human host' else s)

    def test_29_no_host_claim_of_private_channels(self):
        s=source('multiplayer/HOSTED-PLAY.md')
        self.assertIn('does not create separate private ChatGPT channels',s)

    def test_30_no_international_guarantee(self):
        s=source('README.md')+source('BOOTSTRAP.md')+source('feedback/FEEDBACK-AND-METRICS.md')
        self.assertIn('not yet available',s.lower());self.assertRegex(s.lower(),r'not active|no monetary programme is active')

    def test_31_no_italian_payment_form_urls(self):
        for p in ROOT.rglob('*.md'):
            if 'PRIVATE_QA' not in p.parts:
                self.assertNotIn('docs.google.com/forms/',p.read_text(encoding='utf8'),p.name)

    def test_32_no_private_drive_links(self):
        for p in ROOT.rglob('*.md'):
            if 'PRIVATE_QA' not in p.parts:
                self.assertNotRegex(p.read_text(encoding='utf8'),r'https?://(?:docs\.google\.com/(?:document|spreadsheets)/d/|drive\.google\.com/file/d/)',p.name)

    def test_33_license_notices_both_dd(self):
        s=source('THIRD-PARTY-NOTICES.md')
        self.assertIn('This work includes material taken from the System Reference Document 5.1',s)
        self.assertIn('This work includes material from the System Reference Document 5.2.1',s)

    def test_34_privacy_is_release_blocker(self):
        self.assertIn('before any actual monetary intake',source('PRIVACY.md'))

    def test_35_provisional_upstream_confidence_not_english_validation(self):
        s=source('SYSTEM-SUPPORT.md')
        matrix=s.split('## Current English system matrix',1)[1].split('## Runtime routing',1)[0]
        for name,value in [('D&D 5e 2014 (SRD 5.1)','85%'),('D&D 2024 (SRD 5.2.1)','75%'),('Daggerheart™ (unofficial experimental adapter, SRD 2.0)','70%')]:
            self.assertIn(f'| **{name}** | **{value}** | **NOT EVALUATED** |',matrix)
        self.assertIn('not derived from English-language measurements',s)
        self.assertIn('provisional reference from Divertoscopio',s)

    def test_35a_exact_system_menu_and_default_retained(self):
        expected='2. **System:** D&D 5e 2014 (SRD 5.1) / D&D 2024 (SRD 5.2.1) / Daggerheart™ (unofficial experimental adapter, SRD 2.0) / Other (state your rules).'
        for path in ('BOOTSTRAP.md','START-HERE.md','player/PLAYER.md'):
            self.assertIn(expected,menu(path))
            self.assertNotIn('SRD 5.1 (default)',menu(path))
            self.assertIn('Solo, D&D 5e 2014, classic fantasy',menu(path))
            self.assertNotIn('Game Master → Player (OOC)',menu(path))

    def test_35b_visible_ooc_callout_all_player_routes(self):
        for path in ('BOOTSTRAP.md','START-HERE.md','core/CORE.md','player/PLAYER.md','RUNTIME-HOTFIX-V0.3.3.md'):
            s=source(path)
            self.assertIn('Game Master → Player (OOC)',s,path)
            self.assertIn('separate Markdown blockquote',s,path)
            self.assertIn('Keep narration, NPC dialogue and in-fiction consequences outside it',s,path)
            self.assertIn('OOC question alone pauses fictional time',s,path)
        self.assertIn('Customize First, Customize in Depth',source('player/PLAYER.md'))
        self.assertIn('Game Master → Player (OOC)',source('SYSTEM-SUPPORT.md'))

    def test_36_protocol_p0_complete(self):
        s=source('protocols/PROTOCOLS.md')
        for i in range(1,22):
            self.assertRegex(s,rf'(?m)^## P0-{i:02d} \u2014')

    def test_37_runtime_router_uses_active_system(self):
        s=source('RUNTIME-HOTFIX-V0.3.2.md')
        self.assertIn('ONLY the active edition-/system-matched adapter',s)

    def test_38_master_libraries_included(self):
        for p in ['library/MASTER-CRAFT-TOOLBOX.md','library/PATTERN-INDEX.md']:
            self.assertTrue((ROOT/p).is_file())
        self.assertNotIn('toolbox and pattern index must be added',source('KNOWN-LIMITATIONS.md'))

    def test_39_no_broken_relative_md_links(self):
        for f in ROOT.rglob('*.md'):
            if 'PRIVATE_QA' in f.parts:continue
            for link in re.findall(r'(?<!\!)\]\(([^)]+)\)',f.read_text(encoding='utf8')):
                path=link.strip().split('#',1)[0].split('?',1)[0]
                if not path or path.startswith(('http://','https://','mailto:','data:')):continue
                self.assertTrue((f.parent/path).is_file(),f'{f.relative_to(ROOT)} -> {link}')

    def test_40_source_sha_frozen(self):
        self.assertIn('08814049a1d655d7ac31028b28239a67b08fe7cf',source('START-HERE.md'))


    def test_41_exact_negative_price_ultra_guarantee_name(self):
        canon = 'Negative Price Ultra-Guarantee'
        for path in ('README.md','BOOTSTRAP.md','START-HERE.md','BRAND-POSITIONING.md','LEGAL-CLAIMS.md','KNOWN-LIMITATIONS.md','index.html','feedback/FEEDBACK-AND-METRICS.md'):
            content = source(path)
            self.assertIn(canon, content, path)
            self.assertNotIn('Negative-Price Ultra-Guarantee', content, path)
            self.assertNotIn('NEGATIVE-PRICE ULTRA-GUARANTEE', content, path)

    def test_42_private_budget_rules_not_the_obsolete_planning_assumption(self):
        brand = source('BRAND-POSITIONING.md')
        feedback = source('feedback/FEEDBACK-AND-METRICS.md')
        self.assertIn('€20 per month and €100 lifetime', brand)
        self.assertIn('€20/month and €100 lifetime', feedback)
        self.assertIn('NOT active', brand)
        self.assertIn('No public Google Form', feedback.replace('**', '').replace('NO public', 'No public'))

if __name__=='__main__':unittest.main()
