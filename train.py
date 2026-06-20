"""
train.py — train your neural net.

This is YOUR file. You'll build the loss function (Milestone 4) and the training loop
(Milestone 5) here, then run `python train.py` to watch the loss go down.

The Value engine (engine.py) and your nn.py classes do the heavy lifting.
"""
from nn import MLP

# A tiny dataset: 4 examples, each with 3 inputs, and a target of +1 or -1.
xs = [
    [2.0, 3.0, -1.0],
    [3.0, -1.0, 0.5],
    [0.5, 1.0, 1.0],
    [1.0, 1.0, -1.0],
]
ys = [1.0, -1.0, -1.0, 1.0]


def loss_fn(model, xs, ys):
    # TODO (Milestone 4): run the model on every input, then return the mean-squared-error
    # loss as a single Value.
    ...


def train(model, xs, ys, steps=100, lr=0.1):
    # TODO (Milestone 5): the training loop. For each step:
    #   1. forward:  loss = loss_fn(model, xs, ys)
    #   2. zero grads: set every parameter's .grad back to 0.0
    #   3. backward: loss.backward()
    #   4. update:   for each parameter p, nudge p.data -= lr * p.grad
    # Return the final loss value as a plain float.
    ...


if __name__ == "__main__":
    model = MLP(3, [4, 4, 1])
    final = train(model, xs, ys)
    print(f"final loss: {final}")
