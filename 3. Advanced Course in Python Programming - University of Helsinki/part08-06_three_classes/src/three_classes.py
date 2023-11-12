# Checklist class constructor
class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries

# Customer class constructor        
class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount

# Cable class constructor        
class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional