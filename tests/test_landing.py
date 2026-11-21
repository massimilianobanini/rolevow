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
        self.assertEqual(SITE.select_one('a.skip-link')['href'],'#main')

    def test_42_active_conditional_guarantee_not_gameplay_validation(self):
        page=SITE.get_text(' ',strip=True).lower()
        self.assertIn('technical playtest',page)
        self.assertIn('€1 net reputational indemnity',page)
        self.assertIn('no automatic payment',page)
        self.assertIn('published terms',page)

    def test_43_canonical_battlecry(self):
        self.assertEqual(SITE.select_one('.battlecry').get_text(' ',strip=True),
                         "Play your role, now it's your roll. Our vow? To make you say wow.")

    def test_44_supported_rulesets_disclosed_at_guided_start(self):
        self.assertIn('KNOWN-LIMITATIONS.md',HTML)
        bootstrap=(ROOT/'BOOTSTRAP.md').read_text('utf8')
        for t in ('D&D 5e 2014 (SRD 5.1)', 'D&D 2024 (SRD 5.2.1)',
                  'Daggerheart™ (unofficial experimental adapter, SRD 2.0)'):
            self.assertIn(t,bootstrap)

    def test_45_hosted_not_fake_group_chat(self):
        page=SITE.get_text(' ',strip=True).lower()
        self.assertIn('one human relay host and one chat',page)
        self.assertIn('not synchronized individual accounts',page)

    def test_46_guided_start_enabled_without_skipping_chatgpt(self):
        b=SITE.select_one('#start-rolevow')
        self.assertIsNotNone(b)
        self.assertFalse(b.has_attr('disabled'))
        self.assertIn('document.querySelectorAll("[data-start-rolevow]")',JS)
        self.assertIn('navigator.clipboard.writeText',JS)
        self.assertIn('START_PROMPT=REPO+',JS)

    def test_47_repository_exact_and_copy_prompt(self):
        self.assertIn('https://github.com/massimilianobanini/rolevow',JS)
        self.assertIn("Let's begin.",JS)
        self.assertIn('navigator.clipboard.writeText',JS)

    def test_48_no_leaked_form_or_private_drive(self):
        for t in ('docs.google.com/forms','docs.google.com/document/d/','drive.google.com/file/d/','1FAIpQL'):
            self.assertNotIn(t,HTML+JS)

    def test_49_only_approved_visual_hammer_images(self):
        images=SITE.find_all('img')
        self.assertGreaterEqual(len(images),2)
        for img in images:
            self.assertEqual(img.get('src'),'assets/brand/rolevow-visual-hammer-transparent.png')
        self.assertIn('RoleVow Visual Hammer',HTML)

    def test_50_node_syntax_and_manual_pages_only(self):
        p=subprocess.run(['node','--check',str(ROOT/'landing.js')],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr)
        y=(ROOT/'.github/workflows/landing-pages.yml').read_text('utf8')
        self.assertIn('workflow_dispatch:',y)
        self.assertIn('  push:',y)
        self.assertIn('      - index.html',y)
        self.assertIn('      - assets/brand/rolevow-visual-hammer-transparent.png',y)
        self.assertIn('node --check landing.js',y)

if __name__=='__main__':unittest.main()
