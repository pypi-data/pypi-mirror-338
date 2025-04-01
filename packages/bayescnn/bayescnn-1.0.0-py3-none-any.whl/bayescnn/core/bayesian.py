"""Base class that all Bayesian layers inherit from."""


class Bayesian:
    def __init__(self) -> None:
        # All Bayesian layers need these parameters.
        self.latent_mean = 0
        self.latent_var = 0
        self.prior_mean = 0
        self.prior_std = 0
