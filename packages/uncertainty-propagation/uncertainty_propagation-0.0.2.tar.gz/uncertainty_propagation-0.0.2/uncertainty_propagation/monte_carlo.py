"""
Monte Carlo simulation for the probability integration. See Chapter 2.3.1 for equation references in this file
https://hss-opus.ub.ruhr-uni-bochum.de/opus4/frontdoor/deliver/index/docId/9143/file/diss.pdf
"""

import dataclasses
from typing import Any, Callable

import numpy as np
from experiment_design import random_sampling, variable
from experiment_design.experiment_designer import ExperimentDesigner

from uncertainty_propagation import integrator, utils


@dataclasses.dataclass
class MonteCarloSimulationSettings:
    r"""
    Settings for Monte-Carlo simulation

    :param probability_tolerance: Defines the target accuracy of the estimated failure probability in terms
    of digit precision. This in combination with the target_variation_coefficient and chebyshev_confidence_level
    determines the number of samples used according to Eqs. 2.95 and 2.100. A smaller tolerance will require more
    samples. (Default=1e-4)
    :param batch_size: Maximum number of samples to be calculated in one call. If <=0, all samples are calculated at
    once, Note that for larger number of samples, i.e. a smaller probability tolerance or target_variation_coefficient
    memory errors are possible. (Default=1_000_000)
    :param target_variation_coefficient: Target estimation coefficient of variation (Eq. 2.80). This in combination with
    the target_variation_coefficient and chebyshev_confidence_level determines the number of samples used according to
    Eqs. 2.95 and 2.100. A smaller target variation coefficient will require more samples. (Default=0.1)
    :param chebyshev_confidence_level: Confidence level of the Chebyshev inequality (Eq. 2.100). The number of total
    samples are increased by (1 - chebyshev_confidence_level)**-1. (Default=0)
    :param early_stopping: If True (default), simulation may be interrupted before reaching the estimated sample limit,
    if the estimated probability is larger than zero and the estimated variation_coefficient reaches the target.
    :param sample_generator: ExperimentDesigner to generate samples from. (Default: RandomSamplingDesigner)
    :param sample_generator_kwargs: Any keyword arguments to pass to ExperimentDesigner. (Default = `{"steps": 1}`)
    :param comparison: Boolean-comparison operator. Should generally be either `np.less` or `np.less_equal`, depending
    on whether the calculated probability is defined as :math:`$P(Y<y)$` or :math:`$P(Y \leq y)$`. By default, it uses
    `np.less_equal`to match the CDF definition but for reliability analysis use case, using `np.less` might be more
    appropriate. In reality, since :math:`$P(Y=y) = 0$` for continuous Y, this is not expected to have a significant
    effect.
    """

    probability_tolerance: float = 1e-5
    batch_size: int = 1_000_000
    target_variation_coefficient: float = 0.1
    chebyshev_confidence_level: float = 0  # Eq. 2.100
    early_stopping: bool = True
    sample_generator: ExperimentDesigner = random_sampling.RandomSamplingDesigner(
        exact_correlation=False
    )
    sample_generator_kwargs: dict[str, Any] = dataclasses.field(
        default_factory=lambda: {"steps": 1}
    )
    comparison: Callable[
        [np.ndarray | float, np.ndarray | float], np.ndarray | float
    ] = np.less_equal
    sample_limit: int = dataclasses.field(init=False)

    def __post_init__(self):
        sample_limit = (
            self.target_variation_coefficient**-2 / self.probability_tolerance
        )
        sample_limit /= 1 - self.chebyshev_confidence_level
        self.sample_limit = int(np.ceil(sample_limit))
        if self.batch_size < 1 or self.batch_size > self.sample_limit:
            self.batch_size = self.sample_limit


class MonteCarloSimulation(integrator.ProbabilityIntegrator):
    """
    Monte Carlo simulation for the probability integration. See Chapter 2.3.1 for equation references in this file
    https://hss-opus.ub.ruhr-uni-bochum.de/opus4/frontdoor/deliver/index/docId/9143/file/diss.pdf

    See MonteCarloSimulatorSettings documentation for  further details.

    Further references:
    A. B. Owen (2013). "Monte Carlo theory, methods and examples"
    https://artowen.su.domains/mc/
    """

    use_standard_normal_space: bool = False

    def __init__(self, settings: MonteCarloSimulationSettings | None = None) -> None:
        if settings is None:
            settings = MonteCarloSimulationSettings()
        self.settings = settings
        super(MonteCarloSimulation, self).__init__()

    def _calculate_probability(
        self,
        space: variable.ParameterSpace,
        envelope: Callable[[np.ndarray], tuple[np.ndarray, np.ndarray, np.ndarray]],
        cache: bool = False,
    ) -> tuple[float, float, tuple[np.ndarray | None, np.ndarray | None]]:
        total_samples = 0
        history_x, history_y = None, None
        probability = 0.0
        while total_samples < self.settings.sample_limit:
            batch_size = min(
                self.settings.batch_size, self.settings.sample_limit - total_samples
            )
            x = self.settings.sample_generator.design(
                space,
                batch_size,
                old_sample=history_x,
                **self.settings.sample_generator_kwargs,
            )
            y_min, x_to_cache, y_to_cache = envelope(x)
            history_x, history_y = utils.extend_cache(
                history_x,
                history_y,
                x_to_cache,
                y_to_cache,
                cache_x=True,
                cache_y=cache,
            )
            probability = probability * total_samples + (
                np.sum(self.settings.comparison(y_min, 0.0))
            )
            total_samples += batch_size
            probability /= total_samples
            if self.settings.early_stopping and probability > 0:
                cov = np.sqrt(
                    (1 - probability) / probability / total_samples
                )  # estimate CoV using 2.80 from
                if cov <= self.settings.target_variation_coefficient:
                    break
        std_err = np.sqrt(probability * (1 - probability) / total_samples)
        return probability, std_err, (history_x, history_y)
