import { test } from "node:test";
import assert from "node:assert/strict";
import vm from "node:vm";
import { renderHtml } from "../src/index.js";
import { CITY_PRESETS, getAllCitiesData } from "../src/cities_data.js";

function renderPage() {
  return renderHtml("twin-cities", getAllCitiesData({}));
}

function extractScript(html) {
  const start = html.indexOf("<script>");
  const end = html.lastIndexOf("</script>");
  assert.ok(start >= 0 && end > start, "page has a script block");
  return html.slice(start + "<script>".length, end);
}

test("dashboard script block is not terminated early by its own contents", () => {
  const html = renderPage();
  // Exactly one close tag: the real one. A stray literal close sequence
  // inside the script (e.g. in a comment) makes browsers drop every
  // handler defined after it, including switchCity.
  assert.equal(html.split("</script>").length - 1, 1);
  assert.doesNotThrow(() => new vm.Script(extractScript(html)), "inline script must parse");
});

test("every market preset renders a select button wired to switchCity", () => {
  const html = renderPage();
  for (const p of CITY_PRESETS) {
    assert.ok(html.includes(`data-city="${p.id}"`), `chip for ${p.id}`);
    assert.ok(html.includes(`onclick="switchCity('${p.id}')"`), `onclick for ${p.id}`);
  }
});

// Minimal DOM stub recording what switchCity touches.
function makeDom(citiesData) {
  const elements = new Map();
  const el = (id) => {
    if (!elements.has(id)) {
      elements.set(id, {
        id, textContent: "", innerHTML: "", title: "", disabled: false,
        style: {}, dataset: {},
        classList: { toggle() {}, add() {}, remove() {} },
        setAttribute() {}, getAttribute() { return null; },
        appendChild() {}, remove() {},
      });
    }
    return elements.get(id);
  };
  const chips = Object.keys(citiesData).map((id) => ({
    _city: id, attrs: {},
    classList: { toggle(cls, on) { this.lastToggle = [cls, on]; }, add() {}, remove() {} },
    setAttribute(k, v) { this.attrs[k] = v; },
    getAttribute(k) { return k === "data-city" ? this._city : null; },
  }));
  const document = {
    getElementById: el,
    querySelectorAll: (sel) => (sel === ".city-chip" ? chips : []),
    querySelector: () => el("header-actions"),
    createElement: () => el("created-" + Math.random()),
    title: "",
  };
  const window = {
    location: new URL("https://example.test/"),
    history: { replaceState() {} },
    addEventListener() {},
  };
  document.addEventListener = () => {};
  return { document, window, chips, el };
}

test("switchCity activates the clicked market chip and retitles the page", () => {
  const script = extractScript(renderPage());
  const citiesData = JSON.parse(
    script.match(/const CITIES_DATA = (\{.*?\});\n/s)[1].replace(/\\u003c/g, "<"),
  );
  const { document, window, chips, el } = makeDom(citiesData);
  const ctx = vm.createContext({
    document, window,
    localStorage: { setItem() {}, getItem: () => null },
    URL, console,
  });
  vm.runInContext(script, ctx);
  assert.equal(typeof ctx.switchCity, "function", "switchCity is defined globally");

  ctx.switchCity("austin");
  const austin = chips.find((c) => c._city === "austin");
  const twin = chips.find((c) => c._city === "twin-cities");
  assert.deepEqual(austin.classList.lastToggle, ["active", true]);
  assert.deepEqual(twin.classList.lastToggle, ["active", false]);
  assert.equal(austin.attrs["aria-selected"], "true");
  assert.match(el("pageTitle").textContent, /Austin/);
  assert.ok(Number(el("kpiScheduled").textContent) >= 0);

  // Hyphenated ids and the previously-working default both resolve.
  ctx.switchCity("champaign-urbana");
  assert.match(el("pageTitle").textContent, /Champaign/);
  ctx.switchCity("twin-cities");
  assert.match(el("pageTitle").textContent, /Minneapolis/);

  // The footer rewrite must keep the agency link's id, or the next
  // switchCity throws on getElementById('footerAgencyLink').
  assert.match(el("footerText").innerHTML, /id="footerAgencyLink"/);
});
