"""
nn.py — your neural network library, built on the autograd engine.

This is YOUR file. You'll build `Neuron`, `Layer`, and `MLP` here, one milestone at a
time, with the tutor guiding you. The `Value` engine in `engine.py` is already complete —
you don't edit it; you use it.

Run `/check` in Claude Code whenever you want to test your progress.
"""
import random
from engine import Value


class Neuron:
    def __init__(self, nin):
        # TODO (Milestone 1): create `nin` weights and one bias, each a Value.
        # Initialize each weight randomly, e.g. random.uniform(-1, 1).
        ...

    def __call__(self, x):
        # TODO (Milestone 1): compute tanh(sum(wi * xi for each input) + b) and return it.
        ...

    def parameters(self):
        # TODO (Milestone 1): return this neuron's weights + bias as one list.
        ...


class Layer:
    def __init__(self, nin, nout):
        # TODO (Milestone 2): create `nout` neurons, each taking `nin` inputs.
        ...

    def __call__(self, x):
        # TODO (Milestone 2): run every neuron on x. Return a list of outputs,
        # or a single Value if the layer has only one neuron.
        ...

    def parameters(self):
        # TODO (Milestone 2): return every parameter from every neuron.
        ...


class MLP:
    def __init__(self, nin, nouts):
        # TODO (Milestone 3): build a list of Layers wiring
        # nin -> nouts[0] -> nouts[1] -> ... -> nouts[-1].
        ...

    def __call__(self, x):
        # TODO (Milestone 3): forward x through each layer in turn, return the output.
        ...

    def parameters(self):
        # TODO (Milestone 3): return every parameter from every layer.
        ...
