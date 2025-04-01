from bayescnn.layers import BayesLinear
from bayescnn.loss import ELBO

import torch
import numpy as np
from rich.progress import track
from torch import nn, optim
from sklearn.metrics import f1_score


class SimpleLinearModel(nn.Module):
    def __init__(self, input_dim: int, output_dim: int, middle_dim: int):
        super().__init__()
        self.l1 = BayesLinear(input_dim, middle_dim, prior_mean=0.0, prior_std=1.0)
        self.l2 = BayesLinear(middle_dim, output_dim, prior_mean=0.0, prior_std=1.0)
        self.softmax = nn.LogSoftmax(1)

    def forward(self, x):
        x = self.l1(x)
        x = self.l2(x)
        return self.softmax(x)


def test_model_compiles():
    _ = SimpleLinearModel(1, 2, 5)
    assert True


def test_model_trains():
    model = SimpleLinearModel(1, 2, 5)
    criterion = ELBO()

    optimizer = optim.Adam(model.parameters(), lr=0.001)

    x = np.linspace(-10, 10, 100).reshape(-1, 1)
    y = (x > 1).astype(int).flatten()

    x = torch.Tensor(x)
    y = torch.Tensor(y).long()

    losses = []

    for _ in track(range(1000), description="Training Bayesian Linear Model"):
        model.train()
        outputs = model(x)
        loss = criterion(model, outputs, y.flatten(), 1)
        losses.append(loss.item())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    model.eval()
    pred = model(x).detach().numpy().argmax(axis=1)

    f1 = f1_score(y, pred)
    assert f1 > 0.9
