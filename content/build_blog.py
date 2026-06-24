#!/usr/bin/env python3
# Render content/articles/*.json -> blog/<slug>.html + blog/index.html
import json, glob, os, html, re

ROOT = "/Users/Manos/Desktop/casa-valesa-website"
ART  = f"{ROOT}/content/articles"
BLOG = f"{ROOT}/blog"
SITE = "https://casavalesa.gr"
WA   = "306986757880"
AIRBNB = "https://www.airbnb.com/rooms/1157207333231807379"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Manrope:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

HERO_KEYS = [
 ("sunset","sunset"),("balcony","balcony"),("beach path","beach-path"),("beach-access","beach-path"),
 ("beach","beach"),("dining","dining"),("bedroom","bedroom"),("living","living"),
 ("exterior","exterior"),("village","exterior"),("apartment","living"),
]
import os as _os
CREDITS={}
try: CREDITS=json.load(open(f"{ROOT}/blog/heroes2/CREDITS.json"))
except Exception: pass
def hero_path(slug, hint=None):
    p=f"{ROOT}/blog/heroes2/{slug}.jpg"
    if _os.path.exists(p): return f"heroes2/{slug}.jpg"
    # fallback to scene still
    h=(hint or "").lower()
    for k,f in HERO_KEYS:
        if k in h: return f"heroes/{f}.jpg"
    return "heroes/balcony.jpg"
def hero_credit(slug):
    c=CREDITS.get(slug) or {}
    if not c: return ""
    src=c.get("source",""); auth=c.get("author",""); lic=c.get("license",""); url=c.get("url","")
    if "AI" in src or "Pollinations" in src: return '<p class="imgcredit">Image: AI-generated illustration</p>'
    bits=[x for x in [auth, lic] if x]
    txt=" · ".join(bits) if bits else src
    return f'<p class="imgcredit">Image: <a href="{html.escape(url)}" target="_blank" rel="noopener nofollow">{html.escape(txt)}</a> (via Wikimedia Commons)</p>'

NAV = ('<header class="nav"><div class="inner">'
 '<span class="brandwrap"><a class="brand" href="../index.html">Casa <b>Valesa</b></a><span class=\"loc-badge\"><svg viewBox=\"0 0 24 24\" width=\"15\" height=\"15\" aria-hidden=\"true\"><path fill=\"#1F7A78\" d=\"M3 16c2-5 5-8 9-8s7 3 9 8c-3 2-5.5 2-9 2s-6 0-9-2z\"/><circle cx=\"18\" cy=\"6\" r=\"2.1\" fill=\"#E3A93C\"/><path stroke=\"#7fb9b3\" stroke-width=\"1.3\" fill=\"none\" d=\"M2 20c2 1 4 1 6 0s4-1 6 0 4 1 6 0\"/></svg>Thassos · Greece</span></span>'
 '<nav><a href="index.html" style="text-decoration:none;color:var(--pine);margin-right:18px;font-size:.86rem">Journal</a>'
 '<a class="book" href="../index.html#book">Book now</a></nav></div></header>')

def footer():
    return ('<footer><div class="wrap"><div><span class="brand">Casa Valesa</span>'
      'Σκάλα Σωτήρος 640 10 · Thassos, Greece<br><a href="tel:+306974482062">+30 697 448 2062</a></div>'
      '<div><a href="../index.html">Home</a> · <a href="index.html">Journal</a> · '
      f'<a href="{AIRBNB}" target="_blank" rel="noopener">Airbnb ↗</a><br>'
      '<span style="opacity:.6">EOT Reg. No. 00002524808</span></div></div></footer>')

def cta(lang):
    if lang=="ro":
        return ('<div class="cta"><h3>Sejurul tău liniștit la mare</h3>'
          '<p>Casa Valesa — apartament cu 2 dormitoare (6 persoane) în Skala Sotiros, la pas de plajă, cu parcare gratuită.</p>'
          f'<div class="btns"><a class="btn btn-pri" href="{AIRBNB}" target="_blank" rel="noopener">Rezervă pe Airbnb</a>'
          f'<a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a>'
          '<a class="btn btn-gh" href="where-to-stay-skala-sotiros.html">Unde să stai</a></div></div>')
    return ('<div class="cta"><h3>Your peaceful escape by the sea</h3>'
      '<p>Casa Valesa — an entire 2-bedroom apartment (sleeps 6) in Skala Sotiros: walk to the beach, sea views, free parking.</p>'
      f'<div class="btns"><a class="btn btn-pri" href="{AIRBNB}" target="_blank" rel="noopener">Book on Airbnb</a>'
      f'<a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp +30 698 675 7880</a>'
      '<a class="btn btn-gh" href="where-to-stay-skala-sotiros.html">Where to stay</a></div></div>')

def jsonld(a, lang):
    url=f"{SITE}/blog/{a['slug']}.html"
    img=f"{SITE}/blog/{hero_path(a['slug'],a.get('hero_image'))}"
    art={"@context":"https://schema.org","@type":"Article","headline":a.get("seo_title") or a["h1"],
      "description":a.get("meta_description",""),"image":img,"inLanguage":lang,
      "mainEntityOfPage":url,"author":{"@type":"Organization","name":"Casa Valesa"},
      "publisher":{"@type":"Organization","name":"Casa Valesa"}}
    crumbs={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},
      {"@type":"ListItem","position":2,"name":"Journal","item":f"{SITE}/blog/index.html"},
      {"@type":"ListItem","position":3,"name":a["h1"],"item":url}]}
    blocks=[art,crumbs]
    faqs=a.get("faqs") or []
    if faqs:
        blocks.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
          {"@type":"Question","name":f["q"],"acceptedAnswer":{"@type":"Answer","text":re.sub('<[^>]+>','',f['a'])}} for f in faqs]})
    return "\n".join(f'<script type="application/ld+json">{json.dumps(b,ensure_ascii=False)}</script>' for b in blocks)

