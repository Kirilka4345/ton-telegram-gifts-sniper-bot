# -*- coding: utf-8 -*-
"""Unit tests for TON Telegram Gifts Sniper Bot."""
import unittest
import sys
from pathlib import Path

# Add parent directory to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ton_gifts_sniper import TON_WALLET, USDT_WALLET, build_sniper_dashboard

class TestGiftsSniper(unittest.TestCase):
    def test_wallets_presence(self):
        """Verify immutable payout wallets."""
        self.assertTrue(TON_WALLET.startswith("UQ"))
        self.assertTrue(USDT_WALLET.startswith("TX"))

    def test_dashboard_generator(self):
        """Verify HTML dashboard generator builds valid output."""
        sample_items = [
            {
                "collection": "Plush Pepe",
                "slug": "plush-pepe",
                "floor_ton": 5.0,
                "next_ton": 6.0,
                "spread_pct": 16.7,
                "buy_url": "https://fragment.com/gifts/plush-pepe",
                "signal": "🔥 UNDER FLOOR SNIPE"
            }
        ]
        out_path = build_sniper_dashboard(sample_items)
        self.assertTrue(out_path.exists())
        html = out_path.read_text(encoding="utf-8")
        self.assertIn("Plush Pepe", html)
        self.assertIn("5.0 TON", html)
        self.assertIn("Experimental price observations", html)

if __name__ == "__main__":
    unittest.main()
