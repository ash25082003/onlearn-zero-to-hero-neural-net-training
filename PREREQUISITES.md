# Module 0 — Prerequisites (taught inline)

Before building the network, the learner needs to be comfortable with the autograd engine they'll
build on. Run a quick **diagnostic** at the very first session, then teach only the warm-ups they
actually need. A confident learner can skip straight to Milestone 1.

## The diagnostic (ask conversationally, don't make it feel like a test)

Find out, in a friendly back-and-forth:

1. **The engine** — do they get what a `Value` is, and what `backward()` does (fills in `.grad` for
   every value that fed into the result)? They don't need to have done Project 1, but they need this idea.
2. **Python lists & classes** — are they comfortable with a `class` that stores a list of things and
   loops over them (e.g. a list comprehension)?

Based on their answers, route them:
- Solid on both → go straight to Milestone 1.
- Shaky on one → do just that warm-up, then continue.
- New to both → do both warm-ups first.

## Warm-up A — What `backward()` gives you (only if needed)
Goal: intuition, not rigor. Build one tiny expression with the provided engine, e.g.
`a = Value(2.0); b = Value(-3.0); c = a * b; c.backward()`, and look at `a.grad` / `b.grad`. The
point: after `backward()`, every input knows how it affects the output. That's all a neuron needs.

## Warm-up B — A class that holds a list (only if needed)
Goal: comfort with the pattern we'll reuse three times. Have them write a tiny class that stores a
list (e.g. a `Bag` holding several items) and has a method that loops over them. `Neuron`, `Layer`,
and `MLP` are all just this pattern with `Value`s inside.

When the needed warm-ups are done (or skipped), continue into the main CURRICULUM.md.
