#!/usr/bin/env python3
import json, html
ROOT="/Users/Manos/Desktop/casa-valesa-website"
d=json.load(open(f"{ROOT}/content/island/explore-thassos.json"))
SITE="https://casavalesa.gr"; WA="306986757880"; AIRBNB="https://www.airbnb.com/rooms/1157207333231807379"

ICON={
 "beaches":"🏖️","villages":"🏘️","sites":"🏛️","tavernas":"🍽️","cafes":"☕",
 "nightlife":"🌙","agrotourism":"🫒","boating":"⛵","fishing":"🎣","walks":"🥾"}
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Manrope:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

cats=d["categories"]
subnav="".join(f'<a href="#{c["id"]}">{ICON.get(c["id"],"")} {html.escape(c["title"])}</a>' for c in cats)+'<a href="#history">📜 History</a><a href="#daytrips">🗺️ Day trips</a>'

import urllib.parse, re as _re
HOUSE="40.730728,24.5505072"  # Casa Valesa, Skala Sotiros
def directions(name):
    # strip parentheticals / slashes for a clean map query
    q=_re.sub(r'\(.*?\)','',name).split('/')[0].strip()
    dest=urllib.parse.quote(f"{q}, Thassos, Greece")
    url=f"https://www.google.com/maps/dir/?api=1&origin={HOUSE}&destination={dest}&travelmode=driving"
    return f'<a class="dir" href="{url}" target="_blank" rel="noopener">🧭 Directions from Casa Valesa</a>'

def item_block(it):
    meta = f'<span class="meta">{html.escape(it.get("meta",""))}</span>' if it.get("meta") else ""
    tip  = f'<p class="tip"><b>Local tip:</b> {html.escape(it["tip"])}</p>' if it.get("tip") else ""
    return (f'<div class="iv"><div class="iv-h"><h3>{html.escape(it["name"])}</h3>{meta}</div>'
            f'{it.get("desc","")}{tip}{directions(it["name"])}</div>')

def cat_block(c):
    items="".join(item_block(it) for it in c.get("items",[]))
    return (f'<section class="cat" id="{c["id"]}"><div class="wrap">'
      f'<h2><span class="ic">{ICON.get(c["id"],"")}</span> {html.escape(c["title"])}</h2>'
      f'{c.get("blurb","")}<div class="ivs">{items}</div></div></section>')

daytrips="".join(f'<div class="dt"><h3>{html.escape(t["name"])}</h3>{t.get("html","")}</div>' for t in d.get("day_trips",[]))

