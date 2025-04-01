from abc import ABC
from typing import Dict, Optional

from bears.util import Registry
from fmcore.prompt_tuner.types.enums.optimizer_enums import OptimizerType, OptimizerMetricType
from fmcore.types.typed import MutableTyped


class BaseOptimizerParams(MutableTyped):
    """
    Base class for optimizer parameters.

    Attributes:
        optimizer_metric (OptimizerMetricType): The metric used for optimization.
    """

    optimizer_metric: OptimizerMetricType


class BaseOptimizerConfig(MutableTyped, Registry, ABC):
    """
    Abstract base class for optimizer configurations.

    This class provides a registry mechanism for dynamically retrieving optimizer configurations
    based on their type.

    Attributes:
        optimizer_type (OptimizerType): The type of optimizer.
    """

    optimizer_type: OptimizerType

    @classmethod
    def from_dict(cls, optimizer_config: Dict) -> "BaseOptimizerConfig":
        """
        Creates an instance of a specific optimizer configuration subclass from a dictionary.

        Args:
            optimizer_config (Dict): A dictionary containing optimizer configuration parameters.
                                     Must include an "optimizer_type" key.

        Returns:
            BaseOptimizerConfig: An instance of the corresponding optimizer configuration subclass.

        Raises:
            KeyError: If no matching optimizer type is found in the registry.
        """
        optimizer_type = optimizer_config.get("optimizer_type")
        BaseOptimizerConfigClass = BaseOptimizerConfig.get_subclass(key=optimizer_type)
        return BaseOptimizerConfigClass(**optimizer_config)
