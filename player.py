import random
from encounters import Encounter

class Player:
    def __init__(self, world):
        self.credits = 5000
        self.fuel = 100
        self.location = "Earth"
        self.cargo_capacity = 10  # Starting cargo capacity
        self.inventory = {}
        self.world = world
        self.docked = False

    def status(self):
        print(f"Location: {self.location}")
        print(f"Fuel: {self.fuel}")
        print(f"Credits: {self.credits}")
        print(f"Cargo Capacity: {self.cargo_capacity} units")
        print(f"Cargo: {self.inventory if self.inventory else 'Empty'}")

    def fly_to(self, planet_name, economy):
        """Moves the player to another planet if fuel allows."""
        planet_name = next((p for p in self.world.planets if p.lower() == planet_name.lower()), None)

        if not planet_name:
            print("Error: That is not a known location.")
            return

        current_planet_data = self.world.planets[self.location]
        target_planet_data = self.world.planets[planet_name]
        distance = abs(current_planet_data["distance"] - target_planet_data["distance"])

        if self.fuel < distance:
            print("Not enough fuel to reach the destination.")
            print("You will be doomed to forever drift through space!")
            return

        # Display a random story from the planet
        print(self.world.get_story(planet_name))  # This will fetch a random story

        self.fuel -= distance
        self.location = planet_name
        self.docked = False
        economy.update_prices()
        print(f"Traveled to {planet_name}. Fuel remaining: {self.fuel}")
        print(" ")

        if random.random() < 0.25:
            self.pirate_encounter()

    def pirate_encounter(self):
        """Randomly encounters pirates during travel."""
        chance = random.randint(1, 100)

        if chance <= 20:
            print("\nA pirate ship has appeared!")
            encounter = Encounter()
            encounter.pirate_attack(self)

    def dock(self, economy):
        """Allows docking at a planet to access markets & refuel."""
        if not self.docked:
            print(f"Docking at {self.location} station...")
            self.docked = True
            print("You are now docked. You can trade, refuel, or upgrade your cargo.")
            print(" ")
            self.show_market(economy)

            if self.location == "Earth" and not self.inventory:
                self.inventory["grain"] = 5
                print("You received 5 units of grain as a starter cargo.")
        else:
            print("You're already docked here.")
            print(f"Docking at {self.location} station...")

    def show_market(self, economy):
        """Displays the commodities available for trade and their prices."""
        market = economy.get_market(self.location)
        print(f"Market at {self.location}:")
        for commodity, price in market.items():
            print(f"- {commodity.capitalize()}: {price} credits per unit")

    def buy(self, commodity, amount, economy):
        """Handles buying commodities from the market."""
        if not self.docked:
            print("You must dock at a station before trading!")
            return

        market = economy.get_market(self.location)
        if commodity not in market:
            print(f"{commodity.capitalize()} is not available here.")
            return

        price = market[commodity]
        total_cost = price * amount

        if total_cost > self.credits:
            print("Not enough credits.")
            return

        if sum(self.inventory.values()) + amount > self.cargo_capacity:
            print("Not enough cargo space.")
            return

        self.credits -= total_cost
        self.inventory[commodity] = self.inventory.get(commodity, 0) + amount
        print(f"Bought {amount} units of {commodity} for {total_cost} credits.")

    def sell(self, commodity, amount, economy):
        """Handles selling commodities to the market."""
        if not self.docked:
            print("You must dock at a station before trading!")
            return

        if commodity not in self.inventory or self.inventory[commodity] < amount:
            print("You don't have enough of that commodity.")
            return

        market = economy.get_market(self.location)
        if commodity not in market:
            print(f"No buyers for {commodity.capitalize()} here.")
            return

        price = market[commodity]
        total_sale = price * amount
        self.credits += total_sale
        self.inventory[commodity] -= amount

        if self.inventory[commodity] == 0:
            del self.inventory[commodity]

        print(f"Sold {amount} units of {commodity} for {total_sale} credits.")

    def refuel(self, economy):
        """Refuels the player's spaceship."""
        if not self.docked:
            print("You must dock at a station before refueling!")
            return

        market = economy.get_market(self.location)
        if "fuel_cells" not in market:
            print("Fuel is not available at this station.")
            return

        fuel_price = market["fuel_cells"]
        max_fuel_needed = 100 - self.fuel  # This calculates the amount of fuel needed to reach 100
        if max_fuel_needed == 0:
            print("You are already at full fuel.")
            return

        total_refuel_cost = fuel_price * max_fuel_needed  # Calculate cost for only the fuel needed
        if self.credits < total_refuel_cost:
            print(f"Not enough credits to refuel. You need {total_refuel_cost} credits.")
            return

        self.fuel = 100  # Refuel to full capacity
        self.credits -= total_refuel_cost  # Deduct the cost from credits
        print(f"Refueled {max_fuel_needed} units. Current fuel: {self.fuel}. Credits remaining: {self.credits}.")

    def upgrade_cargo(self):
        """Allows the player to upgrade their cargo hold for a cost."""
        if not self.docked:
            print("You must be docked at a station to upgrade cargo!")
            return

        upgrade_cost = self.cargo_capacity * 100  # Cost increases as cargo grows

        if self.credits < upgrade_cost:
            print(f"Not enough credits to upgrade! You need {upgrade_cost} credits.")
            return

        self.credits -= upgrade_cost
        self.cargo_capacity += 5  # Increase cargo space by 5 units
        print(f"Cargo capacity increased to {self.cargo_capacity} units! Credits left: {self.credits}")
