from __future__ import annotations

from typing import Literal, TypeAlias

from ._constant import Constant, Scalar
from ._identification import LevelIdentifier, MeasureIdentifier
from ._operation import (
    HierarchyIsInCondition,
    IsInCondition,
    IsInConditionOperatorBound,
    LogicalCondition,
    RelationalCondition,
    RelationalConditionOperatorBound,
)

_CubeQueryFilterHierarchyIsInCondition: TypeAlias = HierarchyIsInCondition[
    Literal["IS_IN"], Scalar
]
_CubeQueryFilterIsInLevelCondition: TypeAlias = IsInCondition[
    LevelIdentifier, IsInConditionOperatorBound, Scalar
]
_CubeQueryFilterIsInMeasureCondition: TypeAlias = IsInCondition[
    MeasureIdentifier, IsInConditionOperatorBound, Constant | None
]
_CubeQueryFilterRelationalLevelCondition: TypeAlias = RelationalCondition[
    LevelIdentifier, RelationalConditionOperatorBound, Scalar
]
_CubeQueryFilterRelationalMeasureCondition: TypeAlias = RelationalCondition[
    MeasureIdentifier, RelationalConditionOperatorBound, Constant | None
]
_CubeQueryFilterLeafCondition: TypeAlias = (
    _CubeQueryFilterHierarchyIsInCondition
    | _CubeQueryFilterIsInLevelCondition
    | _CubeQueryFilterIsInMeasureCondition
    | _CubeQueryFilterRelationalLevelCondition
    | _CubeQueryFilterRelationalMeasureCondition
)
CubeQueryFilterCondition: TypeAlias = (
    _CubeQueryFilterLeafCondition
    | LogicalCondition[_CubeQueryFilterLeafCondition, Literal["AND"]]
)
