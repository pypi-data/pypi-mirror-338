from torch import nn

from bayescnn.layers import BayesConv2D, BayesLinear


class BayesSimpleConvNetwork(nn.Module):
    def __init__(self, in_channels: int, out_channels: int, middle_dim: int):
        super().__init__()
        self.conv1 = BayesConv2D(
            in_channels,
            middle_dim,
            kernel_size=(3, 3),
            prior_mean=0.0,
            prior_std=0.1,
        )
        self.act1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=3)
        self.conv2 = BayesConv2D(
            middle_dim,
            middle_dim // 2,
            kernel_size=(3, 3),
            prior_mean=0.0,
            prior_std=0.1,
        )
        self.act2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=3)
        self.flatten = nn.Flatten()
        self.linear = BayesLinear(64, out_channels, prior_mean=0.0, prior_std=1.0)
        self.softmax = nn.LogSoftmax(1)

    def forward(self, x):
        x = self.conv1(x)
        x = self.act1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.act2(x)
        x = self.pool2(x)
        x = self.flatten(x)
        x = self.linear(x)
        return self.softmax(x)
