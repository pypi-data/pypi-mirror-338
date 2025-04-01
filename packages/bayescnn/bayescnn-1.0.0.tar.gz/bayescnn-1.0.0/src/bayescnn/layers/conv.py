"""2D Convolutions with Bayesian Weights."""

import torch
import torch.nn.functional as F
from torch import nn

from bayescnn.core.bayesian import Bayesian


class BayesConv2D(nn.Module, Bayesian):
    """A Bayesian Convolutional Layer in 2D."""

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: tuple[int, int] | int,
        prior_mean: float = 0,
        prior_std: float = 1,
        stride: int = 1,
        padding: int = 0,
        dilation: int = 1,
        bias: bool = True,
    ):
        """Initializes the BayesConv2D layer.

        Args:
            in_channels: Number of channels in the input image.
            out_channels: Number of output channels.
            kernel_size: Kernel size of the convolution.
            prior_mean: Prior mean for the weights.
            prior_std: Prior standard deviation for the weights.
            stride: Stride of the convolution.
            padding: Padding for the convolution.
            dilation: Dilation of the convolution.
            bias: Bias in the network.
        """
        super().__init__()

        # Standard CNN args
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = (
            kernel_size
            if isinstance(kernel_size, tuple)
            else (kernel_size, kernel_size)
        )
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.bias = bias

        # Bayesian args
        self.prior_mean = prior_mean
        self.prior_std = prior_std

        # Set up Parameters
        self.latent_mean = nn.Parameter(
            torch.Tensor(out_channels, in_channels, *self.kernel_size)
        )
        self.latent_rho = nn.Parameter(
            torch.Tensor(out_channels, in_channels, *self.kernel_size)
        )

        if self.bias:
            self.bias_mean = nn.Parameter(torch.Tensor(out_channels))
            self.bias_rho = nn.Parameter(torch.Tensor(out_channels))
        else:
            self.bias_mean, self.bias_rho = None, None

        self.init_parameters()

    def init_parameters(self):
        self.latent_mean.data.normal_(0, 0.1)
        self.latent_rho.data.normal_(-3, 0.1)

        # If we have bias Parameters, initialize them
        if isinstance(self.bias_mean, nn.Parameter) and isinstance(
            self.bias_rho, nn.Parameter
        ):
            self.bias_mean.data.normal_(0, 0.1)
            self.bias_rho.data.normal_(-3, 0.1)

    def forward(self, input: torch.Tensor):
        # Calculate the standard deviations from rho
        self.latent_std = torch.log1p(torch.exp(self.latent_rho))

        if isinstance(self.bias_rho, nn.Parameter):
            self.bias_std = torch.log1p(torch.exp(self.bias_rho))
        else:
            self.bias_std = None

        # Local Reparameterization Trick - calculate mean and std
        mean = F.conv2d(
            input,
            self.latent_mean,
            bias=self.bias_mean if self.bias_mean is not None else None,
            stride=self.stride,
            padding=self.padding,
        )
        std = torch.sqrt(
            1e-16
            * F.conv2d(
                input**2,
                self.latent_std**2,
                bias=self.bias_std**2 if self.bias_std is not None else None,
                stride=self.stride,
                padding=self.padding,
            )
        )

        # Output is mean + std * eps, where eps is a random normal
        eps = torch.randn_like(mean)
        return mean + std * eps


class BayesTransConv2D(nn.Module, Bayesian):
    """A Bayesian Transposed Convolutional Layer in 2D."""

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: tuple[int, int] | int,
        prior_mean: float = 0,
        prior_std: float = 1,
        stride: int = 1,
        padding: int = 0,
        dilation: int = 1,
        bias: bool = True,
    ):
        """Initializes the BayesConv2D layer.

        Args:
            in_channels: Number of channels in the input image.
            out_channels: Number of output channels.
            kernel_size: Kernel size of the convolution.
            prior_mean: Prior mean for the weights.
            prior_std: Prior standard deviation for the weights.
            stride: Stride of the convolution.
            padding: Padding for the convolution.
            dilation: Dilation of the convolution.
            bias: Bias in the network.
        """
        super().__init__()

        # Standard CNN args
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = (
            kernel_size
            if isinstance(kernel_size, tuple)
            else (kernel_size, kernel_size)
        )
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.bias = bias

        # Bayesian args
        self.prior_mean = prior_mean
        self.prior_std = prior_std

        # Set up Parameters
        self.latent_mean = nn.Parameter(
            torch.Tensor(in_channels, out_channels, *self.kernel_size)
        )
        self.latent_rho = nn.Parameter(
            torch.Tensor(in_channels, out_channels, *self.kernel_size)
        )

        if self.bias:
            self.bias_mean = nn.Parameter(torch.Tensor(out_channels))
            self.bias_rho = nn.Parameter(torch.Tensor(out_channels))
        else:
            self.bias_mean, self.bias_rho = None, None

        self.init_parameters()

    def init_parameters(self):
        self.latent_mean.data.normal_(0, 0.1)
        self.latent_rho.data.normal_(-3, 0.1)

        if isinstance(self.bias_mean, nn.Parameter) and isinstance(
            self.bias_rho, nn.Parameter
        ):
            self.bias_mean.data.normal_(0, 0.1)
            self.bias_rho.data.normal_(-3, 0.1)

    def forward(self, input: torch.Tensor):
        self.latent_std = torch.log1p(torch.exp(self.latent_rho))

        if isinstance(self.bias_rho, nn.Parameter):
            self.bias_std = torch.log1p(torch.exp(self.bias_rho))
        else:
            self.bias_std = None

        # Local reparameterization trick
        mean = F.conv_transpose2d(
            input,
            self.latent_mean,
            bias=self.bias_mean if self.bias_mean is not None else None,
            stride=self.stride,
            padding=self.padding,
        )
        std = torch.sqrt(
            1e-16
            * F.conv_transpose2d(
                input**2,
                self.latent_std**2,
                bias=self.bias_std**2 if self.bias_std is not None else None,
                stride=self.stride,
                padding=self.padding,
            )
        )

        eps = torch.randn_like(mean)
        return mean + std * eps
