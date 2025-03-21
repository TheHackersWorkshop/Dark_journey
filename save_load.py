import json

def save_game(player):
    data = {
        "credits": player.credits,
        "fuel": player.fuel,
        "location": player.location,
        "cargo_capacity": player.cargo_capacity,
        "cargo": player.inventory
    }
    with open("savegame.json", "w") as f:
        json.dump(data, f)
    print("Game saved.")

def load_game(player):
    try:
        with open("savegame.json", "r") as f:
            data = json.load(f)
            player.credits = data["credits"]
            player.fuel = data["fuel"]
            player.location = data["location"]
            player.cargo_capacity = data["cargo_capacity"]
            player.inventory = data["cargo"]
        print("Game loaded.")
    except FileNotFoundError:
        print("No save file found.")
