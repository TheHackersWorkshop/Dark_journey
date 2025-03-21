# world.py

import random

class World:
    def __init__(self):
        self.planets = {
            "Earth": {"distance": 0, "name": "Earth", "stories": [
                "The Earth is bustling with activity as people prepare for the upcoming interstellar festival.",
                "As you approach Earth, you notice the shimmering blue oceans that are nearly visible from space.",
                "Earth is experiencing an economic boom. New technologies are popping up in every corner.",
                "You feel a sense of nostalgia as you approach Earth, home to many fond memories.",
                "Earth's cities have grown immensely since the last time you visited, skyscrapers reaching new heights.",
                "The Earth government has issued new travel restrictions due to a recent wave of piracy.",
                "Earth's agriculture is thriving, with vast fields of crops producing enough to feed the colonies.",
                "A long-range communication tower on Earth is sending out distress signals to nearby colonies."
            ]},
            "Mars": {"distance": 20, "name": "Mars", "stories": [
                "Mars is known for its rich mining operations. Massive excavators dig into the red soil.",
                "Mars has begun terraforming efforts, and small patches of green are appearing on the surface.",
                "Mars' colonies are expanding rapidly, creating a bustling atmosphere of progress.",
                "You hear rumors of ancient ruins found deep beneath the Martian surface.",
                "The Martian government has introduced new policies to attract more settlers from other planets.",
                "Mars has recently been the subject of a large-scale scientific expedition studying the planet’s deep core.",
                "Mars' settlements are now more reliant on trade with nearby planets than ever before.",
                "Mars is experiencing a dust storm, making it difficult for travelers to land safely."
            ]},
            "Titan": {"distance": 50, "name": "Titan", "stories": [
                "Titan’s thick atmosphere casts an eerie glow over the surface, making the landscape seem otherworldly.",
                "You are informed that Titan's moons are undergoing a mining rush due to rare minerals discovered.",
                "The methane lakes on Titan are a popular tourist destination, though dangerous to explore.",
                "Titan's population is small but rapidly growing, with settlers coming from all over the solar system.",
                "The icy surface of Titan is said to hide many secrets about the origins of life in the universe.",
                "Titan has an extensive spaceport, serving as a major hub for interplanetary travelers.",
                "Rumors circulate that Titan’s government is facing unrest due to its increasing reliance on foreign trade.",
                "Titan has recently been the site of numerous scientific expeditions to study its alien biology."
            ]},
            "Jupiter": {"distance": 100, "name": "Jupiter", "stories": [
                "Jupiter's stormy atmosphere makes it difficult to navigate, but the rewards of its moons are great.",
                "Jupiter's moons are home to thriving research stations studying its magnetic field and radiation.",
                "Jupiter itself remains largely unexplored, with many dangers lurking within its clouds.",
                "The moons of Jupiter are rich with resources, drawing miners from across the galaxy.",
                "Jupiter's space station is one of the most advanced in the galaxy, a beacon of technological achievement.",
                "Jupiter's atmosphere is constantly changing, creating a hostile but fascinating environment.",
                "Rumors are spreading about strange anomalies appearing near Jupiter's storm systems.",
                "Jupiter is at the center of a new scientific venture, studying the possibility of life beyond Earth."
            ]}
        }

    def list_nearby_planets(self, location):
        """Lists nearby planets based on the player's current location."""
        print(f"Nearby planets to {location}:")
        current_planet_data = self.planets[location]
        for planet, data in self.planets.items():
            # Simple proximity rule based on distance
            if abs(current_planet_data["distance"] - data["distance"]) <= 50:
                print(f"- {planet} (Distance: {data['distance']})")

    def get_planet(self, name):
        """Returns the planet data if it exists."""
        return self.planets.get(name)

    def get_all_planets(self):
        """Returns a list of all planet names."""
        return self.planets.keys()

    def get_distance(self, planet_name):
        """Returns the distance of a planet from Earth."""
        planet = self.get_planet(planet_name)
        if planet:
            return planet["distance"]
        return None

    def generate_market(self, planet_name):
        """Generates a random market for each planet and returns the prices."""
        commodities = ["grain", "metal", "fuel_cells", "electronics"]
        prices = {commodity: random.randint(50, 150) for commodity in commodities}
        return prices  # No print here

    def get_story(self, planet_name):
        """Randomly selects a story for a given planet."""
        planet = self.get_planet(planet_name)
        if planet:
            stories = planet["stories"]
            return random.choice(stories)
        return "No stories available."
