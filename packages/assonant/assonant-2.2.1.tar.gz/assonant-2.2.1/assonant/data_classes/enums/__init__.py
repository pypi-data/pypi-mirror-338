"""Assonant data classes enums.

This submodule defines Enumations classes used to standardize options from some data classes.
"""

from .beamline_name import BeamlineName
from .experiment_stage import ExperimentStage
from .transformation_type import TransformationType
from .value_placeholders import ValuePlaceholders

__all__ = ["BeamlineName", "ExperimentStage", "TransformationType", "ValuePlaceholders"]
