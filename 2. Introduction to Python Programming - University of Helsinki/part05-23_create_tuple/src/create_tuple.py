# Takes three integers as its arguments, and creates and returns a tuple.
# The first element in the tuple is the smallest of the arguments
# The second element in the tuple is the greatest of the arguments
# The third element in the tuple is the sum of the arguments

def create_tuple(x: int, y: int, z: int):
    nums = (x, y, z)
    return (min(nums), max(nums), sum(nums))
    
    
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))