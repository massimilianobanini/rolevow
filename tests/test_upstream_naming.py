"""Static upstream 2026-11-16 editorial parity; not gameplay or legal clearance."""
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def src(p):return (ROOT/p).read_text(encoding='utf-8')
class UpstreamEditorialNamingTests(unittest.TestCase):
    def test_01_three_player_menus_exactly_match(self):
        def menu(p):return src(p).split('**START OF CANONICAL PLAYER-VISIBLE TEXT**')[1].split('**END OF CANONICAL PLAYER-VISIBLE TEXT**')[0].strip()
        self.assertEqual(menu('BOOTSTRAP.md'),menu('START-HERE.md'))
        self.assertEqual(menu('BOOTSTRAP.md'),menu('player/PLAYER.md'))
        self.assertIn('Daggerheart™ (unofficial experimental adapter, SRD 2.0)',menu('BOOTSTRAP.md'))
    def test_02_adapter_has_editorial_label_and_no_english_test_claim(self):
        a=src('adapters/dh-srd20/ADAPTER.md')
        self.assertIn('Unofficial experimental adapter, refined based on player feedback.',a)
        self.assertIn('does **not** mean that RoleVow itself has completed independent English-language playtests',a)
        self.assertIn('41e1e350d3ec72e64dc04a8818a608ddf0d9b4c0',a)
    def test_03_third_party_rights_still_disclosed(self):
        n=src('THIRD-PARTY-NOTICES.md')
        for p in ('DPCGL','SRD 2.0','Daggerheart™','not affiliated'):
            self.assertIn(p,n)
        self.assertIn('DPCGL conditions',n)
    def test_04_no_borrowed_italian_metrics_as_english(self):
        s=src('SYSTEM-SUPPORT.md')
        self.assertIn('NOT EVALUATED',s)
        self.assertIn('**Daggerheart™ (unofficial experimental adapter, SRD 2.0)** | **70%** | **NOT EVALUATED**',s)
        self.assertIn('not derived from English-language measurements',s)
        # The landing links to the limitations; exact edition labels live at guided start.
        self.assertIn('KNOWN-LIMITATIONS.md',src('index.html'))
        self.assertIn('Daggerheart™ (unofficial experimental adapter, SRD 2.0)',src('BOOTSTRAP.md'))
if __name__=='__main__':unittest.main()
