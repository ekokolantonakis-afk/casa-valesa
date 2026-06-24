# Casa Valesa — Holiday Rental Marketing Website (Design Prompt)

> **How to use:** Paste everything below the line into claude.ai's design tool (Claude Artifacts / claude.ai/design).
> **Before pasting, do ONE replacement:** swap every `{{REPO_RAW_BASE}}` for your real public GitHub raw base URL, e.g. `https://raw.githubusercontent.com/youruser/casa-valesa/main/images` (no trailing slash).

---

Build me a complete, production-quality marketing website for a single holiday rental. Output one polished, self-contained responsive site (HTML/CSS, minimal vanilla JS — no framework, no build step). It must look like a boutique villa brand, not a templated listing.

## 1. The property (use exactly)

- **Name:** Casa Valesa
- **What it is:** the entire apartment — 2 bedrooms, 1 bathroom, **sleeps 6**
- **Where:** Skala Sotiros (Σκάλα Σωτήρος 640 10), Thassos, Greece — a quiet seaside village on the calm west coast
- **Features:** walking distance to the beach · sea views · private balcony · family-friendly · fully equipped kitchen · free parking · fast WiFi · authentic Greek village atmosphere · an ideal base to explore the whole island
- **Status:** brand-new listing — **no guest reviews yet**. Promote on photos, location, space and value. **Never invent star ratings, review counts, or testimonials.**
- **Booking:** direct (phone/WhatsApp) + Airbnb
  - Airbnb: `https://www.airbnb.com/rooms/1157207333231807379`
  - Phone / WhatsApp: **+30 697 448 2062**
- **Legal:** EOT Reg. No. **00002524808** (show in footer)

## 2. Market study — design TO this demand (keep it in mind, don't print it verbatim)

- **Who books Thassos:** families & road-trippers driving down from **Romania, Bulgaria, Serbia, North Macedonia** (via Promachonas/Kulata border + Keramoti/Kavala ferry), plus **Germany & UK**; couples wanting quiet authentic beaches; remote workers / longer stays.
- **What they actually want:** safe easy family beaches · free parking · quiet evenings · sea views · space · value · a real (non-touristy) village · a good base to tour the island.
- **Why this matters for the design:** these are practical, value-driven family researchers, mostly **on their phones**. The site must make beach-walk, parking, sleeps-6 and price-confidence obvious in seconds, and feel trustworthy for a no-reviews-yet listing.

## 3. Visual direction — Thassos "emerald isle", NOT the generic AI default

**Do NOT** use the default cream-serif-and-terracotta "AI Mediterranean" look. Ground the design in real Thassos materials: **pine forest meeting turquoise Aegean, white Thassian marble, olive groves, calm west-coast sunsets.**

- **Palette (pick and refine around these named hexes):**
  - Aegean turquoise `#1FA6A0` / deep sea `#0E5C63`
  - Pine green `#2F5E3A` / olive `#7C8B5A`
  - Thassian marble white `#F6F4EF` / warm stone `#E7E1D6`
  - Charcoal text `#23282A`
  - One warm sunset accent for CTAs only: `#E8915B`
- **Typography (opinionated pairing, NOT system defaults):** a confident display face for headings (e.g. **Fraunces** or **Cormorant Garamond** — characterful, not Playfair-default) paired with a clean, highly legible humanist sans for body & UI (e.g. **Inter**, **Hanken Grotesk**, or **Source Sans 3**). Set generous line-height, real type scale, comfortable measure.
- **ONE memorable signature element — choose one and apply it consistently:** a thin **Thassian-marble vein hairline** that divides sections (a subtle veined line/edge), OR a recurring **turquoise→pine gradient "horizon" band** that echoes the west-coast sunset over the sea. Use it as the brand thread across hero, section dividers and the footer. Keep it tasteful and restrained.

## 4. Photos — use the REAL property photos (no stock, no AI images)

All 52 real photos live in a public GitHub repo. Pull hero + gallery strictly from these URLs:

- Base: `{{REPO_RAW_BASE}}`
- Pattern: `{{REPO_RAW_BASE}}/photo-01.jpeg`, `photo-02.jpeg`, … up to `photo-53.jpeg`
- **Important quirks:**
  - **`photo-31` is skipped** — there is no photo-31; do not request it.
  - **`photo-34`, `photo-35`, `photo-39` are `.png`** (not `.jpeg`).
  - Everything else is `.jpeg`.
