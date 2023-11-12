import json

# Dispaly commands Menu.
def help():
    print("commands: ")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")

# Executes selected command.
def execute():
    data = read_file()
    help()
    while True:
        print("")
        command = input("command: ")
        if command == "0":
            break
        elif command == "1":
            search_name(data)
        elif command == "2":
            teams(data)
        elif command == "3":
            countries(data)
        elif command == "4":
            team_players(data)
        elif command == "5":
            country_players(data)
        elif command == "6":
            most_points(data)
        elif command == "7":
            most_goals(data)

# Read the json file.
def read_file():
    filename = input("file name: ")
    with open(filename) as my_file:
        data = my_file.read()
    stats = json.loads(data)
    print(f"read the data of {len(stats)} players\n")
    return stats

# Search by name for a single player's stats.
def search_name(data):
    name = input("name: ")
    for player in data:
        if player["name"] == name:
            print(f'{player["name"]:21}{player["team"]:3}{player["goals"]:>4} +{player["assists"]:>3} ={player["assists"]+player["goals"]:>4}')
            return
        else:
            print("Player not found.")

# List all the abbreviations for team names in alphabetical order.
def teams(data):
    teams = sorted(set(map(lambda x: x["team"], data)))
    for team in teams:
        print(team)

# List all the abbreviations for countries in alphabetical order.
def countries(data):
    nations = sorted(set(map(lambda x: x["nationality"], data)))
    for nation in nations:
        print(nation)            

# List players in a specific team in the order of points scored, from highest to lowest. Points equals goals + assists.
def team_players(data):
    team = input("team: ")
    info = []
    for player in data:
        if player["team"] == team:
            info.append((player["assists"]+player["goals"], f'{player["name"]:21}{player["team"]:3}{player["goals"]:>4} +{player["assists"]:>3} ={player["assists"]+player["goals"]:>4}'))
    sorted_info = sorted(info, key=lambda x: x[0], reverse=True)
    for item in sorted_info:
        print(item[1])

# List players from a specific country in the order of points scored, from highest to lowest.
def country_players(data):
    country = input("country: ")
    info = []
    for player in data:
        if player["nationality"] == country:
            info.append((player["assists"]+player["goals"], f'{player["name"]:21}{player["team"]:3}{player["goals"]:>4} +{player["assists"]:>3} ={player["assists"]+player["goals"]:>4}'))
    sorted_info = sorted(info, key=lambda x: x[0], reverse=True)
    for item in sorted_info:
        print(item[1])

# List of n players who've scored the most points.
# If two players have the same score, whoever has scored the higher number of goals comes first.
def most_points(data):
    num = int(input("how many: "))
    info = []
    for player in data:
        info.append((player["assists"]+player["goals"], player["goals"],  f'{player["name"]:21}{player["team"]:3}{player["goals"]:>4} +{player["assists"]:>3} ={player["assists"]+player["goals"]:>4}'))
    sorted_info = sorted(info, key=lambda x: (x[0], x[1]), reverse=True)
    for i in range(num):
        print(sorted_info[i][2])

# List of n players who've scored the most goals.
# If two players have the same number of goals, whoever has played the lower number of games comes first.
def most_goals(data):
    num = int(input("how many: "))
    info = []
    for player in data:
        info.append((player["goals"], player["games"],  f'{player["name"]:21}{player["team"]:3}{player["goals"]:>4} +{player["assists"]:>3} ={player["assists"]+player["goals"]:>4}'))
    sorted_info = sorted(info, key=lambda x: (-x[0], x[1]))
    for i in range(num):
        print(sorted_info[i][2])

execute()