class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.original_value = initial_value

    def print_value(self):
        print("value:", self.value)

    # Decreases the value stored in the counter by one.
    def decrease(self):
        if self.value > 0:
            self.value -= 1

    # Sets the value of the counter to 0            
    def set_to_zero(self):
        self.value = 0

    # Resets the counter to its initial state        
    def reset_original_value(self):
        self.value = self.original_value