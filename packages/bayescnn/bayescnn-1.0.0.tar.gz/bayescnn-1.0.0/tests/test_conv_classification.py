"""Tests the Bayesian Convolutional Neural Network for Classification."""

import numpy as np
from sklearn.metrics import f1_score
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
from rich.progress import Progress
import torch

from bayescnn.models import BayesSimpleConvNetwork
from bayescnn.loss import ELBO


def test_model_compiles():
    """Test that the model compiles without error."""
    _ = BayesSimpleConvNetwork(1, 10, 64)
    assert True


def test_model_trains():
    """Test that the model trains and achieves a high F1 score."""
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    model = BayesSimpleConvNetwork(1, 10, 64).to(device)

    criterion = ELBO()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # Load MNIST data
    train = MNIST(root="./data", train=True, download=True, transform=ToTensor())
    test = MNIST(root="./data", train=False, download=True, transform=ToTensor())

    train_loader = DataLoader(train, batch_size=16, shuffle=True)
    test_loader = DataLoader(test, batch_size=16)

    model.train()
    with Progress() as progress:
        num_epochs = 10
        task1 = progress.add_task("[red]Training...", total=num_epochs)
        for _ in range(num_epochs):
            for batch in train_loader:
                features, labels = batch
                features = features.to(device)
                labels = labels.to(device)
                outputs = model(features)
                loss = criterion(model, outputs, labels.flatten(), 1)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            progress.update(
                task1,
                advance=1,
                description=f"[red]Training... Loss: {loss.item()}",
            )

    test_f1s = []
    model.eval()
    for batch in test_loader:
        features, labels = batch
        pred = model(features).cpu().detach().numpy().argmax(axis=1)
        f1 = f1_score(labels.detach().numpy(), pred, average="micro")
        test_f1s.append(f1)

    f1 = np.mean(test_f1s)
    assert f1 > 0.9
