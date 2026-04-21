#!usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional, Any, Type
from datetime import datetime
from enum import Enum
from alien_contacts2 import ALIEN_CONTACTS as lists


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContactModel(BaseModel):

    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(..., max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validator(self) -> None:
        message: str = ""
        found = False
        if not self.contact_id.startswith("AC"):
            message = message.join("The ID need to start with 'AC'\n")
            found = True
        if not self.is_verified and self.contact_type == ContactType.PHYSICAL:
            message = message.join("if the contact is physical, "
                                   "the contact must be verificate\n")
            found = True
        if (self.contact_type == ContactType.TELEPATHIC and
           self.witness_count < 3):
            message = message.join("if the contact is telepathic, the "
                                   "contact must have at last 3 witness\n")
            found = True
        if self.signal_strength > 7.0 and not self.message_received:
            message = message.join("All contact over 7 signal strength need"
                                   " a message\n")
            found = True
        if found:
            raise ValueError(message)
        return self


def main(objets: Type[AlienContactModel], values: dict[str, Any]) -> None:
    try:
        print("=" * 40)
        ale: AlienContactModel = objets(**values)
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
    print("Alien Contact Log Validation")
    for i in lists:
        main(AlienContactModel, i)
