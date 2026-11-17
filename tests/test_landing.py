"""Static landing regression tests. No browser, network, gameplay or legal approval."""
import re
from pathlib import Path
from bs4 import BeautifulSoup
import unittest
import subprocess

ROOT=Path(__file__).resolve().parents[1]
HTML=(ROOT/'index.html').read_text('utf8')
JS=(ROOT/'landing.js').read_text('utf8')
CSS=(ROOT/'landing.css').read_text('utf8')
SITE=BeautifulSoup(HTML,'html.parser')

class LandingScaffoldTests(unittest.TestCase):
    def test_41_english_and_accessible_title(self):
        self.assertEqual(SITE.html['lang'],'en')
        self.assertIn('RoleVow',SITE.title.get_text())
        self.assertEqual(SITE.select_one('a.skip')['href'],'#main')

    def test_42_pre_release_status_no_fictional_offer(self):
        self.assertEqual(SITE.body.get('data-release-status'),'pre-release')
        self.assertIn('not active',SITE.get_text(' ',strip=True).lower())

    def test_43_canonical_battlecry(self):
        self.assertIn("Play your role, now it's your roll. Our vow? To make you say wow.",HTML)

    def test_44_both_dd_and_daggerheart_disclosed(self):
        for t in ('D&D 5e (2014)','D&D (2024)','Daggerheart','SRD 5.2.1','SRD 5.1','SRD 2.0'):
            self.assertIn(t,HTML)

    def test_45_hosted_not_fake_group_chat(self):
        self.assertIn('one human host',HTML.lower())
        self.assertIn('not</strong> a synchronized multi-account',HTML)

    def test_46_test_start_enabled_without_guarantee(self):
        b=SITE.select_one('#copy-starter')
        self.assertIsNotNone(b)
        self.assertFalse(b.has_attr('disabled'))
        self.assertIn('["pre-release", "released"]',JS)

    def test_47_repository_exact_and_copy_prompt(self):
        self.assertIn('https://github.com/massimilianobanini/rolevow',JS)
        self.assertIn("Let's begin.",JS)
        self.assertIn('navigator.clipboard.writeText',JS)

    def test_48_no_leaked_form_or_private_drive(self):
        for t in ('docs.google.com/forms','docs.google.com/document/d/','drive.google.com/file/d/','1FAIpQL'):
            self.assertNotIn(t,HTML+JS)

    def test_49_no_unapproved_visual_hammer(self):
        self.assertEqual(len(SITE.find_all('img')),0)
        self.assertNotIn('visual-hammer',HTML.lower()+CSS.lower()+JS.lower())

    def test_50_node_syntax_and_manual_pages_only(self):
        p=subprocess.run(['node','--check',str(ROOT/'landing.js')],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr)
        y=(ROOT/'.github/workflows/landing-pages.yml').read_text('utf8')
        self.assertIn('workflow_dispatch:',y)
        self.assertNotIn('  push:',y)
        self.assertIn('node --check landing.js',y)

if __name__=='__main__':unittest.main()
