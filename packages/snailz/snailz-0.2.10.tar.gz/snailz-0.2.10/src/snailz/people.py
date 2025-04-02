"""Generate synthetic people."""

import io
import random

from faker import Faker, config as faker_config
from pydantic import BaseModel, Field, field_validator

from . import utils


class PeopleParams(BaseModel):
    """Parameters for people generation."""

    locale: str = Field(
        description="Locale code for generating names (must be supported by Faker)"
    )
    number: int = Field(
        gt=0, description="Number of people to generate (must be positive)"
    )
    seed: int = Field(ge=0, description="Random seed for reproducibility")

    model_config = {"extra": "forbid"}

    @field_validator("locale")
    def validate_fields(cls, v):
        """Validate that the locale is available in faker."""
        if v not in faker_config.AVAILABLE_LOCALES:
            raise ValueError(f"Unknown locale {v}")
        return v


class Person(BaseModel):
    """A single person."""

    family: str = Field(description="family name")
    ident: str = Field(description="unique identifier")
    personal: str = Field(description="personal name")


class AllPersons(BaseModel):
    """A set of generated people."""

    individuals: list[Person] = Field(description="list of people")
    params: PeopleParams = Field(description="parameters used to generate data")

    def to_csv(self) -> str:
        """Return a CSV string representation of the people data.

        Returns:
            A CSV-formatted string with people data (without parameters) using Unix line endings
        """
        output = io.StringIO()
        writer = utils.csv_writer(output)
        writer.writerow(["ident", "personal", "family"])
        for person in self.individuals:
            writer.writerow([person.ident, person.personal, person.family])
        return output.getvalue()


def people_generate(params: PeopleParams) -> AllPersons:
    """Generate synthetic people data.

    Parameters:
        params: PeopleParams object

    Returns:
        AllPersons object containing generated individuals and parameters
    """
    fake = Faker(params.locale)
    fake.seed_instance(params.seed)
    gen = utils.UniqueIdGenerator(
        "people",
        lambda p, f: f"{f[0].lower()}{p[0].lower()}{random.randint(0, 9999):04d}",
    )

    individuals = []
    for _ in range(params.number):
        personal = fake.first_name()
        family = fake.last_name()
        ident = gen.next(personal, family)
        individuals.append(Person(personal=personal, family=family, ident=ident))

    return AllPersons(individuals=individuals, params=params)
