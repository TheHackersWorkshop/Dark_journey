from player import Player
from world import World
from economy import Economy
from save_load import save_game, load_game

class Game:
    def __init__(self):
        self.world = World()
        self.economy = Economy(self.world)
        self.player = Player(self.world)

    def start(self):
        print("Welcome to Dark Journey: A Sci-Fi Trade Adventure")
        print("You are at the Earth's space station. Dock to start.")
        print("Type 'help' for available commands.")

        while True:
            command = input("\n> ").strip().lower()
            if not self.handle_command(command):
                break

    def handle_command(self, command):
        if command.startswith("fly to "):
            planet_name = command[7:]
            self.player.fly_to(planet_name, self.economy)

        elif command == "status":
            self.player.status()

        elif command == "dock":
            self.player.dock(self.economy)

        elif command == "nearby":
            self.world.list_nearby_planets(self.player.location)

        elif command == "help":
            print("Commands: fly to <planet>, dock, status, nearby, refuel, buy <commodity> <amount>, sell <commodity> <amount>, upgrade, save, load, exit")

        elif command.startswith("buy "):
            _, commodity, amount = command.split()
            self.player.buy(commodity, int(amount), self.economy)

        elif command.startswith("sell "):
            _, commodity, amount = command.split()
            self.player.sell(commodity, int(amount), self.economy)

        elif command == "refuel":
            self.player.refuel(self.economy)

        elif command == "upgrade":
            self.player.upgrade_cargo()  # Add the upgrade command

        elif command == "save":
            save_game(self.player)

        elif command == "load":
            load_game(self.player)

        elif command == "exit":
            print("Exiting game...")
            return False

        else:
            print("Unknown command. Type 'help' for options.")

        return True
