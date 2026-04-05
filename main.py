from typing import Literal

class Schedule:
    
    def __init__(self, shift: Literal["Morning Shift", "Afternoon Shift", "Evening Shift"]):
        self.shift = shift

class Character:
    def __init__(self, ingame_name: str, role=Literal["DPS", "Healer", "Tank"]):
        self.member = None
        self.ingame_name = ingame_name
        self.role = role
        
class Member:
    def __init__(self, name: str, schedule: Schedule):
        self.characters = []
        self.discord_name = name
        self.schedule = schedule

class NormalParty:
    pass

class RaidParty:
    pass

def main():
    example_schedule = Schedule("Morning Shift")
    print(f"Schedule created with shift: {example_schedule.shift}")
    
if __name__ == "__main__":
    main()