def render(a):
    lang = "ro" if a["slug"]=="cazare-thassos-familie" else "en"
    hero = hero_path(a["slug"], a.get("hero_image"))
    crumb_journal = "Jurnal" if lang=="ro" else "Journal"
    secs="".join(f'<h2>{html.escape(s["h2"])}</h2>\n{s["html"]}\n' for s in a.get("sections",[]))
    tk=a.get("key_takeaways") or []
    tkhtml=""
    if tk:
        label="Pe scurt" if lang=="ro" else "Key takeaways"
        tkhtml='<div class="takeaways"><h3>'+label+'</h3><ul>'+''.join(f'<li>{html.escape(t)}</li>' for t in tk)+'</ul></div>'
    faqs=a.get("faqs") or []
    faqhtml=""
    if faqs:
        label="Întrebări frecvente" if lang=="ro" else "Frequently asked questions"
        items="".join(f'<details><summary>{html.escape(f["q"])}</summary><p>{f["a"]}</p></details>' for f in faqs)
        faqhtml=f'<div class="faq"><h2>{label}</h2>{items}</div>'
    rt=a.get("read_minutes","")
    rtl=(f"{rt} min de citit" if lang=="ro" else f"{rt} min read") if rt else ""
    meta_line=" · ".join(x for x in [a.get("silo",""),rtl] if x)
    doc=f'''<!DOCTYPE html><html lang="{lang}"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(a.get("meta_title") or a.get("seo_title") or a["h1"])}</title>
<meta name="description" content="{html.escape(a.get("meta_description",""))}">
<link rel="canonical" href="{SITE}/blog/{a['slug']}.html">
<meta property="og:type" content="article"><meta property="og:title" content="{html.escape(a.get('seo_title') or a['h1'])}">
<meta property="og:description" content="{html.escape(a.get('meta_description',''))}">
<meta property="og:image" content="{SITE}/blog/{hero}"><meta property="og:url" content="{SITE}/blog/{a['slug']}.html">
<meta name="twitter:card" content="summary_large_image">
{FONTS}<link rel="stylesheet" href="blog.css">
{jsonld(a,lang)}
</head><body>
{NAV}
<div class="post-hero"><img src="{hero}" alt="{html.escape(a['h1'])}">
  <div class="wrap"><div class="crumb"><a href="../index.html">Casa Valesa</a> / <a href="index.html">{crumb_journal}</a></div>
  <h1>{html.escape(a['h1'])}</h1><div class="meta">{html.escape(meta_line)}</div></div></div>
<article><div class="wrap">
<div class="lead-wrap">{a.get('intro_html','')}</div>
{hero_credit(a["slug"])}
{tkhtml}
{secs}
{faqhtml}
{cta(lang)}
</div></article>
{footer()}
</body></html>'''
    with open(f"{BLOG}/{a['slug']}.html","w") as f: f.write(doc)
    return lang

# ---- build all ----
arts=[]
for fp in sorted(glob.glob(f"{ART}/*.json")):
    try:
        arts.append(json.load(open(fp)))
    except Exception as e:
        print("SKIP (bad json)",os.path.basename(fp),e)

SILO_ORDER=["Skala Sotiros & West Coast","Where to Stay / Accommodation","Thassos Beaches","Family Holidays","Getting There: Ferries & Driving","Thassos Food","Itineraries","Couples & Romance","Remote Work / Long Stays"]
def silo_key(a):
    s=a.get("silo","Other");
    return (SILO_ORDER.index(s) if s in SILO_ORDER else 99, s)

built=[]
for a in arts:
    lang=render(a); built.append((a,lang))
print(f"rendered {len(built)} articles")

# index
from collections import OrderedDict
groups=OrderedDict()
for a,_ in sorted(built,key=lambda x:silo_key(x[0])):
    groups.setdefault(a.get("silo","Guides"),[]).append(a)
cards_html=""
for silo,items in groups.items():
    cs="".join(
      f'<a class="card" href="{a["slug"]}.html"><img src="{hero_path(a["slug"],a.get("hero_image"))}" alt="{html.escape(a["h1"])}" loading="lazy"><div class="b"><h3>{html.escape(a["h1"])}</h3><p>{html.escape(a.get("meta_description",""))}</p></div></a>'
      for a in items)
    cards_html+=f'<section class="silo"><h2>{html.escape(silo)}</h2><div class="cards">{cs}</div></section>'
idx=f'''<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Thassos Travel Journal — Casa Valesa, Skala Sotiros</title>
<meta name="description" content="Local guides to Thassos: where to stay, the best quiet beaches, family itineraries, ferries and the drive from the Balkans — from Casa Valesa in Skala Sotiros.">
<link rel="canonical" href="{SITE}/blog/index.html">
{FONTS}<link rel="stylesheet" href="blog.css"></head><body>
{NAV}
<div class="idxwrap"><div class="idx-hero"><span class="eyebrow">The journal</span>
<h1>Thassos, by someone who lives it</h1>
<p>Honest local guides to the quiet west coast — where to stay, the calmest beaches, family days out, ferries and the drive down from the Balkans.</p></div>
{cards_html}
</div>
{footer()}
</body></html>'''
open(f"{BLOG}/index.html","w").write(idx)
print("rendered index.html with", len(built), "articles across", len(groups), "silos")
