# Build & train a neural net 🧠

**Neural Networks: Zero to Hero · Module 1 · Project 2**
Companion lecture: [The spelled-out intro to neural networks and backpropagation](https://youtu.be/VMj-3S1tku0) by Andrej Karpathy.

You built the autograd engine in Project 1. Now you'll put it to work: build a small neural
network — neurons, layers, an MLP — and a training loop, then watch it actually *learn* a tiny
dataset. With an AI tutor guiding you one step at a time.

## What you need
- Python 3.9+ and `pytest` (`pip install pytest`)
- [Claude Code](https://claude.com/claude-code)
- The idea behind Project 1 (the `Value` autograd engine). You don't need your own engine —
  a complete `engine.py` is included here for you to build on. You **don't edit it**.

## How to start
1. Download or clone this project and `cd` into it.
2. Open it in Claude Code.
3. Just say hi. Your tutor takes it from there.

Your code goes in `nn.py` (the network) and `train.py` (the training loop). Type `/hint` when
stuck, `/check` to test, `/next` when ready to advance.

The tests decide when you're done — not the tutor. When they all pass, you've trained a neural
network from scratch. Run `python train.py` any time to watch the loss drop.
