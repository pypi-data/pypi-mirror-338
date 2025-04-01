"""Bayesian implementation of U-Net model"""

import typing as tp

import torch
import torch.nn.functional as F
from torch import nn

from bayescnn.layers import BayesConv2D
from bayescnn.layers.conv import BayesTransConv2D


class BayesDoubleConv(nn.Module):
    def __init__(
        self, in_channels: int, out_channels: int, mid_channels: tp.Optional[int] = None
    ) -> None:
        super().__init__()

        if not mid_channels:
            mid_channels = out_channels

        self.conv1 = BayesConv2D(
            in_channels, mid_channels, kernel_size=3, padding=1, bias=False
        )
        self.bn1 = nn.BatchNorm2d(mid_channels)
        self.relu1 = nn.ReLU()
        self.conv2 = BayesConv2D(
            mid_channels, out_channels, kernel_size=3, padding=1, bias=False
        )
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.relu2 = nn.ReLU()

    def forward(self, x):
        return nn.Sequential(
            self.conv1, self.bn1, self.relu1, self.conv2, self.bn2, self.relu2
        )(x)


class BayesDownsample(nn.Module):
    def __init__(self, in_channels: int, out_channels: int) -> None:
        super().__init__()
        self.pool = nn.MaxPool2d(2)
        self.double_conv = BayesDoubleConv(in_channels, out_channels)

    def forward(self, x):
        return nn.Sequential(self.pool, self.double_conv)(x)


class BayesUpsample(nn.Module):
    def __init__(
        self, in_channels: int, out_channels: int, bilinear: bool = False
    ) -> None:
        super().__init__()

        if bilinear:
            self.up = nn.Upsample(scale_factor=2, mode="bilinear", align_corners=True)
            self.double_conv = BayesDoubleConv(
                in_channels, out_channels, in_channels // 2
            )
        else:
            self.up = BayesTransConv2D(
                in_channels, in_channels // 2, kernel_size=2, stride=2
            )
            self.double_conv = BayesDoubleConv(in_channels, out_channels)

    def forward(self, x1, x2):
        x1 = self.up(x1)

        diffy = x2.size()[2] - x1.size()[2]
        diffx = x2.size()[3] - x1.size()[3]

        x1 = F.pad(x1, [diffx // 2, diffx - diffx // 2, diffy // 2, diffy - diffy // 2])

        x = torch.cat([x1, x2], dim=1)

        return self.double_conv(x)


class BayesUNet(nn.Module):
    def __init__(self, in_channels: int, out_channels: int, bilinear: bool = False):
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.bilinear = bilinear

        factor = 2 if bilinear else 1

        self.start = BayesDoubleConv(in_channels, 64)

        self.down1 = BayesDownsample(64, 128)
        self.down2 = BayesDownsample(128, 256)
        self.down3 = BayesDownsample(256, 512)
        self.down4 = BayesDownsample(512, 1024)
        self.up1 = BayesUpsample(1024, 512 // factor)
        self.up2 = BayesUpsample(512, 256 // factor)
        self.up3 = BayesUpsample(256, 128 // factor)
        self.up4 = BayesUpsample(128, 64)
        self.outconv = BayesConv2D(64, out_channels, kernel_size=(1, 1))
        self.outact = nn.LogSoftmax(1)

    def forward(self, x):
        x1 = self.start(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        x = self.up1(x5, x4)
        x = self.up2(x, x3)
        x = self.up3(x, x2)
        x = self.up4(x, x1)
        x = self.outconv(x)
        return self.outact(x)
