from typing import Literal, Optional

ROLES = Literal["DPS", "Healer", "Tank"]
SHIFTS = Literal["Morning Shift", "Afternoon Shift", "Evening Shift"]

class Schedule:
    
    def __init__(self, shift: SHIFTS):
        self.shift = shift
        
    def __repr__(self):
        return f"Shift='{self.shift}'"

class Character:
    def __init__(self, ingame_name: str, role: ROLES):
        self.member: Optional["Member"] = None
        self.ingame_name = ingame_name
        self.role = role
        
    def __repr__(self):
        return f"IGN='{self.ingame_name}', ROLE='{self.role}')"
        
class Member:
    def __init__(self, name: str, schedule: Schedule):
        self.characters = []
        self.discord_name = name
        self.schedule = schedule

    def add_character(self, character: Character):
        self.characters.append(character)
        character.member = self

class NormalParty:
    pass

class RaidParty:
    pass

def main():
    morning_schedule = Schedule("Morning Shift")
    member1 = Member("Amity", morning_schedule)
    character1 = Character(ingame_name="Alysedryn", role="DPS")
    member1.add_character(character1)
    print(member1.discord_name)  # Output: Amity
    print(member1.characters)
    print(member1.schedule)
    
if __name__ == "__main__":
    main()
