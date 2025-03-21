import random
import time  # Import time module for delay in text output

class Encounter:
    def __init__(self):
        self.enemy_hp = random.randint(20, 40)  # Slightly weaker pirates
        self.enemy_attack = random.randint(5, 12)  # Slightly weaker attack
        self.enemy_defense = random.randint(1, 5)  # Reduce pirate defense to balance fights
        self.enemy_credits = random.randint(30, 100)

    def pirate_attack(self, player):
        print("\nA pirate ship appears! They demand 50 credits or they will attack!")
        action = input("Do you (fight/flee/bribe)? ").strip().lower()

        if action == "fight":
            return self.fight(player)
        elif action == "flee":
            return self.flee(player)
        elif action == "bribe":
            return self.bribe(player)
        else:
            print("Invalid action, pirates attack!")
            time.sleep(1)  # Pause before fight starts
            return self.fight(player)

    def fight(self, player):
        player_hp = 50  # Player starting HP
        player_attack = random.randint(15, 25)  # Increased damage for a higher chance of winning

        while player_hp > 0 and self.enemy_hp > 0:
            print("\nYou prepare for battle...")
            time.sleep(1)  # Small pause before each round

            damage = max(player_attack - self.enemy_defense, 0)  # Reduce damage by pirate defense
            self.enemy_hp -= damage
            print(f"You hit the pirate for {damage} damage! Pirate HP: {self.enemy_hp}")
            time.sleep(1)

            if self.enemy_hp <= 0:
                print("You destroyed the pirate ship!")
                player.credits += 100  # Reward for winning
                return

            enemy_damage = max(self.enemy_attack - random.randint(2, 7), 0)  # Reduce damage variation
            player_hp -= enemy_damage
            print(f"The pirate hits you for {enemy_damage} damage! Your HP: {player_hp}")
            time.sleep(1)

        if player_hp <= 0:
            print("You were destroyed! Game over.")
            exit()

    def flee(self, player):
        print("\nYou attempt to flee from the pirates...")
        time.sleep(1)

        fuel_cost = random.randint(5, 15)
        player.fuel -= fuel_cost  # Random fuel cost
        print(f"You burn {fuel_cost} fuel while escaping. Fuel remaining: {player.fuel}")
        time.sleep(1)

        if random.randint(1, 20) == 1:  # 1 in 20 chance of being hit
            damage = random.randint(5, 15)
            print(f"As you flee, the pirates fire at you! You take {damage} damage.")
            player.hp -= damage  # Assume player object has HP attribute
            time.sleep(1)
        else:
            print("You successfully escaped!")
            time.sleep(1)

    def bribe(self, player):
        bribe_amount = random.randint(30, 80)  # Pirates demand a random bribe
        print(f"\nYou try to bribe the pirates with {bribe_amount} credits...")
        time.sleep(1)

        if player.credits >= bribe_amount:
            print("The pirates accept your bribe and let you go!")
            player.credits -= bribe_amount
        else:
            print("You don't have enough credits to bribe them! The pirates attack!")
            time.sleep(1)
            self.fight(player)
