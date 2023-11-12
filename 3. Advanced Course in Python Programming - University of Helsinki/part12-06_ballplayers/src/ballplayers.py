class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')

# Takes a list of ball players as its argument.
# Returns the name of the player who scored the most goals, in string format.
def most_goals(players: list):
     return sorted(players, key=lambda player: player.goals)[-1].name

# Which takes a list of ball players as its argument.
# Returns a tuple containing the name and shirt number of the player who has scored the most points.     
def most_points(players: list):
     mp = sorted(players, key=lambda player: player.goals+player.passes)[-1]
     return (mp.name, mp.number)

# Which takes a list of ball players as its argument.
# Returns the BallPlayer object which has the smallest value of minutes played.
def least_minutes(players: list):
     return sorted(players, key=lambda player: player.minutes)[0]