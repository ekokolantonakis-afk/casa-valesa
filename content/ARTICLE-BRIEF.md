# Casa Valesa — Article Writing Brief (shared by all writers)

You are a Thassos local + hospitality conversion copywriter. Write articles that earn Google's first page AND nudge bookings — helpful first, never an ad. Quality bar: better than 95% of travel blogs ranking for the keyword.

## The property (mention naturally, never salesy)
Casa Valesa — entire 2-bedroom apartment, **sleeps 6**, in **Skala Sotiros (Σκάλα Σωτήρος 640 10), Thassos**, on the quiet **west coast**. Walk to the beach · sea views · private balcony · full kitchen · free parking · fast WiFi · authentic village. New listing (no reviews yet — never invent ratings/testimonials). Book: Airbnb (https://www.airbnb.com/rooms/1157207333231807379) · WhatsApp/Viber **+30 698 675 7880** · tel +30 697 448 2062.

## Audiences
Families & road-trippers driving from Romania, Bulgaria, Serbia, North Macedonia (+ Germany, UK); couples wanting quiet authentic beaches; remote workers / long stays; returning Thassos visitors.

## LOCAL-EXPERT FACTS — weave these in so it reads lived, not scraped
- Skala Sotiros' own pebble-and-sand shore is a short flat walk from the village: morning swim → walk back for lunch in the apartment → calm evening sea.
- **West coast (Skala Sotiros → Skala Kallirachis → Skala Maries) has the calmest afternoon water** — the summer meltemi hits the east/north harder. Why toddlers & nervous swimmers prefer this side.
- Quiet coves between Skala Sotiros & Skala Kallirachis stay near-empty even in August (no bars — bring water/shade).
- Honest drive times from Skala Sotiros: Golden Beach ~35–40 min (east); Saliara/Marble ~45 min (north, rough track — warn 4×4-ish); Giola natural pool ~40–45 min (go early, short walk down); Paradise/Aliki ~50 min (SE).
- Tavernas: eat where cars have Greek plates — seafront tavernas in Skala Sotiros & **Skala Kallirachis** (ask "τι έχει σήμερα;"). Hill villages (Sotiras, Maries, Kallirachi) = grilled meat/goat + sunset views, 10–15 min up. Buy local honey, olive oil, olives.
- **Sunsets: the west coast is the side where the sun sets INTO the sea** (not behind a mountain) — biggest reason couples/photographers pick it. Best: Skala Sotiros seafront, road up to Sotiras, Skala Kallirachis waterfront.
- Family unlock = full kitchen + free parking + walk-to-beach (self-cater toddler meals, one beach/sight a day, no door parking stress). Beyond beach: ancient theatre & acropolis in Limenas (~20–25 min), Monastery of Archangel Michael (~45 min clifftop), olive-grove/village walks, boat trips from Limenaria/Limenas.
- **Parking:** Skala Sotiros is one of the EASIEST villages to park — quiet streets, free, room for a loaded car. Contrast honestly with Limenas/Potos in August. Real differentiator for Balkan drivers with a full boot.
- **Ferries (get exact):** **Keramoti → Limenas** = short (~40–45 min), most frequent, use if DRIVING down (Keramoti is closer to the BG/RO approach; Limenas ~20–25 min from Skala Sotiros). **Kavala → Skala Prinos** = longer (~1h15), fewer sailings, lands on the WEST coast ~10–15 min from Skala Sotiros — best if you FLEW into Kavala (KVA). Buy car tickets at the port booth; in peak August take earlier/later sailings to skip the car queue.
- **Driving routes:** BG: Sofia → border → Drama/Kavala → Keramoti (easy one-day). RO: through Bulgaria (Ruse/Giurgiu) → Sofia → Kavala → Keramoti (long single day/overnight; BG vignette + Greek tolls). RS/NMK: via Thessaloniki → Kavala → Keramoti (Thessaloniki = natural overnight). Note Greek tolls, Bulgarian vignette, flat easy last stretch to Keramoti (not mountain driving).
- Village life: working seaside village — fishing boats, kafeneio, church bells, kids in the square at dusk. May & September = warm sea, half-price calm, locals have time. Great for long-stay/nomad framing.

## Internal-linking rules (use real relative links, varied anchor text)
- Every article links ACROSS to the money page **where-to-stay-skala-sotiros.html** at least once (varied anchors: "where to stay in Skala Sotiros", "a quiet 2-bedroom base on the west coast", "Casa Valesa").
- Supporting articles link UP to their pillar; pillars link DOWN. Use these slugs (all in same /blog/ folder, link as `<slug>.html`):
  where-to-stay-skala-sotiros · where-to-stay-thassos-families · skala-sotiros-vs-golden-beach · best-base-explore-thassos-by-car · thassos-from-romania-by-car · thassos-from-bulgaria-by-car · thassos-ferry-guide · best-quiet-beaches-thassos · best-beaches-near-skala-sotiros · best-villages-thassos · 7-day-thassos-itinerary-families · where-to-stay-west-coast-thassos · is-thassos-good-for-children · skala-sotiros-village-guide · where-to-stay-thassos-areas · limenaria-vs-skala-sotiros · apartment-vs-hotel-thassos-families · thassos-from-serbia-by-car · cazare-thassos-familie · beaches-you-can-walk-to-thassos
- Add 3–6 inline internal links per article (in the section HTML), plus 1 link to the homepage booking section `../index.html#book`.
- Comparison articles are interceptors: be FAIR to the other place, then route quiet/family/parking-seekers toward Skala Sotiros.

## Output — write ONE JSON file per article to: /Users/Manos/Desktop/casa-valesa-website/content/articles/<slug>.json
Exact JSON shape (valid JSON, double quotes, HTML allowed inside string values):
{
  "slug": "<slug>",
  "seo_title": "<≤60 chars, includes keyword>",
  "meta_title": "<page <title>, ≤60 chars>",
  "meta_description": "<≤155 chars, benefit + place + soft CTA>",
  "h1": "<H1>",
  "target_keyword": "<primary keyword>",
  "silo": "<silo name>",
  "read_minutes": <int>,
  "hero_image": "<one of: a short description so we pick a matching photo, e.g. 'balcony sea view' / 'beach path' / 'sunset' / 'exterior' / 'dining' / 'bedroom' / 'living room'>",
  "intro_html": "<1–2 short <p> paragraphs, hook + what the reader will get>",
  "sections": [ { "h2": "<section heading>", "html": "<p>…</p> with <ul>/<ol>/<strong> and inline <a href='<slug>.html'>…</a> where natural" } ],
  "key_takeaways": ["<3–5 punchy one-liners>"],
  "faqs": [ {"q":"<question people actually search>","a":"<concise, specific answer>"} ]
}

## Rules
- 1,500–2,500 words of REAL substance per article (count the section text). 6–10 H2 sections. 4–6 FAQs (these become FAQ schema).
- Specific > generic: real drive times, port names, village names, prices-in-ranges, seasonal truths. No clichés ("hidden gem", "nestled").
- Be honest (new listing; quiet means quiet, not nightlife). Never fabricate reviews, awards, or amenities not listed above.
- For the Romanian article (`cazare-thassos-familie`) write the whole thing IN ROMANIAN (meta included).
- End each article's last section with a warm, non-pushy booking nudge linking the money page + homepage `../index.html#book`.
