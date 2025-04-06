from __future__ import annotations

from ...._measure.calculated_measure import CalculatedMeasure, Operator
from ...._measure_convertible import VariableMeasureConvertible
from ...._measure_description import MeasureDescription, convert_to_measure_description
from .._strictly_positive_number import StrictlyPositiveNumber


def cdf(
    point: VariableMeasureConvertible,
    /,
    *,
    degrees_of_freedom: StrictlyPositiveNumber | VariableMeasureConvertible,
) -> MeasureDescription:
    """Cumulative distribution function for a Student's t distribution.

    Args:
        point: The point where the function is evaluated.
        degrees_of_freedom: The number of degrees of freedom.
            Must be positive.

    See Also:
        `The Student's t Wikipedia page <https://en.wikipedia.org/wiki/Student%27s_t-distribution>`__.

    """
    return CalculatedMeasure(
        Operator(
            "student_cumulative_probability",
            [
                convert_to_measure_description(arg)
                for arg in [point, degrees_of_freedom]
            ],
        ),
    )
