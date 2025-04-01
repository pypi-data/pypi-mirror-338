"""Loss functions for Bayesian Neural Networks."""

import torch
from torch import nn
from bayescnn.core import Bayesian
from enum import Enum


class Reduction(Enum):
    MEAN = 1
    SUM = 2
    NONE = 3


class KL_Divergence(nn.Module):
    def __init__(self, reduction: Reduction = Reduction.MEAN) -> None:
        super().__init__()
        self.reduction = reduction

    @staticmethod
    def single_kl_divergence(q_mean, q_var, p_mean, p_var) -> torch.Tensor:
        """kullback-leibler (kl) divergence between two multivariate normal distributions.

        here we assume the covariance matricies are diagonal - simplifying the equation.

        args:
            q_mean ([todo:parameter]): latent space mean
            log_q_var ([todo:parameter]): log latent space variance
            p_mean ([todo:parameter]): prior mean
            log_p_var ([todo:parameter]): log prior variance
        """
        kl = (
            2 * torch.log(p_var / q_var)
            - 1
            + (q_var / p_var).pow(2)
            + ((p_mean - q_mean) / p_var).pow(2)
        )
        return 0.5 * kl.sum()

    def forward(
        self, model: nn.Module, reduction: Reduction = Reduction.MEAN
    ) -> torch.Tensor:
        device = next(model.parameters()).device
        # Initialise counters
        kl_sum = torch.Tensor([0]).to(device)
        n = torch.Tensor([0]).to(device)

        # Iterate through the model
        for m in model.modules():
            # Only calculate KL Divergence for modules that can calcualte it.
            if isinstance(m, Bayesian):
                kl = self.single_kl_divergence(
                    m.latent_mean,
                    m.latent_std,
                    m.prior_mean,
                    m.prior_std,
                )

                kl_sum += kl
                n += len(m.latent_mean.flatten())

                # If we have a bias term, calculate the loss here as well.
                if m.bias:
                    kl = self.single_kl_divergence(
                        m.bias_mean,
                        m.bias_std,
                        m.prior_mean,
                        m.prior_std,
                    )

                    kl_sum += kl
                    n += len(m.bias_mean.flatten())

        # Edge case: no Bayesian layers
        if n == 0:
            return kl_sum

        # Match over reduction enum
        match reduction:
            case Reduction.MEAN:
                return kl_sum / n
            case _:
                return kl_sum


class ELBO(nn.Module):
    """ELBO (Evidence Lower Bound) is a loss function mixing how well the model's
    predictions match the true labels as well as ensuring that the weight distributions
    are of standard normal form."""

    def __init__(self, reduction: Reduction = Reduction.MEAN) -> None:
        super().__init__()
        self.reduction = reduction

        # NLLoss reduction is string either none, mean or sum.
        self.log_loss = nn.NLLLoss(reduction=reduction.name.lower())
        self.kl_loss = KL_Divergence(reduction=reduction)

    def forward(
        self,
        model: nn.Module,
        prediction: torch.Tensor,
        target: torch.Tensor,
        beta: float,
    ) -> torch.Tensor:
        """Calculate the ELBO loss for a given sample.

        Beta controls the weight of the KL divergence compared to the negative
        log likelihood on the loss function - a higher KL divergence can prevent
        overfitting, especially when the dataset is small.

        Args:
            model: Model to calculate the loss for
            prediction: Prediction made by the model.
            target: Ground truth of the model
            beta: Weighting parameter towards the KL divergence

        Returns:
            torch.Tensor: Total ELBO Loss for the model
        """
        return self.log_loss(prediction, target) + (
            beta * self.kl_loss(model, reduction=self.reduction)
        )
