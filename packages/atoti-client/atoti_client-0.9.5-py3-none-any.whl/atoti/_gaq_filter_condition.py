from __future__ import annotations

from typing import Literal, TypeAlias

from ._constant import Scalar
from ._identification import LevelIdentifier
from ._operation import IsInCondition, LogicalCondition, RelationalCondition

_GaqFilterLeafCondition: TypeAlias = (
    IsInCondition[LevelIdentifier, Literal["IS_IN"], Scalar]
    | RelationalCondition[LevelIdentifier, Literal["EQ", "NE"], Scalar]
)
GaqFilterCondition: TypeAlias = (
    _GaqFilterLeafCondition | LogicalCondition[_GaqFilterLeafCondition, Literal["AND"]]
)
