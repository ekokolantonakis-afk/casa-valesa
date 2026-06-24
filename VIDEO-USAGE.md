# Casa Valesa — 45s Commercial: assets & usage prompt

## Files (in this repo)
| Asset | Path | Raw URL |
|-------|------|---------|
| Commercial (1080p, with music, 28 MB) | `video/casa-valesa-commercial.mp4` | `https://raw.githubusercontent.com/ekokolantonakis-afk/casa-valesa/main/video/casa-valesa-commercial.mp4` |
| Poster frame (balcony sea view) | `video/casa-valesa-poster.jpg` | `https://raw.githubusercontent.com/ekokolantonakis-afk/casa-valesa/main/video/casa-valesa-poster.jpg` |
| Vertical 9:16 (Reels/TikTok/Stories, with music, 16 MB) | `video/casa-valesa-vertical.mp4` | `https://raw.githubusercontent.com/ekokolantonakis-afk/casa-valesa/main/video/casa-valesa-vertical.mp4` |

> **Already embedded on casavalesa.gr:** the commercial runs as a muted autoplay loop in the **hero** (poster fallback on mobile + reduced-motion) and again with sound in the **“45 seconds in Skala Sotiros”** section. The 9:16 file is for social only.

> The 45s edit runs: exterior arrival → balcony sea view → living room → bedroom → dining → beach access → beach → sunset, ending on the title card *“CASA VALESA · SKALA SOTIROS • THASSOS · Your peaceful escape by the sea.”* Music: “Sunset Over Casa Valesa”.

---

## Paste-ready prompt for claude.ai/design

> Add the Casa Valesa commercial to the site. Use it in two places:
>
> **1. Hero (primary):** Replace the static hero photo with the commercial as a **muted, autoplay, looping, inline background video** behind the headline and CTAs. It must:
> - Use `muted autoplay loop playsinline` (browsers block sound-on autoplay — keep it muted).
> - Set `poster="https://raw.githubusercontent.com/ekokolantonakis-afk/casa-valesa/main/video/casa-valesa-poster.jpg"` so a still shows instantly while the video loads.
> - Source: `https://raw.githubusercontent.com/ekokolantonakis-afk/casa-valesa/main/video/casa-valesa-commercial.mp4`.
> - Keep the headline, “Sleeps 6 · Walk to the beach” line, and the Book / WhatsApp CTAs fully readable over it (dark gradient overlay).
> - **Respect `prefers-reduced-motion`:** if set, don’t autoplay — show the poster image instead.
> - **Mobile:** on small screens, fall back to the poster image (don’t autoplay a 28 MB file on cellular); offer a play button that opens the video with sound.
>
> **2. “Watch the film” section (with sound):** A dedicated section lower on the page with the same video in a normal `<video controls>` player (sound on when the visitor presses play), poster set, lazy-loaded. Caption: *“45 seconds in Skala Sotiros.”*
>
> Provide a clean play/pause + mute control on the hero for accessibility, with visible keyboard focus.

### Minimal reference markup the design can adapt
```html
<!-- Hero background -->
<video class="hero-video" autoplay muted loop playsinline
       poster="https://raw.githubusercontent.com/ekokolantonakis-afk/casa-valesa/main/video/casa-valesa-poster.jpg">
  <source src="https://raw.githubusercontent.com/ekokolantonakis-afk/casa-valesa/main/video/casa-valesa-commercial.mp4" type="video/mp4">
</video>

<!-- “Watch the film” section -->
<video controls preload="none"
       poster="https://raw.githubusercontent.com/ekokolantonakis-afk/casa-valesa/main/video/casa-valesa-poster.jpg">
  <source src="https://raw.githubusercontent.com/ekokolantonakis-afk/casa-valesa/main/video/casa-valesa-commercial.mp4" type="video/mp4">
</video>
```

### Other uses
- **Open Graph / social preview:** set `og:video` to the commercial URL and `og:image` to the poster.
- **Reels / TikTok / Stories:** ask for a **9:16 vertical cut** (same footage, recropped) — not included here yet.
- **Airbnb / Booking listing:** upload the file directly in the host dashboard (they don’t accept external URLs).
