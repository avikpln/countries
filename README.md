# 195 Countries

A browsable reference page listing all 195 countries of the world, with their flags, ISO codes, capital cities, and links to Wikipedia entries for both the country and its capital.

🌍 **[Browse it live](https://avikpln.github.io/countries/)**

---

## Two Implementations

The project contains two independent implementations of the same page, each taking a different approach to rendering the data:

- **`docs/`** — a JavaScript implementation that reads country data from local JavaScript modules and builds the page dynamically in the browser. This is the version served live via GitHub Pages.
- **`static/`** — a Python-based static generator that reads `countries.csv` and produces a fully self-contained `index.html` and `styles.css` with all data baked in at generation time. This version works by opening `index.html` directly in a browser without a server, since it has no runtime dependencies.

---

## Running the Static Version Locally

```bash
cd static
python generate.py
open index.html   # or drag into your browser
```

This reads `countries.csv` and writes `index.html` and `styles.css` into the same directory.

---

## Project Structure

```
countries/
├── docs/                    # Static website
│   ├── flags/               # Country flag images
│   │   ├── ad.png
│   │   ├── ae.png
│   │   ├── ...
│   │   └── zw.png
│   ├── library/             # Country data libraries
│   │   ├── countries.js
│   │   └── wiki.js
│   ├── index.html
│   ├── script.js
│   └── styles.css
├── static/                  # Data generation scripts
│   ├── countries.csv
│   ├── generate.py
│   ├── index.html
│   ├── library.py
│   └── styles.css
├── LICENSE
└── README.md
```

---

## Data Sources

- Flags: [flagpedia.net](https://flagpedia.net/download/images)
- Country names: [worldometers.info](https://www.worldometers.info/geography/alphabetical-list-of-countries/)
- ISO codes: [Wikipedia — ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
- Capitals: [Wikipedia — List of national capitals](https://en.wikipedia.org/wiki/List_of_national_capitals)
- Continents: [statisticstimes.com](https://statisticstimes.com/geography/countries-by-continents.php)

---

## License

[Apache-2.0](LICENSE)
