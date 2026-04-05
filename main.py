

class Schedule:
    
    def __init__(self, shift: str):
        self.shift = shift


class Member:
    pass

class Characters:
    pass

class NormalParty:
    pass

class RaidParty:
    pass

def main():
    example_schedule = Schedule("Morning Shift")
    print(f"Schedule created with shift: {example_schedule.shift}")
    
if __name__ == "__main__":
    main()
