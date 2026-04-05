from typing import Literal

class Schedule:
    
    def __init__(self, shift: str):
        self.shift = shift

class Member:
    def __init__(self, name: str):
        self.discord_name = name

class Character:
    def __init__(self, ingame_name: str, role=Literal["DPS", "Healer", "Tank"]):
        self.member = None
        self.ingame_name = ingame_name
        self.role = role

class NormalParty:
    pass

class RaidParty:
    pass

def main():
    example_schedule = Schedule("Morning Shift")
    print(f"Schedule created with shift: {example_schedule.shift}")
    
if __name__ == "__main__":
    main()
