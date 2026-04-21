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

    def experience(crew: List[CrewMemberModel]) -> bool:
        return True

    @model_validator(mode="after")
    def validator(self) -> None:
        message: str = ""
        found = False
        if not self.contact_id.startswith("M"):
            message = message.join("The ID need to start with 'M'\n")
            found = True
        if not any(crew.rank in [Rank.CAPTAIN, Rank.COMMANDER]
                   for crew in self.crew):
            message = message.join("the \n")
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
        print("Valid contact report:")
        print(f"ID: {ale.contact_id}")
        print(f"Type: {ale.contact_type}")
        print(f"Location: {ale.location}")
        print(f"Day: {ale.timestamp}")
        print(f"Signal: {ale.signal_strength}/10")
        print(f"Duration: {ale.duration_minutes} minutes")
        print(f"Witnesses: {ale.witness_count}")
        print(f"Message: {ale.message_received}")
        print("Verificate:", end="")
        print('Is Verificate' if ale.is_verified else 'Is NOT Verificates',
              end="\n\n")
    except (ValidationError, ValueError) as e:
        print("Expected validation error:")
        if isinstance(e, ValueError):
            print(e.errors()[0]['msg'])
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
