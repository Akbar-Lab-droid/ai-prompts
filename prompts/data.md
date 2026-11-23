# Data & Spreadsheets

5 prompts. See [PROMPTING-GUIDE.md](../PROMPTING-GUIDE.md) for how to write your own.

## Get the Right Spreadsheet Formula

**Purpose:** Get a formula you can paste, with each part explained and the common mistake flagged.

```
I need a spreadsheet formula for this:

What I have: [describe your columns and data]
What I want: [the result]
I'm using [Google Sheets / Excel].

Give me the exact formula I can paste, explain each part in one line, and tell me the common mistake to avoid with it.
```

**Tip:** Paste 3-4 rows of sample data — a formula written blind usually needs two more rounds.

**What to expect:** =SUMIFS(C:C, A:A, "Bandung", B:B, ">=100000") — this sums column C where column A is Bandung and column B is at least 100,000.

## Analyze This Data and Tell Me What Matters

**Purpose:** Turn a pile of numbers into the patterns, the oddity, and the next step.

```
Analyze this data and tell me what actually matters:

[Paste the data or describe it]

Give me: 1) the 3 most important patterns, 2) one thing that looks odd or wrong, 3) what I should do next based on the numbers. Don't just describe the data — interpret it. If the data is too small to trust a conclusion, say so.
```

**Tip:** Say what decision the analysis is for — 'what matters' depends on what you're deciding.

**What to expect:** Pattern 1: sales double on weekends but your ad spend is flat all week — you're under-spending when demand is highest.

## Which Chart Should I Use?

**Purpose:** Pick the chart that makes your point obvious in 3 seconds — and avoid the wrong one.

```
I want to show this data in a chart:

[Describe the data and what you want people to see]

Tell me: the best chart type and why, the second-best option, and one chart type I should NOT use here. Then tell me what to put on each axis and what title to use.
```

**Tip:** A chart should make one point obvious in 3 seconds — if it needs a paragraph to explain, pick a simpler chart.

**What to expect:** Use a bar chart: months on the x-axis, sales on the y-axis. Don't use a pie chart — 12 slices are unreadable.

## Clean Up This Messy Data

**Purpose:** Get a safe step-by-step plan to fix duplicates, wrong formats, and missing values.

```
Help me clean this data:

[Paste a sample or describe the problems — duplicates, wrong formats, missing values]

Give me a step-by-step plan: what to fix first, the exact steps or formulas for each fix, and how to check the result. Keep the original data safe — tell me how to work on a copy.
```

**Tip:** Always work on a copy — cleaning is the step where data gets lost.

**What to expect:** Step 1: duplicate the sheet. Step 2: use Data > Remove duplicates on the email column. Step 3: check the row count before and after.

## Write a SQL Query for Me

**Purpose:** Get a working query with a plain explanation and a tip for large tables.

```
Write a SQL query for this:

Tables: [table names and key columns]
I need: [what you want to get]
Database: [MySQL / Postgres / SQLite].

Give me the query, explain each part briefly, and add one tip for making it faster if the table is large. If my request is ambiguous, ask me one question instead of guessing.
```

**Tip:** List the exact column names — guessing column names is how queries fail silently.

**What to expect:** SELECT name, price FROM products WHERE stock > 0 ORDER BY price DESC LIMIT 10; — this gets the 10 most expensive products that are in stock.