doc=f'''<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Explore Thassos — Beaches, Villages, Food & Things to Do | Casa Valesa</title>
<meta name="description" content="A local guide to Thassos: the best and secret beaches, mountain villages (Theologos, Panagia, Potos, Sotiras, Prinos), archaeological sites, tavernas, boating, walking paths and ready-made day trips from Skala Sotiros.">
<link rel="canonical" href="{SITE}/explore-thassos.html">
<meta property="og:title" content="Explore Thassos — the local guide"><meta property="og:type" content="article">
<meta property="og:image" content="{SITE}/blog/heroes/beach-path.jpg">
{FONTS}
<style>
:root{{--marble:#F7F6F2;--marble-2:#EDEBE3;--pine:#12352A;--aegean:#1F7A78;--seaglass:#9FCEC8;--sun:#E3A93C;--ink:#16201C;--muted:#5E6A64;--line:rgba(18,53,42,.14);--shadow:0 24px 60px -24px rgba(18,53,42,.35)}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--marble);color:var(--ink);font-family:"Manrope",system-ui,sans-serif;line-height:1.7}}
h1,h2,h3{{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;line-height:1.08;color:var(--pine);margin:0}}
a{{color:var(--aegean)}}img{{max-width:100%;display:block}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 24px}}
header.nav{{position:sticky;top:0;z-index:50;background:rgba(247,246,242,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}}
header.nav .inner{{max-width:1140px;margin:0 auto;padding:13px 24px;display:flex;align-items:center;justify-content:space-between}}
.brand{{font-family:"Cormorant Garamond",serif;font-size:1.4rem;color:var(--pine);text-decoration:none}}
.brand b{{font-weight:600}}
.brandwrap{{display:flex;align-items:center;gap:10px}}
.loc-badge{{display:inline-flex;align-items:center;gap:6px;font-family:"JetBrains Mono",monospace;font-size:.6rem;letter-spacing:.12em;text-transform:uppercase;color:var(--pine);background:var(--marble-2);border:1px solid var(--line);padding:5px 9px;border-radius:100px;white-space:nowrap}}
@media(max-width:560px){{.loc-badge{{display:none}}}}.nav a.book{{background:var(--sun);color:var(--pine);padding:8px 16px;border-radius:100px;text-decoration:none;font-size:.82rem;font-weight:600}}
.hero{{position:relative;height:56vh;min-height:360px;display:flex;align-items:flex-end;color:#fff;overflow:hidden}}
.hero img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.hero::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,28,22,.2),rgba(8,28,22,.82))}}
.hero .wrap{{position:relative;z-index:2;padding-bottom:40px}}
.hero .eyebrow{{font-family:"JetBrains Mono",monospace;font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;color:var(--seaglass)}}
.hero h1{{color:#fff;font-size:clamp(2.4rem,7vw,5rem);margin-top:10px}}
.intro{{padding:46px 0 8px}}.intro p{{font-size:1.12rem;max-width:70ch}}
.subnav{{position:sticky;top:51px;z-index:40;background:var(--pine);overflow-x:auto;white-space:nowrap;-webkit-overflow-scrolling:touch}}
.subnav .wrap{{display:flex;gap:6px;padding:10px 24px}}
.subnav a{{color:var(--seaglass);text-decoration:none;font-size:.8rem;font-family:"JetBrains Mono",monospace;letter-spacing:.04em;padding:6px 12px;border-radius:100px;flex:0 0 auto}}
.subnav a:hover{{background:rgba(255,255,255,.1);color:#fff}}
.cat{{padding:40px 0;border-bottom:1px solid var(--line)}}
.cat h2{{font-size:clamp(1.8rem,4vw,2.6rem);margin-bottom:6px;display:flex;align-items:center;gap:12px}}
.cat .ic{{font-size:.85em}}
.cat>.wrap>p{{color:var(--muted);max-width:64ch;margin:8px 0 24px}}
.ivs{{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:20px}}
.iv{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:20px 22px}}
.iv-h h3{{font-size:1.32rem}}
.iv .meta{{display:block;font-family:"JetBrains Mono",monospace;font-size:.7rem;letter-spacing:.06em;color:var(--aegean);margin:4px 0 8px;text-transform:uppercase}}
.iv p{{margin:6px 0;color:#2c352f;font-size:.96rem}}
.iv .tip{{background:var(--marble-2);border-radius:8px;padding:8px 12px;font-size:.88rem;color:var(--pine);margin-top:10px}}
.iv .dir{{display:inline-block;margin-top:12px;font-family:"JetBrains Mono",monospace;font-size:.72rem;letter-spacing:.04em;color:var(--aegean);text-decoration:none;border:1px solid var(--line);padding:7px 12px;border-radius:100px}}
.iv .dir:hover{{background:var(--aegean);color:#fff}}
.hist{{padding:52px 0;background:var(--marble-2)}}.hist h2{{font-size:clamp(2rem,5vw,3rem);margin-bottom:16px}}.hist .wrap>div{{max-width:72ch;font-size:1.05rem}}
.daytrips{{padding:52px 0}}.daytrips h2{{font-size:clamp(2rem,5vw,3rem);margin-bottom:20px}}
.dts{{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:20px}}
.dt{{background:#fff;border:1px solid var(--line);border-left:3px solid var(--sun);border-radius:12px;padding:22px 24px}}.dt h3{{font-size:1.3rem;margin-bottom:8px}}
.cta{{background:var(--pine);color:var(--marble);text-align:center;padding:56px 24px}}
.cta h2{{color:#fff;font-size:clamp(2rem,5vw,3.2rem);margin-bottom:10px}}.cta p{{color:rgba(247,246,242,.82);max-width:46ch;margin:0 auto 22px}}
.btns{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}}
.btn{{padding:13px 24px;border-radius:100px;text-decoration:none;font-weight:600;font-size:.92rem}}
.btn-pri{{background:var(--sun);color:var(--pine)}}.btn-wa{{background:#25D366;color:#06351d}}.btn-gh{{background:rgba(247,246,242,.12);color:#fff;border:1px solid rgba(247,246,242,.4)}}
footer{{background:#0c241c;color:rgba(247,246,242,.7);font-size:.86rem}}footer .wrap{{padding:40px 24px;display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap}}footer a{{color:var(--seaglass);text-decoration:none}}footer .brand{{color:#fff;font-size:1.5rem;display:block;margin-bottom:8px}}
@media(max-width:640px){{.hero{{height:46vh}}}}
</style></head><body>
<header class="nav"><div class="inner"><span class="brandwrap"><a class="brand" href="index.html">Casa <b>Valesa</b></a><span class="loc-badge"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path fill="#1F7A78" d="M3 16c2-5 5-8 9-8s7 3 9 8c-3 2-5.5 2-9 2s-6 0-9-2z"/><circle cx="18" cy="6" r="2.1" fill="#E3A93C"/><path stroke="#7fb9b3" stroke-width="1.3" fill="none" d="M2 20c2 1 4 1 6 0s4-1 6 0 4 1 6 0"/></svg>Thassos · Greece</span></span>
<nav><a href="blog/index.html" style="text-decoration:none;color:var(--pine);margin-right:18px;font-size:.86rem">Journal</a><a class="book" href="index.html#book">Book now</a></nav></div></header>
<div class="hero"><img src="blog/heroes/beach-path.jpg" alt="Explore Thassos">
<div class="wrap"><span class="eyebrow">Θάσος · The island guide</span><h1>{html.escape(d.get("title","Explore Thassos"))}</h1></div></div>
<div class="subnav"><div class="wrap">{subnav}</div></div>
<div class="intro"><div class="wrap">{d.get("intro_html","")}</div></div>
{''.join(cat_block(c) for c in cats)}
<section class="hist" id="history"><div class="wrap"><h2>📜 A short history of Thassos</h2><div>{d.get("history_html","")}</div></div></section>
<section class="daytrips" id="daytrips"><div class="wrap"><h2>🗺️ Ready-made day trips from Skala Sotiros</h2><div class="dts">{daytrips}</div></div></section>
<section class="cta"><h2>Make Skala Sotiros your base</h2><p>All of this within easy reach of a quiet 2-bedroom apartment with free parking and a walk to the beach.</p>
<div class="btns"><a class="btn btn-pri" href="{AIRBNB}" target="_blank" rel="noopener">Book on Airbnb</a><a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp +30 698 675 7880</a><a class="btn btn-gh" href="blog/where-to-stay-skala-sotiros.html">Where to stay</a></div></section>
<footer><div class="wrap"><div><span class="brand">Casa Valesa</span>Σκάλα Σωτήρος 640 10 · Thassos, Greece<br><a href="tel:+306974482062">+30 697 448 2062</a></div>
<div><a href="index.html">Home</a> · <a href="blog/index.html">Journal</a> · <a href="explore-thassos.html">Explore Thassos</a><br><span style="opacity:.6">EOT Reg. No. 00002524808</span></div></div></footer>
</body></html>'''
open(f"{ROOT}/explore-thassos.html","w").write(doc)
print("explore-thassos.html written;", sum(len(c.get('items',[])) for c in cats),"items across",len(cats),"categories +",len(d.get('day_trips',[])),"day trips")
