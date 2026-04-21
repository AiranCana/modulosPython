#!usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError
from typing import Optional, Any, Type
from datetime import datetime
from space_stations2 import SPACE_STATIONS as lists


class SpaceStationModel(BaseModel):

    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(..., max_length=200)


def main(objets: Type[SpaceStationModel], values: dict[str, Any]) -> None:
    try:
        print("=" * 40)
        sta = objets(**values)
        print("Valid station created:")
        print(f"ID: {sta.station_id}")
        print(f"Name: {sta.name}")
        print(f"Crew: {sta.crew_size} people")
        print(f"Power: {sta.power_level}%")
        print(f"Oxygen: {sta.oxygen_level}%")
        print(f"Last maintenance: {sta.last_maintenance}")
        print(f"Notes: {sta.notes}")
        print("Status:", end="")
        print('Operational' if sta.is_operational else 'No operational',
              end="\n\n")
    except ValidationError as e:
        print("Expected validation error:")
        lis = e.errors()
        for i in lis:
            print(i)
            print(f"{i['msg']} in {i['loc']}")
        print()


if __name__ == "__main__":
    print("Space Station Data Validation")
    for i in lists:
        main(SpaceStationModel, i)
