/* --- SOURCES ---
 * Flags: https://flagpedia.net/download/images
 * Names: https://www.worldometers.info/geography/alphabetical-list-of-countries/
 * Codes: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
 * Capitals: https://en.wikipedia.org/wiki/List_of_national_capitals
 * Continents: https://statisticstimes.com/geography/countries-by-continents.php
 */

/* --- IMPORTS --- */
import COUNTRIES from "./library/countries.js";
import WIKI_PAGES from "./library/wiki.js";

/* --- CONSTANTS --- */
const SITE_TITLE = "195 Countries";
const TABLE_HEADERS = ["Flag", "Name", "Code", "Capital"];
const WIKI_PREFIX = "https://en.wikipedia.org/wiki/";

const siteHeader = document.querySelector("#site-header");
siteHeader.innerHTML = SITE_TITLE;

const table = document.createElement("div");
table.classList.add("table");
siteHeader.insertAdjacentElement("afterend", table);

// store table header indices for later use
const index = {};
for (let i = 1; i < TABLE_HEADERS.length; i++) {
  for (let j = 0; j < COUNTRIES[0].length; j++) {
    if (TABLE_HEADERS[i] == COUNTRIES[0][j]) {
      index[TABLE_HEADERS[i]] = j;
      break;
    }
  }
  console.assert(
    TABLE_HEADERS[i] in index,
    `Missing table header '${TABLE_HEADERS[i]}'.`
  );
}

// create table headers
const flagHeader = document.createElement("div");
flagHeader.classList.add("cell", "table-header");
flagHeader.innerHTML = `<h2>${TABLE_HEADERS[0]}</h2>`;
flagHeader.style.backgroundColor = "aquamarine";
table.append(flagHeader);
for (let i = 1; i < TABLE_HEADERS.length; i++) {
  const header = document.createElement("div");
  header.classList.add("cell", "table-header");
  header.innerHTML = `<h2>${TABLE_HEADERS[i]}</h2>`;
  table.append(header);
}

// create table rows
for (let i = 1; i < COUNTRIES.length; i++) {
  const row = COUNTRIES[i];
  const name = row[index["Name"]];
  const code = row[index["Code"]].toUpperCase();
  const capital = row[index["Capital"]];

  const alt = name;
  // const imagePath = "../db/images/flags/" + code.toLowerCase() + ".png";
  const imagePath = "flags/" + code.toLowerCase() + ".png";

  // FLAG
  const flagData = document.createElement("div");
  flagData.classList.add("cell", "table-data");
  // flagData.innerHTML = `
  //   <figure>
  //     <img src="${imagePath}" alt="${alt}" title="${name}"/>
  //   </figure>
  // `;
  flagData.innerHTML = `
    <img src="${imagePath}" alt="${alt}" title="${name}"/>
  `;
  table.append(flagData);

  // NAME
  const nameData = document.createElement("div");
  nameData.classList.add("cell", "table-data");
  const nameWiki = WIKI_PREFIX + WIKI_PAGES[name][0];
  nameData.innerHTML = `<a class="btn" href="${nameWiki}" target="_blank" rel="noopener noreferrer">${name}</a>`;
  table.append(nameData);

  // CODE
  const codeData = document.createElement("div");
  codeData.classList.add("cell", "table-data");
  codeData.innerHTML = `${code}`;
  table.append(codeData);

  // CAPITAL
  const capitalData = document.createElement("div");
  capitalData.classList.add("cell", "table-data");
  const capitalWiki = WIKI_PREFIX + WIKI_PAGES[name][1];
  capitalData.innerHTML = `<a class="btn" href="${capitalWiki}" target="_blank" rel="noopener noreferrer">${capital}</a>`;
  table.append(capitalData);
}
