class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

# A GameWarehouse object is used to store ComputerGame objects.
class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games

# Returns a list of only those games which were made before the year 1990.      
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()
        
    def list_games(self):
        legends = []
        for game in super().list_games():
            if game.year < 1990:
                legends.append(game)
        return legends