- That is **52 images total** across the 01–53 range. Use a strong, bright sea-view/balcony/beach shot as the hero; spread the rest across the gallery and the section backgrounds.
- Add descriptive `alt` text per image (room/view) for accessibility & SEO. Lazy-load gallery images. Never substitute stock or generated images.

## 5. Required sections (in order)

1. **Hero** — full-bleed real photo, property name, one warm line ("Your sea-view home in a quiet Thassos village"), village + sleeps-6 tagline, two CTAs: **Book on Airbnb** and **WhatsApp / Call**.
2. **At-a-glance bar** — four quick icons/stats: **Sleeps 6 · 2 Bedrooms · Walk to the beach · Free parking** (plus sea views / fast WiFi if room).
3. **The apartment** — warm description: layout, the two bedrooms, fully equipped kitchen, the private balcony with sea views, who it suits (families, couples, longer stays).
4. **Photo gallery** — full grid of all 52 photos with an accessible **lightbox** (click to enlarge, arrow-key + swipe navigation, ESC to close, focus trap).
5. **Amenities** — clean grouped grid: kitchen, comfort, connectivity (fast WiFi), parking, family-friendly, outdoor/balcony.
6. **The area & map** — Skala Sotiros and the calm west coast: beach walk, quiet evenings, authentic village, and using Casa Valesa as a base to tour the island (mention driving in via Keramoti/Kavala ferry & the northern borders for the Balkan road-trip audience). Embed a simple map locator for Skala Sotiros, Thassos.
7. **Why book direct (trust)** — honest, no-reviews-yet framing: brand-new listing, direct contact with the owner, best rate when you book direct, fast WhatsApp answers, EOT-registered (legit). **No fake stars.**
8. **FAQ** — accessible accordion: How do we get there? Is parking free? How far is the beach? Is it good for families/kids? Is there fast WiFi? Sleeps how many? How do we book / pay? Can we tour the island from here?
9. **Booking block** — prominent: **Book on Airbnb** (link above), **WhatsApp +30 697 448 2062**, **Call +30 697 448 2062**. Make WhatsApp a real `wa.me/306974482062` deep link and the phone a `tel:` link.
10. **Footer** — address (Σκάλα Σωτήρος 640 10, Thassos, Greece), **EOT Reg. No. 00002524808**, contact, Airbnb link, copyright. Carry the signature element through here.

## 6. Multilingual & SEO

- **Primary language: English.** Structure copy and markup so **Greek, Romanian, Bulgarian and German can be added later** easily (clean, translatable text blocks; a visible language-switch placeholder in the header is welcome; use `lang` attributes and avoid baking text into images).
- **SEO:** proper `<title>`, meta description, Open Graph + Twitter card (use a hero photo URL), and JSON-LD structured data (`LodgingBusiness` / `Apartment` with `geo`, `address`, `numberOfRooms`, `occupancy` — but **no `aggregateRating`** since there are no reviews). Target phrases: **"Skala Sotiros apartment"**, **"Thassos family villa"**, "apartment Thassos sea view", "Thassos holiday rental west coast".

## 7. Quality floor (non-negotiable)

- **Mobile-first** and fully responsive (most Balkan family research is on phones) — test the layout at 360px, 768px, 1280px.
- **Keyboard-accessible** throughout: lightbox, accordion, nav, and all CTAs operable by keyboard with visible focus states; semantic HTML; sufficient colour contrast.
- **Fast:** lazy-load images, no heavy libraries, system-friendly fonts loaded efficiently.
- **`prefers-reduced-motion` respected** — disable non-essential animation when set.
- **Tasteful motion only:** gentle fade/parallax on the hero, subtle reveal on scroll. Nothing flashy or distracting.

## 8. Copy tone

Warm, specific, local and helpful — never hard-sell. Speak like a thoughtful host, not a booking platform. Concrete details ("a five-minute stroll to the water", "park right outside, free", "morning coffee on the balcony watching the boats") build more trust than adjectives. Honest about being a fresh listing; confident about location, space and value.

---

**Deliver:** one cohesive, deployable site that a family from Bucharest or Sofia could open on a phone, instantly understand, trust, and tap straight through to Airbnb or WhatsApp to book.
