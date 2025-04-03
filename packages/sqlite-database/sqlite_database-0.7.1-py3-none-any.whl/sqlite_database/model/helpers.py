"""Model helpers"""
# pylint: disable=invalid-name,too-few-public-methods,abstract-method

from typing import Any, Callable, Type, TypeAlias

from sqlite_database.model.errors import ValidationError
from ..column import BuilderColumn, text, integer, blob, boolean

TypeFunction: TypeAlias = Callable[[str], BuilderColumn]

TYPES: dict[Type[Any], TypeFunction] = { # pylint: disable=possibly-used-before-assignment
    int: integer,
    str: text,
    bytes: blob,
    bool: boolean
}


class Constraint:
    """Base constraint class for models"""
    def __init__(self, column: str) -> None:
        self._column = column

    @property
    def column(self):
        """Columns"""
        return self._column

    def apply(self, type_: BuilderColumn):
        """Apply this constraint to an column"""
        raise NotImplementedError()

class Unique(Constraint):
    """Unique constraint"""

    def apply(self, type_: BuilderColumn):
        type_.unique()

class Foreign(Constraint):
    """Foreign constraint"""

    def __init__(self, column: str, target: str) -> None:
        super().__init__(column)
        self._target = target

    @property
    def target(self):
        """Target foreign constraint"""
        return self._target

    def apply(self, type_: BuilderColumn):
        type_.foreign(self._target)

class Primary(Constraint):
    """Primary constraint"""

    def apply(self, type_: BuilderColumn):
        """Apply this constraint as primary"""
        type_.primary()

class Validators():
    """Base class to hold validators"""

    def __init__(self, fn: Callable[[Any], bool], if_fail: str) -> None:
        self._callable = fn
        self._reason = if_fail

    def validate(self, value: Any):
        """Validate a value"""
        if not self._callable(value):
            err = ValidationError(self._reason)
            err.add_note(str(value))
            raise err
        return True
