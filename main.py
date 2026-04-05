from typing import Literal, Optional, List, Dict

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

    def __repr__(self):
        return f"Member('{self.discord_name}', {self.schedule}, {self.characters})"
class NormalParty:
    
    def __init__(self):
        self.members = []
        self.length = 4

    def form_party(self, members: List[Member]):
        result = {"Morning Shift": [], "Afternoon Shift": [], "Evening Shift": []}
        for member in members:
            if member.schedule.shift  == "Morning Shift" and len(result["Morning Shift"]) < self.length:
                result["Morning Shift"].append(member)
            elif member.schedule.shift == "Afternoon Shift" and len(result["Afternoon Shift"]) < self.length:
                result["Afternoon Shift"].append(member)
            elif member.schedule.shift == "Evening Shift" and len(result["Evening Shift"]) < self.length:
                result["Evening Shift"].append(member)
        self.members = result
        return result
    
class RaidParty:
    pass

def main():
    morning_schedule = Schedule("Morning Shift")
    afternoon_schedule = Schedule("Afternoon Shift")
    evening_schedule = Schedule("Evening Shift")

    member1 = Member("Amity", morning_schedule)
    character1 = Character(ingame_name="Alysedryn", role="DPS")
    member1.add_character(character1)
    
    memberr1 = Member("Yarborough", morning_schedule)
    characterr1 = Character(ingame_name="Yarborough", role="Healer")
    memberr1.add_character(characterr1)
    
    member2 = Member("Basil", afternoon_schedule)
    character2 = Character(ingame_name="Rynn", role="Healer")
    member2.add_character(character2)

    member3 = Member("Cass", evening_schedule)
    character3 = Character(ingame_name="Torin", role="Tank")
    member3.add_character(character3)

    all_members = [member1, member2, member3, memberr1]

    print(member1.discord_name)  # Output: Amity
    print(member1.characters)
    print(member1.schedule)

    party = NormalParty()
    party.form_party(all_members)
    print(party.members)

if __name__ == "__main__":
    main()
