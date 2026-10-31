# 💎 ton-telegram-gifts-sniper-bot

> **Real-Time Floor Price Tracker, Spread Scanner & Under-Floor Radar for Telegram Collectible Gifts and TON NFT Markets.**

[![Latest Release](https://img.shields.io/github/v/release/Kirilka4345/ton-telegram-gifts-sniper-bot?style=for-the-badge&logo=github&color=success)](https://github.com/Kirilka4345/ton-telegram-gifts-sniper-bot/releases/latest)
[![Download Zip](https://img.shields.io/badge/Download_v1.0.0-ZIP-blue?style=for-the-badge&logo=zip)](https://github.com/Kirilka4345/ton-telegram-gifts-sniper-bot/releases/download/v1.0.0/TON-Telegram-Gifts-Sniper-Bot-v1.0.zip)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![Tests: Passing](https://img.shields.io/badge/Tests-3%2F3%20Passing-success?style=for-the-badge&logo=python)](tests/test_gifts_sniper.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🚀 Overview

**ton-telegram-gifts-sniper-bot** is a specialized real-time monitoring and arbitrage scanner for the rapidly expanding Telegram Gifts and TON digital collectibles ecosystem (Portals Market, Fragment, Getgems). It continuously calculates floor-to-next price spreads, identifies mispriced listings, and flags profitable arbitrage opportunities.

### ⚡ Key Capabilities
- **Real-Time Floor Tracking:** Monitors live floor prices and immediate price gaps across all major gift collections.
- **Instant Arbitrage Spread Detection:** Flags items listed below fair market value with automated margin calculation.
- **Interactive Dashboard:** Generates an HTML terminal view (`TON_GIFTS_SNIPER.html`) for at-a-glance market analytics.
- **Lightweight Zero-Key Architecture:** Operates with public RPC endpoints and market feeds without requiring paid API keys.
- **Instant Notification Hooks:** Ready to broadcast buy signals to Telegram channels, private chats, or webhooks.

---

## ⚡ Quickstart

### 1. Installation
Clone the repository or [download the release archive](https://github.com/Kirilka4345/ton-telegram-gifts-sniper-bot/releases/download/v1.0.0/TON-Telegram-Gifts-Sniper-Bot-v1.0.zip):

```bash
git clone https://github.com/Kirilka4345/ton-telegram-gifts-sniper-bot.git
cd ton-telegram-gifts-sniper-bot
pip install -r requirements.txt
```

### 2. Configuration
Review `config.example.json` to customize your scan thresholds, notification webhooks, and target collections:

```json
{
  "min_spread_ton": 1.0,
  "poll_interval_seconds": 30,
  "wallets": {
    "TON": "UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP",
    "USDT_TRC20": "TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj"
  }
}
```

### 3. Run
```bash
python ton_gifts_sniper.py
# or double-click START.bat on Windows
```

---

## 💼 Pro Trading Bots & Custom On-Chain Automation

Looking for high-frequency on-chain sniping, automated Tonkeeper/TonConnect wallet execution (v5r1 / v4r2), or bespoke Telegram Mini App integration?

I build custom Web3 & crypto bots:
- **TON Ecosystem:** Jetton sniping, DEX liquidity pool monitors (DeDust / STON.fi), Fragment phone number & username bidders.
- **Security & Reliability:** Non-custodial architectures, rate-limit resilience, multi-node RPC failover.

### 📩 Contact & Inquiries
- **GitHub:** [@Kirilka4345](https://github.com/Kirilka4345)
- **Direct Crypto Licensing ($15 – $49):**
  - **TON:** `UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP`
  - **USDT (TRC-20):** `TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj`
  - **EVM (Base / ETH):** `0x12f0a957bd351492252aac81198edba4c5a56790`
