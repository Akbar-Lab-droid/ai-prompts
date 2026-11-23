# Coding

5 prompts. See [PROMPTING-GUIDE.md](../PROMPTING-GUIDE.md) for how to write your own.

## Debug an Error Message

**Purpose:** Get a clear explanation of an error and a fix you can actually try.

```
I ran into this error and I can't figure out what's wrong:

[Paste the full error message]

Here's the code around it:

[Paste the relevant code]

Explain in plain language: 1) what the error actually means, 2) the most likely cause, 3) the smallest fix to try first, and 4) how to check whether it worked. If there are two possible causes, tell me how to tell them apart.
```

**Tip:** Paste the full error, not just the last line — the lines above it usually say where it really started.

**What to expect:** The error means Python can't find the module 'requests' — it's not installed in this environment. Most likely cause: you installed it for a different Python version. Fix: run pip install requests in the same terminal, then re-run the script.

## Review My Code Like a Senior Teammate

**Purpose:** Get an honest, specific code review that finds real problems, not vague praise.

```
Review this code as if you're a senior developer on my team. Be honest and specific:

[Paste your code]

Check for: 1) bugs or edge cases that will break, 2) parts that are hard to read and how to simplify them, 3) security or performance problems, 4) anything that doesn't follow normal conventions for this language. For each issue, show the line, explain why it matters, and suggest the fix. End with the 3 most important changes, in order.
```

**Tip:** Say what the code is supposed to do first — a review is much better when the goal is clear.

**What to expect:** 1) Line 14: user input is used directly in the SQL query — this allows SQL injection. Use a parameterized query instead. 2) The loop runs a database query on every iteration — fetch the data once before the loop...

## Refactor for Readability

**Purpose:** Make working code easier to read and change later, without breaking what it does.

```
Refactor this code so it's easier to read and change later, without changing what it does:

[Paste your code]

Rules: keep the same behavior and the same function names. Break long functions into smaller ones with clear names, remove duplicated logic, and replace magic numbers with named constants. Show the full refactored code, then list what you changed and why — in one line per change.
```

**Tip:** If the code works but is messy, say so — refactoring working code is safer than rewriting it.

**What to expect:** Extracted the discount calculation into calculate_discount() so the checkout function drops from 60 lines to 25. Replaced the magic number 0.1 with DISCOUNT_RATE = 0.1 at the top of the file.

## Write Tests for This Function

**Purpose:** Generate tests that cover the normal case, the edge cases, and bad input.

```
Write tests for this function:

[Paste the function]

Cover: the normal case, at least two edge cases (empty input, zero, the biggest realistic value), and one case where the input is invalid. Use [pytest / Jest / your framework]. For each test, add a one-line comment saying what it's checking. If something can't be tested easily, say so and explain why.
```

**Tip:** Name the testing framework you use — test code looks very different between pytest and Jest.

**What to expect:** test_add_empty_list: checks that add([]) returns 0 instead of crashing. test_add_negative: checks that add([-1, -2]) returns -3.

## Explain This Code in Plain Words

**Purpose:** Understand code you didn't write (or wrote long ago) line by line.

```
Explain this code to me line by line, in plain words, as if I'm learning the language:

[Paste the code]

For each part, say what it does and why it's there. Skip the obvious lines. At the end, summarize in 2-3 sentences what the whole thing does and what I should remember about it.
```

**Tip:** Mention the language and your level — the explanation changes a lot between beginner and intermediate.

**What to expect:** Line 3 loops over every user in the list. Line 4 checks if the user is active. Overall, this function filters out inactive users before sending the email.
