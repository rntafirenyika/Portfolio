# Recording class which models a single recording.
class Recording:
    # constructor which takes the length as an argument
    def __init__(self, length: int):
        if length <= 0:
            raise ValueError("Length cannot be less than or equal to zero")
        self.__length = length

    # Getter method which returns the length of the recording.
    @property
    def length(self):
        return self.__length

    # Setter method which sets the length of the recording.
    @length.setter
    def length(self, length: int):
        if length <= 0:
            raise ValueError("Length cannot be less than or equal to zero")
        self.__length = length
