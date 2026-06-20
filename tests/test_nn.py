"""
Tests = the source of truth for completion. A milestone is done when its tests pass.
Run with: python -m pytest -q   (or just use /check in Claude Code)
"""
import random
import pytest
from engine import Value
from nn import Neuron, Layer, MLP
from train import xs, ys, loss_fn, train


# ---- Milestone 1: a single Neuron ----
def test_m1_neuron():
    random.seed(1)
    n = Neuron(3)
    # 3 weights + 1 bias
    assert len(n.parameters()) == 4
    out = n([1.0, 2.0, 3.0])
    assert isinstance(out, Value)
    # tanh squashes the output into (-1, 1)
    assert -1.0 < out.data < 1.0


# ---- Milestone 2: a Layer of neurons ----
def test_m2_layer():
    random.seed(1)
    layer = Layer(3, 4)
    outs = layer([1.0, 2.0, 3.0])
    assert len(outs) == 4
    assert all(isinstance(o, Value) for o in outs)
    # 4 neurons * (3 weights + 1 bias) = 16
    assert len(layer.parameters()) == 16


# ---- Milestone 3: a multi-layer perceptron ----
def test_m3_mlp():
    random.seed(1)
    model = MLP(3, [4, 4, 1])
    out = model([1.0, 2.0, 3.0])
    # the final layer has a single neuron, so the output is one Value
    assert isinstance(out, Value)
    # 3->4: 4*(3+1)=16 ; 4->4: 4*(4+1)=20 ; 4->1: 1*(4+1)=5 ; total = 41
    assert len(model.parameters()) == 41


# ---- Milestone 4: the loss ----
def test_m4_loss():
    random.seed(1)
    model = MLP(3, [4, 4, 1])
    loss = loss_fn(model, xs, ys)
    assert isinstance(loss, Value)
    assert loss.data > 0.0


# ---- Milestone 5: training drives the loss down ----
def test_m5_training_converges():
    random.seed(1)
    model = MLP(3, [4, 4, 1])
    start = loss_fn(model, xs, ys).data
    final = train(model, xs, ys, steps=100, lr=0.1)
    assert isinstance(final, float)
    assert final < start          # it learned something
    assert final < 0.1            # and it learned well


if __name__ == "__main__":
    raise SystemExit(pytest.main(["-q", __file__]))
