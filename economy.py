import random

class Economy:
    def __init__(self, world):
        self.world = world
        self.market = {planet: self.generate_market(planet) for planet in self.world.planets}

    def generate_market(self, planet):
        """Generates market prices for a given planet."""
        commodities = ["grain", "metal", "fuel_cells", "electronics"]
        prices = {commodity: random.randint(50, 150) for commodity in commodities}
        
        # Set the fuel price between 1 and 10 for all planets
        prices["fuel_cells"] = random.randint(1, 10)  # Price per unit between 1 and 10 for fuel cells

        return prices

    def get_market(self, planet):
        """Returns the market prices for a given planet."""
        return self.market.get(planet, {})
    
    def update_prices(self):
        """Optionally update prices based on certain logic."""
        for planet in self.world.planets:
            self.market[planet] = self.generate_market(planet)
