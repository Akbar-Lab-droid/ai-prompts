// AI Prompts — loads prompts.json (same folder, copied by scripts/build_docs.py),
// renders searchable, filterable cards with a copy button per prompt.

const CATEGORY_TITLES = {
  coding: "Coding",
  writing: "Writing",
  learning: "Learning & Study",
  analysis: "Analysis & Research",
  business: "Business & Marketing",
  image: "Image Generation",
  data: "Data & Spreadsheets",
  productivity: "Productivity",
  career: "Job & Career",
  everyday: "Everyday Life",
};

const state = { prompts: [], query: "", category: "all" };

const cardsEl = document.getElementById("cards");
const emptyEl = document.getElementById("empty");
const countEl = document.getElementById("count");
const searchEl = document.getElementById("search");
const filtersEl = document.getElementById("filters");

function escapeHtml(text) {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function filtered() {
  const q = state.query.trim().toLowerCase();
  return state.prompts.filter((p) => {
    if (state.category !== "all" && p.category !== state.category) return false;
    if (!q) return true;
    const haystack = [
      p.title,
      p.purpose,
      p.prompt,
      p.tips,
      p.example || "",
      CATEGORY_TITLES[p.category] || p.category,
    ].join(" ").toLowerCase();
    return haystack.includes(q);
  });
}

function render() {
  const list = filtered();
  countEl.textContent = `${state.prompts.length} prompts · ${list.length} shown`;
  emptyEl.hidden = list.length > 0;

  cardsEl.innerHTML = list
    .map(
      (p) => `
    <article class="card">
      <span class="category">${escapeHtml(CATEGORY_TITLES[p.category] || p.category)}</span>
      <h2>${escapeHtml(p.title)}</h2>
      <p class="purpose">${escapeHtml(p.purpose)}</p>
      <pre class="prompt">${escapeHtml(p.prompt)}</pre>
      <p class="tip"><strong>Tip:</strong> ${escapeHtml(p.tips)}</p>
      <p class="example"><strong>What to expect:</strong> ${escapeHtml(p.example)}</p>
      <button class="copy" data-id="${escapeHtml(p.id)}" type="button">Copy prompt</button>
    </article>`
    )
    .join("");
}

function renderFilters() {
  const counts = {};
  state.prompts.forEach((p) => {
    counts[p.category] = (counts[p.category] || 0) + 1;
  });
  const buttons = [{ key: "all", label: `All (${state.prompts.length})` }].concat(
    Object.keys(CATEGORY_TITLES)
      .filter((key) => counts[key])
      .map((key) => ({ key, label: `${CATEGORY_TITLES[key]} (${counts[key]})` }))
  );
  filtersEl.innerHTML = buttons
    .map(
      (b) =>
        `<button class="filter${state.category === b.key ? " active" : ""}" data-category="${b.key}" type="button">${escapeHtml(b.label)}</button>`
    )
    .join("");
}

filtersEl.addEventListener("click", (event) => {
  const button = event.target.closest("[data-category]");
  if (!button) return;
  state.category = button.dataset.category;
  renderFilters();
  render();
});

searchEl.addEventListener("input", () => {
  state.query = searchEl.value;
  render();
});

cardsEl.addEventListener("click", async (event) => {
  const button = event.target.closest(".copy");
  if (!button) return;
  const entry = state.prompts.find((p) => p.id === button.dataset.id);
  if (!entry) return;
  try {
    await navigator.clipboard.writeText(entry.prompt);
  } catch (err) {
    // Clipboard API can fail on non-secure contexts; fall back to a selection.
    const area = document.createElement("textarea");
    area.value = entry.prompt;
    document.body.appendChild(area);
    area.select();
    document.execCommand("copy");
    area.remove();
  }
  button.textContent = "Copied ✓";
  button.classList.add("copied");
  setTimeout(() => {
    button.textContent = "Copy prompt";
    button.classList.remove("copied");
  }, 2000);
});

fetch("prompts.json")
  .then((response) => {
    if (!response.ok) throw new Error("prompts.json not found: " + response.status);
    return response.json();
  })
  .then((data) => {
    state.prompts = data.prompts || [];
    renderFilters();
    render();
  })
  .catch((err) => {
    countEl.textContent = "Could not load prompts.";
    emptyEl.hidden = false;
    emptyEl.textContent = "Could not load the prompt data. " + err.message;
  });
