import sys, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import ton_gifts_sniper as scanner

class DashboardSafetyTests(unittest.TestCase):
    def test_external_markup_and_url_are_not_executed(self):
        item = dict(collection='<script>alert(1)</script>', signal='<img onerror=alert(1)>', buy_url='javascript:alert(1)', floor_ton=1, next_ton=2, spread_pct=50)
        with tempfile.TemporaryDirectory() as tmp, patch.object(scanner, 'BASE_DIR', Path(tmp)):
            text = scanner.build_sniper_dashboard([item]).read_text(encoding='utf-8')
        self.assertNotIn('<script>', text)
        self.assertNotIn('javascript:', text)
        self.assertIn('&lt;script&gt;', text)
        self.assertNotIn('0.0045 TON', text)

    def test_empty_observations_do_not_claim_profit(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(scanner, 'BASE_DIR', Path(tmp)):
            text = scanner.build_sniper_dashboard([]).read_text(encoding='utf-8')
        self.assertIn('no verified profit', text)
