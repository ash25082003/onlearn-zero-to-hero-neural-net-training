# Curriculum — Build & train a neural net

Goal: on top of the provided autograd engine, the student builds `Neuron`, `Layer`, and `MLP`,
then a training loop that uses gradient descent to fit a tiny dataset. By the end they've trained
a neural network from scratch and watched the loss go down.

Reveal these milestones **one at a time**. Do not show the whole list to the student.

## Milestone 1 — The `Neuron`
A single neuron: it holds a weight (a `Value`) for each input plus one bias `Value`. Calling it on
an input vector computes `tanh(Σ wᵢ·xᵢ + b)`. It can also list its `parameters()` (weights + bias).
*Concept:* a neuron is just a weighted sum squashed by an activation — and every weight is a `Value`,
so gradients flow through it automatically.

## Milestone 2 — The `Layer`
A layer is a list of independent neurons that all see the same input. Calling it returns one output
per neuron. Its `parameters()` are all its neurons' parameters.
*Concept:* width = how many neurons in a layer.

## Milestone 3 — The `MLP`
A multi-layer perceptron stacks layers: the outputs of one layer are the inputs to the next, wiring
`nin → nouts[0] → … → nouts[-1]`. Calling it forwards the input through every layer.
*Concept:* depth = stacked layers; this is a real (tiny) neural network.

## Milestone 4 — The loss
Given the model and the dataset (`xs`, `ys`), compute the predictions and the **mean-squared-error**
loss: `Σ (prediction − target)²`. The loss is a single `Value`, so it carries the whole graph.
*Concept:* the loss is one number that says how wrong the network currently is.

## Milestone 5 — The training loop
Repeat: forward (compute the loss) → zero the gradients → `loss.backward()` → nudge every parameter
`p.data -= lr * p.grad`. Watch the loss fall. This is gradient descent.
*Concept:* learning = repeatedly nudging parameters in the direction that lowers the loss.

Each milestone has tests in `tests/`. A milestone is **done when its tests pass**.

When all tests pass, you've trained a neural network from scratch — the same loop that scales up to
every model in the rest of this course.
