# Build & train a neural net

**Neural Networks: Zero to Hero - Module 1 - Project 2**
Companion lecture: [The spelled-out intro to neural networks and backpropagation](https://youtu.be/VMj-3S1tku0) by Andrej Karpathy.

You built the autograd engine in Project 1. Now you'll put it to work: build a small neural
network — neurons, layers, an MLP — and a training loop, then watch it actually *learn* a tiny
dataset. With an AI tutor guiding you one step at a time.

## What you need
- Python 3.9+ and `pytest` (`pip install pytest`)
- Any coding agent or AI assistant that can read the project files and run shell commands
  (Claude, Codex, Cursor, or another tool)
- The idea behind Project 1 (the `Value` autograd engine). You don't need your own engine —
  a complete `engine.py` is included here for you to build on. You **don't edit it**.

## How to start
1. Download or clone this project and `cd` into it.
2. Open it with your preferred coding agent.
3. Just say hi. Your tutor takes it from there.

For tool-specific setup notes, see [SETUP.md](./SETUP.md). It covers Claude Code, Codex,
Cursor, and generic coding assistants.

Your code goes in `nn.py` (the network) and `train.py` (the training loop). Ask for a hint
when stuck, ask the tutor to check your work to run the tests, and ask to move on when ready
for the next milestone.

The tests decide when you're done — not the tutor. When they all pass, you've trained a neural
network from scratch. Run `python train.py` any time to watch the loss drop.
