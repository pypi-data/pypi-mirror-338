import math
import torch
import torch.nn.functional as F
from torch import nn

from bayescnn.core.bayesian import Bayesian


class BayesLinear(nn.Module, Bayesian):
    def __init__(
        self,
        in_features: int,
        out_features: int,
        prior_mean: float,
        prior_std: float,
        bias: bool = True,
    ) -> None:
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.bias = bias

        self.prior_mean = prior_mean
        self.prior_std = prior_std

        self.latent_mean = nn.Parameter(torch.Tensor(out_features, in_features))
        self.latent_rho = nn.Parameter(torch.Tensor(out_features, in_features))

        if self.bias:
            self.bias_mean = nn.Parameter(torch.Tensor(out_features))
            self.bias_rho = nn.Parameter(torch.Tensor(out_features))

        self.init_parameters()

    def init_parameters(self):
        self.latent_mean.data.normal_(0, 0.1)
        self.latent_rho.data.normal_(-3, 0.1)

        if self.bias:
            self.bias_mean.data.normal_(0, 0.1)
            self.bias_rho.data.normal_(-3, 0.1)

    def forward(self, input: torch.Tensor):
        # Calculate variance
        self.latent_std = torch.log1p(torch.exp(self.latent_rho))

        if self.bias:
            self.bias_std = torch.log1p(torch.exp(self.bias_rho))
        else:
            self.bias_std = None

        # Local Reparameterisation Trick
        mean = F.linear(input, self.latent_mean, self.bias_mean)
        std = torch.sqrt(
            1e-16
            + F.linear(
                input**2,
                self.latent_std**2,
                self.bias_std**2 if self.bias_std is not None else None,
            )
        )

        eps = torch.randn_like(mean)
        return mean + std * eps
