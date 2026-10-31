"""Experimental Fragment HTML price observer. No trades or publishing."""
import json
from html import escape
from urllib.parse import urlsplit
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


GH = r"C:\Users\Huesos\AppData\Local\Programs\gh\gh.exe"
TON_WALLET = "UQCwrgVAYHvlJe87-eOAK01ZzMW42E17YnbCyWPPkKeLhEpP"
USDT_WALLET = "TXCYzTR3Br4MuWXUnGRvpA3EaYC7iyydYj"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0.0.0"}


def http_json(url: str):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode("utf-8", errors="ignore"))


def fetch_live_telegram_gifts() -> list[dict]:
    """Fetches real Telegram Gift NFT collections and items from Fragment & TonAPI."""
    gifts = []
    # Query Fragment Collectible Gifts HTML/data & TonAPI NFT collections
    try:
        req = urllib.request.Request("https://fragment.com/gifts", headers=UA)
        html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="ignore")
        import re
        # Extract gift collection names and counts from Fragment
        matches = re.findall(r'href="/gifts/([a-z0-9_-]+)"[^>]*>.*?tm-main-filters-name[^>]*>([^<]+)<', html, re.S)
        seen = set()
        for slug, name in matches[:45]:
            if slug in seen:
                continue
            seen.add(slug)
            gifts.append({"slug": slug, "name": name.strip(), "url": f"https://fragment.com/gifts/{slug}"})
    except Exception as e:
        print(f"[warn] Fragment gifts fetch: {e}")

    # Enrich top gift collections with live on-chain listings / floor data
    enriched = []
    for g in gifts[:35]:
        slug = g["slug"]
        try:
            req = urllib.request.Request(f"https://fragment.com/gifts/{slug}?filter=sale&sort=price_asc", headers=UA)
            page = urllib.request.urlopen(req, timeout=12).read().decode("utf-8", errors="ignore")
            import re
            prices = [float(p.replace(",", "")) for p in re.findall(r'icon-ton">(\d[\d,]*\.?\d*)<', page)]
            if not prices:
                prices = [float(p.replace(",", "")) for p in re.findall(r'tm-value icon-before icon-ton">(\d[\d,]*\.?\d*)<', page)]
            floor = prices[0] if prices else 0.0
            second = prices[1] if len(prices) > 1 else floor
            spread_pct = round(((second - floor) / second) * 100, 1) if second > floor > 0 else 0.0
            enriched.append({
                "collection": g["name"],
                "slug": slug,
                "floor_ton": floor,
                "next_ton": second,
                "spread_pct": spread_pct,
                "sample_prices": prices[:5],
                "buy_url": f"https://fragment.com/gifts/{slug}?filter=sale&sort=price_asc",
                "signal": "🔥 UNDER FLOOR SNIPE" if spread_pct >= 8.0 else ("✅ ARBITRAGE WATCH" if spread_pct >= 3.0 else "NORMAL"),
            })
        except Exception as e:
            print(f"[warn] {slug}: {e}")
    enriched.sort(key=lambda x: x["spread_pct"], reverse=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "live_ton_gifts_arbitrage.json").write_text(json.dumps(enriched, indent=2, ensure_ascii=False), encoding="utf-8")
    return enriched


def build_sniper_dashboard(items: list[dict]):
    rows = ""
    for original in items:
        it = dict(original)
        it["collection"] = escape(str(it["collection"]))
        it["signal"] = escape(str(it["signal"]))
        url = str(it["buy_url"])
        it["buy_url"] = escape(url, quote=True) if urlsplit(url).scheme == "https" and urlsplit(url).hostname == "fragment.com" else "#"
        badge_col = "#3fb950" if "SNIPE" in it["signal"] else ("#d29922" if "WATCH" in it["signal"] else "#8b949e")
        rows += f"""<tr>
          <td><b>{it['collection']}</b></td>
          <td style="color:#58a6ff;font-weight:bold;">{it['floor_ton']} TON</td>
          <td>{it['next_ton']} TON</td>
          <td style="color:{badge_col};font-weight:bold;">+{it['spread_pct']}% ({it['signal']})</td>
          <td><a href="{it['buy_url']}" target="_blank">Открыть лот ↗</a></td>
        </tr>"""
    html = f"""<!DOCTYPE html>
<html lang="ru"><head><meta charset="UTF-8"><title>Fragment Price Observer</title>
<style>
body{{background:#0d1117;color:#e6edf3;font-family:system-ui,sans-serif;padding:24px}}
.wrap{{max-width:1180px;margin:0 auto}}
.card{{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:18px;margin-bottom:20px}}
table{{width:100%;border-collapse:collapse;margin-top:12px}}
th,td{{padding:10px;text-align:left;border-bottom:1px solid #30363d}}
a{{color:#58a6ff;text-decoration:none}}
.warn{{background:rgba(248,81,73,0.15);border:1px solid #f85149;padding:12px;border-radius:8px;margin-bottom:18px}}
</style></head><body><div class="wrap">
<h1>Fragment Price Observer</h1>
<p>Generated: {datetime.now().isoformat()} | Experimental price observations; no verified profit.</p>
<div class="warn">HTML parsing may be incomplete. Price gaps do not establish liquidity, executable trades or profit.</div>
<div class="card">
  <h2>🎯 Живой радар спредов Telegram Gifts (Fragment / TON On-Chain)</h2>
  <table><thead><tr><th>Коллекция подарка</th><th>Нижний лот (Floor)</th><th>Следующий лот</th><th>Спред арбитража</th><th>Действие</th></tr></thead>
  <tbody>{rows}</tbody></table>
</div>
</div></body></html>"""
    out = BASE_DIR / "TON_GIFTS_SNIPER.html"
    out.write_text(html, encoding="utf-8")
    return out


if __name__ == "__main__":
    items = fetch_live_telegram_gifts()
    dash = build_sniper_dashboard(items)
    print(f"Observed {len(items)} collections -> {dash}")
