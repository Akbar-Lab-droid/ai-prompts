# AI Prompts

50 ready-to-use prompts that make AI genuinely useful — for coding, writing, learning, business, and everyday life. Each prompt has a clear purpose, copy-paste text, a short tip, and an example of what to expect.

**Browse them all on the web:** https://akbar-lab-droid.github.io/ai-prompts/

## What's inside

| Category | Prompts |
| --- | --- |
| [Coding](prompts/coding.md) | 5 |
| [Writing](prompts/writing.md) | 5 |
| [Learning & Study](prompts/learning.md) | 5 |
| [Analysis & Research](prompts/analysis.md) | 5 |
| [Business & Marketing](prompts/business.md) | 5 |
| [Image Generation](prompts/image.md) | 5 |
| [Data & Spreadsheets](prompts/data.md) | 5 |
| [Productivity](prompts/productivity.md) | 5 |
| [Job & Career](prompts/career.md) | 5 |
| [Everyday Life](prompts/everyday.md) | 5 |

**Total: 50 prompts in 10 categories.**

## How to use

1. Pick a prompt that matches what you need.
2. Copy it (or click **Copy** on the website).
3. Replace the `[bracketed parts]` with your own details — the more specific you are, the better the answer.
4. Paste it into ChatGPT, Claude, Gemini, or any AI chat tool.
5. If the first answer isn't quite right, push back: "shorter", "give me 3 options", "you assumed X, actually it's Y". The second message is usually where the quality comes from.

Read [PROMPTING-GUIDE.md](PROMPTING-GUIDE.md) for how to write your own prompts: role, context, constraints, examples, iteration, and the mistakes to avoid.

## How it works

`prompts.json` is the single source of truth. Everything else is generated from it:

- `prompts/<category>.md` — one Markdown file per category, built by `scripts/build_docs.py`
- `docs/prompts.json` — a copy of the data for the website (GitHub Pages only serves the `docs/` folder)
- `docs/` — the website itself: search, filter by category, and a copy button per prompt

To rebuild the docs after editing `prompts.json`:

```bash
python3 scripts/build_docs.py
python3 scripts/check_prompts.py
```

Both scripts use only the Python standard library — no dependencies to install.

## How to contribute

Found a prompt that doesn't work, or have a better one? Open an issue or a pull request:

1. Edit `prompts.json` (one entry per prompt — see the existing entries for the format).
2. Run `python3 scripts/build_docs.py` and `python3 scripts/check_prompts.py` — both must pass.
3. Keep prompts practical and specific: a clear purpose, real placeholders in `[brackets]`, one short tip, and a short example. No empty hype, no filler.

## License

MIT — use them however you like.
