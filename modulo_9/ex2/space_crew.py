#!usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Any, Type, List
from datetime import datetime
from enum import Enum
from space_missions2 import SPACE_MISSIONS as lists


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMemberModel(BaseModel):

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=2, max_length=50)
    years_experience: int = Field(..., ge=0, le=50)
    is_operational: bool = True


class SpaceMissionModel(BaseModel):

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMemberModel] = Field(..., min_length=3, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    def experience(self, crew: List[CrewMemberModel]) -> bool:
        count = 0
        for member in crew:
            if member.years_experience >= 5:
                count += 1
        return (len(crew) / 2) <= count

    @model_validator(mode="after")
    def validator(self) -> "SpaceMissionModel":
        message: str = ""
        found = False
        if not self.mission_id.startswith("M"):
            message = message.join("The ID need to start with 'M'\n")
            found = True
        if not any(crew.rank in [Rank.CAPTAIN, Rank.COMMANDER]
                   for crew in self.crew):
            message = message.join("the crew need a captain or Commander\n")
            found = True
        if (self.duration_days >= 365 and not self.experience(self.crew)):
            message = message.join("The crew need more experience to"
                                   " this mision\n")
            found = True
        if not all(crew.is_operational for crew in self.crew):
            message = message.join("Need All crew Active\n")
            found = True
        if found:
            raise ValueError(message)
        return self


def main(objets: Type[SpaceMissionModel], values: dict[str, Any]) -> None:
    try:
        print("=" * 40)
        ale: SpaceMissionModel = objets(**values)
        print("Valid mission created:")
        print(f"Mission: {ale.mission_name}")
        print(f"ID: {ale.mission_id}")
        print(f"Destination: {ale.destination}")
        print(f"Duration: {ale.duration_days} days")
        print(f"Budget: ${ale.budget_millions}M")
        print(f"Crew size: {len(ale.crew)}")
        print("Crew members:")
        for member in ale.crew:
            print(f" - {member.name} ({member.rank}) - "
                  f"{member.specialization}")
        print()
    except (ValidationError, ValueError) as e:
        print("Expected validation error:")
        if isinstance(e, ValueError):
            print(e, end="")
        else:
            print("\n\nhola\n\n")
            lis = e.errors()
            for i in lis:
                print(f"{i['msg']} in {i['loc']}")
            print()


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    for i in lists:
        main(SpaceMissionModel, i)
