"""Tests the Bayesian Convolutional Neural Network for Segmentation."""

import numpy as np
from rich.progress import Progress
from sklearn.metrics import f1_score
from torchvision.datasets import OxfordIIITPet
from torchvision import transforms
import torch
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

from bayescnn.models import BayesUNet
from bayescnn.loss import ELBO


def test_model_compiles():
    """Test that the model compiles without error."""
    _ = BayesUNet(3, 3)
    assert True


def test_model_trains():
    """Test that the model trains and achieves a high F1 score."""
    IMG_SIZE = 128
    BATCH_SIZE = 16

    torch.cuda.empty_cache()
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

    model = BayesUNet(3, 3).to(device)

    criterion = ELBO()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, 0.5)

    t = transforms.Compose(
        [
            transforms.Resize((IMG_SIZE, IMG_SIZE)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )

    t_target = transforms.Compose(
        [
            transforms.Resize((IMG_SIZE, IMG_SIZE)),
            transforms.ToTensor(),
            transforms.Lambda(lambda x: (x * 255 - 1).long()),
        ]
    )

    train = OxfordIIITPet(
        root="./data",
        split="trainval",
        target_types="segmentation",
        transform=t,
        target_transform=t_target,
        download=True,
    )

    test = OxfordIIITPet(
        root="./data",
        split="test",
        target_types="segmentation",
        transform=t,
        target_transform=t_target,
        download=True,
    )

    train_loader = DataLoader(train, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test, batch_size=1)

    model.train()
    with Progress() as progress:
        num_epochs = 10
        task1 = progress.add_task(
            "[green]Training Segmentation Model...", total=num_epochs
        )

        for idx in range(num_epochs):
            mean_loss = []
            for batch in train_loader:
                optimizer.zero_grad()
                features, labels = batch

                # Move everything to the right device
                features = features.to(device)
                labels = labels.to(device)

                outputs = model(features)
                labels = labels.squeeze(1)

                loss = criterion(model, outputs, labels, 0.5)

                loss.backward()
                optimizer.step()
                mean_loss.append(float(loss.item()))

            scheduler.step()

            progress.update(
                task1,
                advance=1,
                description=f"[green]Training Segmentation Model...Loss:{np.mean(mean_loss)}",
            )

            plt.close("all")
            fig, axes = plt.subplots(3, 3)
            f = np.einsum("ijk->jki", features.cpu().detach().numpy()[0])
            o = outputs.cpu().detach().numpy()[0]
            l = labels.cpu().detach().numpy()[0]

            axes[0][0].imshow(f)
            axes[0][2].imshow(l)
            axes[0][1].imshow(o[0])
            axes[1][1].imshow(o[1])
            axes[2][1].imshow(o[2])
            axes[2][2].imshow(o.argmax(axis=0))

            for ax in axes.flatten():
                ax.axis("off")

            plt.tight_layout()
            plt.savefig(f"img/{idx}.png")

    test_f1s = []
    model.eval()
    for batch in test_loader:
        features, labels = batch
        features = features.to(device)
        pred = model(features).cpu().detach().numpy().argmax(axis=1)
        f1 = f1_score(labels.detach().numpy(), pred, average="micro")
        test_f1s.append(f1)

    f1 = np.mean(test_f1s)
    assert f1 > 0.9
