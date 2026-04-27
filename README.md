# Trade Policy Activity Index — Website

Quarto website for the TPA Index (IMF Working Paper 2025/220).  
Authors: Centorrino, Diakantoni, Keck, Ruta, Sztajerowska, Wei.

## Local Development

### Prerequisites
- [Quarto](https://quarto.org/docs/get-started/) ≥ 1.4
- R ≥ 4.3 with packages: `plotly`, `dplyr`, `htmlwidgets`

### Install R packages
```r
install.packages(c("plotly", "dplyr", "htmlwidgets"))
```

### Preview locally
```bash
quarto preview
```

### Render to `docs/`
```bash
quarto render
```

---

## Publish to GitHub Pages

This site is configured to publish from the `docs/` folder on the `main` branch
(same setup used for your previous Quarto → GitHub Pages workflow).

**One-time GitHub setup:**
1. Push this repo to GitHub
2. Go to **Settings → Pages → Source**: set to `Deploy from a branch`, branch `main`, folder `/docs`
3. Or enable the GitHub Actions workflow (`.github/workflows/deploy.yml`) and set Pages source to **GitHub Actions**

**Push to update:**
```bash
quarto render
git add docs
git commit -m "update site"
git push
```

---

## Replacing Placeholder Data

All charts currently use simulated data. To use real data:

1. Place your CSV files in `data/` (filenames match those in `data.qmd`)
2. In `index.qmd` and `explorer.qmd`, replace the `make_tpa()` calls with:
   ```r
   df <- read.csv("data/tpa_global.csv")
   ```
3. Re-render: `quarto render`

---

## Hero Image

The current hero background (`assets/hero-bg.jpg`) is a programmatically generated
placeholder. Replace with a high-quality photo (shipping port, globe, trade floor)
for the final site. Recommended: 1600×900px, dark/moody tone so text is legible.

---

## TODO: Author Links

In `index.qmd`, the authors section has a comment:
```html
<!-- TODO: Replace each .author-name span with <a href="[personal-page-url]"> 
     when personal pages are available -->
```
Update each author's `<span class="author-name">` to an `<a>` tag with their URL.

---

## Site Structure

```
tpa-index/
├── _quarto.yml          # Site config, navbar, theme
├── index.qmd            # Home page (hero + about + findings + chart + downloads + citation)
├── explorer.qmd         # Interactive Data Explorer (4 plotly charts)
├── methodology.qmd      # Methodology explainer (DFM, MIDAS, loadings)
├── data.qmd             # Full downloads + variable definitions + changelog
├── styles/
│   ├── custom.scss      # Main theme (IMF blue palette, Playfair/Source Sans fonts)
│   └── custom.css       # Quarto layout overrides
├── data/                # CSV data files (replace placeholders with real data)
├── assets/
│   ├── hero-bg.jpg      # Hero section background (replace with real photo)
│   └── make_hero.py     # Script that generated the placeholder image
└── .github/workflows/
    └── deploy.yml       # Auto-deploy to GitHub Pages on push to main
```
