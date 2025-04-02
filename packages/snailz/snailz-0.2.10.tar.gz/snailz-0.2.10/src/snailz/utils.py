"""Utilities."""

import csv
from datetime import date
from io import StringIO
import json
import sys
from pathlib import Path
from typing import Any, Callable, TextIO, Type

from pydantic import BaseModel, Field


# Decimal places in floating-point values.
PRECISION = 2


class Point(BaseModel):
    """A 2D point with x and y coordinates."""

    x: int | None = Field(default=None, description="x coordinate")
    y: int | None = Field(default=None, description="y coordinate")


class UniqueIdGenerator:
    """Generate unique IDs using provided function."""

    def __init__(self, name: str, func: Callable, limit: int = 10000) -> None:
        """Initialize the unique ID generator.

        Parameters:
            name: A name for this generator (used in error messages)
            func: Function that creates IDs when called
            limit: Maximum number of attempts to find a unique ID
        """
        self._name = name
        self._func = func
        self._limit = limit
        self._seen = set()

    def next(self, *args: object) -> str:
        """Get next unique ID.

        Parameters:
            *args: Arguments to pass to the ID-generating function

        Returns:
            A unique identifier that hasn't been returned before

        Raises:
            RuntimeError: If unable to generate a unique ID within limit attempts
        """
        for i in range(self._limit):
            ident = self._func(*args)
            if ident in self._seen:
                continue
            self._seen.add(ident)
            return ident
        raise RuntimeError(f"failed to find unique ID for {self._name}")


def csv_writer(output: TextIO | StringIO) -> Any:
    """Wrapper to get line terminator settings right."""

    return csv.writer(output, lineterminator="\n")


def fail(msg: str) -> None:
    """Print message to standard error and exit with status 1.

    Parameters:
        msg: The error message to display
    """
    print(msg, file=sys.stderr)
    sys.exit(1)


def load_data(
    parameter_name: str, filename: str | Path | None, cls: Type[BaseModel]
) -> BaseModel:
    """Construct a Pydantic model from serialized JSON.

    Parameters:
        parameter_name: Name of the parameter requiring this file (for error messages)
        filename: Path to the JSON file to load (allowed to be None so that checking is done in one place)
        cls: The Pydantic model to instantiate with the loaded data

    Returns:
        An instance of cls constructed from the JSON data

    Raises:
        IOError: If the file cannot be read
    """
    assert filename is not None, f"--{parameter_name} is required"
    with open(filename, "r") as reader:
        return cls.model_validate(json.load(reader))


def report_result(output: str | Path | None, result: BaseModel) -> None:
    """Save or display result as JSON.

    Parameters:
        output: Path to output file, or None to print to stdout
        result: The Pydantic model object to serialize as JSON

    Side effects:
        Either writes to the specified output file or prints to stdout
    """
    result_json = json.dumps(result.model_dump(), default=serialize_values)
    if output:
        with open(output, "w") as writer:
            writer.write(result_json)
    else:
        print(result_json)


def serialize_values(obj: object) -> str | dict:
    """Custom JSON serializer for JSON conversion.

    Parameters:
        obj: The object to serialize

    Returns:
        String representation of date objects or dict for Pydantic models

    Raises:
        TypeError: If the object type is not supported for serialization
    """
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, BaseModel):
        return obj.model_dump()
    raise TypeError(f"Type {type(obj)} not serializable")


def validate_date(ctx: object, param: object, value: str | None) -> date | None:
    """Validate and convert date string to date object.

    Parameters:
        ctx: Click context object
        param: Click parameter being processed
        value: The value to validate

    Returns:
        None if value is None, otherwise a date object
    """
    return None if value is None else date.fromisoformat(value)
