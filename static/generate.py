# --- SOURCES --- #
# Flags: https://flagpedia.net/download/images
# Names: https://www.worldometers.info/geography/alphabetical-list-of-countries/
# Codes: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
# Capitals: https://en.wikipedia.org/wiki/List_of_national_capitals
# Continents: https://statisticstimes.com/geography/countries-by-continents.php

# --- IMPORTS --- #
import csv
# from PIL import Image  # to extract image dimensions # REMOVEME: Not needed anymore.

from library import WIKI_PAGES;

# --- CONSTANTS --- #
HTML_OUTPUT_FILE_PATH = 'index.html'
DUMP_CSS = True
CSS_OUTPUT_FILE_PATH = 'styles.css'
COUNTRIES_FILE_PATH = 'countries.csv'

LANG = 'en-US'
DIR = 'ltr'
TITLE = 'Flags'
CHARSET = 'UTF-8'
HEADER = '195 Countries'

BUTTON_CLS = "btn"
GRID_CLS = "grid"
GRID_ITEM_CLS = "grid-item"
GRID_ITEM_HEADER_CLS = "grid-header"
GRID_ITEM_DATA_CLS = "grid-data"

TABLE_HEADERS = ('Flag', 'Name', 'Code', 'Capital')

WIKI_PREFIX = 'https://en.wikipedia.org/wiki/'

# --- GLOBALS --- #
# open countries (csv) file for reading
with open(COUNTRIES_FILE_PATH, 'r', encoding=CHARSET) as incsvfp:
    reader = csv.reader(incsvfp)
    input_headers = next(reader)
    input_rows = [row for row in reader if len(row) > 0]
lowercase_input_headers = [header.lower() for header in input_headers]

# --- HELPER FUNCTIONS --- #
def get_header_index(header):  # NOTE case insensitive
    # global lowercase_table_headers
    try:
        index = lowercase_input_headers.index(header.lower())
    except ValueError:
        raise KeyError(f'{header} header not found')
    return index

def get_source_by_code(code):  # h120
    return '../db/images/flags/' + code.lower() + '.png'

# --- PREPROCESSING --- #
# store table header indices for later use
index = dict()
for header in TABLE_HEADERS[1:]:  # 0 is reserved for 'Flag'
    index[header] = get_header_index(header)

# --- OPENING --- #
html = \
f'''<!DOCTYPE html>
<html lang="{LANG}" dir="{DIR}">
  <head>
    <title>{TITLE}</title>
    <meta charset="{CHARSET}">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{CSS_OUTPUT_FILE_PATH}">
  </head>

  <body>
  <main>
    <h1>{HEADER}</h1>

    <div class="{GRID_CLS}">'''

# --- TABLE: HEADERS --- #

# flags header
flags_header = TABLE_HEADERS[0]
html += \
f'''
      <div class="{GRID_ITEM_CLS} {GRID_ITEM_HEADER_CLS}"><h2>{flags_header}</h2></div>'''

# info headers
for header in TABLE_HEADERS[1:]:
    html += \
f'''
      <div class="{GRID_ITEM_CLS} {GRID_ITEM_HEADER_CLS}"><h2>{header}</h2></div>'''

# --- TABLE: ROWS --- #
for row in input_rows:
    name = row[index['Name']]
    code = row[index['Code']].upper()
    capital = row[index['Capital']]

    alt = name
    src = get_source_by_code(code)
    # width, height = Image.open(src).size

    # FLAG
    html += \
f'''

      <!-- {name.upper()} -->
      <div class="{GRID_ITEM_CLS} {GRID_ITEM_DATA_CLS}">
        <figure>
          <img src="{src}" alt="{alt}" title="{name}"/>
        </figure>
      </div>'''

    # NAME
    href = WIKI_PREFIX + WIKI_PAGES[name][0]
    content = f'<a class="{BUTTON_CLS}" href="{href}" target="_blank" rel="noopener noreferrer">{name}</a>'
    html += \
f'''
      <div class="{GRID_ITEM_CLS} {GRID_ITEM_DATA_CLS}">{content}</div>'''

    # CODE
    html += \
f'''
      <div class="{GRID_ITEM_CLS} {GRID_ITEM_DATA_CLS}">{code}</div>'''

    # CAPITAL
    href = WIKI_PREFIX + WIKI_PAGES[name][1]
    content = f'<a class="{BUTTON_CLS}" href="{href}" target="_blank" rel="noopener noreferrer">{capital}</a>'
    html += \
f'''
      <div class="{GRID_ITEM_CLS} {GRID_ITEM_DATA_CLS}">{content}</div>'''

# --- CLOSING --- #
html += \
f'''
    </div>

  </main>
  </body>
</html>'''

# --- DUMP HTML --- #
with open(HTML_OUTPUT_FILE_PATH, 'w', encoding=CHARSET) as outfp:
  outfp.write(html)

# --- CSS --- #
css = \
'''/* MAIN */
main {
  border: 5px solid indigo;
  background: honeydew;
  padding: 5px;
}

/* H1 */
h1 {
  color: indigo;
  text-align: center;
  font-family: cursive;
  font-size: 70px;
  line-height: 1;
}

/* DIV */
div {
  background: white;
}

/* A */
/* a,
a:hover,
a:focus,
a:active {
  color: darkblue;
  text-decoration: none;
  border: 1px groove darkblue;
  padding: 5px;
} */
a.btn {
  color: aliceblue;
  background: royalblue;
  text-decoration: none;
  padding: 8px;
  border: 1px solid blue;
  border-radius: 4px;
  display: inline-block;
}
a.btn:hover {
  color: gold;
}

/* FIGURE, IMG */
figure {
  /* border: 1px solid black; */
  /* padding: 5px; */
  width: 200px;

  /* text-align: center; */
  display: flex;
  justify-content: center;
  align-items: center;
}
img {
  border: 1px solid black;
  background: white;
  /* padding: 5px; */
  height: 120px;
}

/* GRID */
.grid {
  border: 1px solid black;
  background: royalblue;
  padding: 5px;

  display: grid;
  grid-template-columns: repeat(''' \
    + str(len(TABLE_HEADERS)) + ''', 1fr);''' \
    + \
'''
  grid-template-rows: auto;
  grid-gap: 5px;
}

/* GRID-ITEM */
.grid-item {
  border: 1px solid black;
  padding: 5px;

  /* display: grid; */
  display: flex;
  align-items: center;
  justify-content: center;
}
.grid-item.grid-header {
  border: 1px solid black;
  background: aqua;
  font-family: cursive;
  font-size: 120%;
}
.grid-item.grid-data {
  border: 1px solid black;
  background: aliceblue;
  font-family: Verdana, sans-serif;
  font-size: 100%;
}
'''

# --- DUMP CSS --- #
if DUMP_CSS:
  with open(CSS_OUTPUT_FILE_PATH, 'w') as outfp:
    outfp.write(css)
