# How to Write a Good Prompt

A good prompt is not magic. It is a clear brief: who the AI should be, what you want, what good looks like, and what to avoid. This guide covers the parts that actually change the result.

## The 5 parts of a good prompt

### 1. Role — who should the AI be?

Give the AI a job, not a personality. "You are a senior Python developer" works better than "You are a helpful assistant" because it sets the standard of the answer.

- Good: "Review this code as if you're a senior developer on my team."
- Bad: "Look at my code."

### 2. Context — what does the AI need to know?

Paste the real material: the code, the text, the numbers, the audience. An AI guessing at your situation gives generic answers.

- Good: "My audience is small shop owners in Bandung who have never run ads."
- Bad: "Write marketing copy." (For whom? About what?)

### 3. Task — what exactly should it do?

One task per prompt. Use a verb: explain, compare, rewrite, list, draft. If you ask for three things at once, you get three shallow answers.

- Good: "Rewrite this paragraph so a 14-year-old can understand it."
- Bad: "Make this better." (Better how? Shorter? Funnier? More formal?)

### 4. Constraints — what are the limits?

Length, format, tone, what to avoid. Constraints are what turn a generic answer into a usable one.

- Good: "Under 150 words. No exclamation marks. End with one clear question."
- Bad: "Keep it short." (How short is short?)

### 5. Example — what does good look like?

One example beats a paragraph of description. Show the format you want, even roughly.

- Good: "Format the answer like this: Problem — ... Fix — ... Check — ..."
- Bad: "Format it nicely."

## A simple formula

```
Role: You are a [job/expert].
Context: [the facts, the material, the audience].
Task: [one clear verb + what to produce].
Constraints: [length, format, tone, what to avoid].
Example: [what good looks like, if you have one].
```

## Iterate — the first answer is a draft

Almost nobody gets the best answer on the first try. That is normal. The second message is where the quality comes from:

1. **Narrow it down:** "That's too long. Give me the 3 most important points."
2. **Correct it:** "You assumed X, but actually it's Y. Try again with that."
3. **Ask for the opposite:** "Now argue the other side."
4. **Ask for a different format:** "Same content, but as a table."

If the answer is wrong, say what is wrong. "That's not right" helps less than "The price is wrong — it's 243,000, not 300,000."

## Common mistakes

| Mistake | Why it fails | Fix |
|---|---|---|
| No context | The AI guesses, and the guess is generic | Paste the real text, numbers, or code |
| Too many tasks at once | Every part gets a shallow answer | One prompt, one job |
| Vague words ("better", "nice", "good") | The AI can't measure vague | Say what "better" means: shorter, simpler, more specific |
| No format | You get a wall of text you have to rework | Ask for bullets, a table, or a word count |
| Accepting the first answer | The first draft is rarely the best one | Push back once or twice — that's where quality comes from |
| Trusting everything | AI makes up facts, prices, and quotes | Check numbers and claims against a real source |

## Good vs bad — same request, different prompt

**Bad prompt:**

> Write something about WiFi.

Result: a generic paragraph you could find anywhere.

**Good prompt:**

> Write a 3-sentence Instagram caption for XL Home FWA WiFi in Bandung. Audience: families who work from home and hate slow WiFi. Key fact: 100 Mbps for Rp243,000/month, no cable, free installation. Tone: friendly, direct. End with a call to action to WhatsApp 0877-1570-6320.

Result: something you can actually post.

## One last thing

A prompt is a skill, not a trick. The people who get the most out of AI are not the ones with secret magic words — they are the ones who explain their problem clearly, give real context, and keep pushing back until the answer is actually useful. Start with the prompts in this repo, then change them to fit your own work. That is the whole point.
