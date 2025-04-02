"""Test people generation."""

import csv
import io
import pytest
import random

from snailz.defaults import DEFAULT_PEOPLE_PARAMS
from snailz.people import people_generate, AllPersons, Person, PeopleParams

from utils import check_params_stored


@pytest.mark.parametrize(
    "name, value",
    [
        ("number", 0),
        ("number", -5),
        ("locale", ""),
    ],
)
def test_people_fail_bad_parameter_value(name, value):
    """Test people generation fails with invalid parameter values."""
    params_dict = DEFAULT_PEOPLE_PARAMS.model_dump()
    params_dict[name] = value
    with pytest.raises(ValueError):
        PeopleParams(**params_dict)


@pytest.mark.parametrize("seed", [127893, 47129, 990124, 512741, 44109318])
def test_people_valid_result(seed):
    """Test that people generation returns the expected structure."""
    random.seed(seed)
    params = DEFAULT_PEOPLE_PARAMS.model_copy(update={"seed": seed})
    result = people_generate(params)
    check_params_stored(params, result)

    # Check result has correct structure
    assert hasattr(result, "individuals")
    assert isinstance(result.individuals, list)
    assert len(result.individuals) == DEFAULT_PEOPLE_PARAMS.number

    # Check that all individuals have personal and family names
    for person in result.individuals:
        assert person.personal
        assert person.family
        assert isinstance(person.personal, str)
        assert isinstance(person.family, str)

        assert len(person.ident) == 6
        assert person.ident[:2] == (person.family[0] + person.personal[0]).lower()
        assert person.ident[2:].isdigit()
        assert len(person.ident[2:]) == 4

    # Check that all identifiers are unique
    identifiers = [person.ident for person in result.individuals]
    assert len(set(identifiers)) == len(identifiers)

    # Check that new seed is stored
    assert result.params.seed == seed


def test_people_to_csv():
    """Test exporting people to CSV string."""
    people = AllPersons(
        individuals=[
            Person(personal="John", family="Doe", ident="jd1234"),
            Person(personal="Jane", family="Smith", ident="js5678"),
        ],
        params={"locale": "en_US", "number": 2, "seed": 12345},
    )

    csv_string = people.to_csv()
    rows = list(csv.reader(io.StringIO(csv_string)))

    assert len(rows) == 3
    assert rows[0] == ["ident", "personal", "family"]
    assert rows[1] == ["jd1234", "John", "Doe"]
    assert rows[2] == ["js5678", "Jane", "Smith"]
