# Base Character class
import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
    import random
    def heal(self):
        heal_amount = 20  # Set the amount of health restored
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health  # Ensure health does not exceed maximum
        print(f"{self.name} heals for {heal_amount}. Current health: {self.health}/{self.max_health}")
    
    import random
    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        damage = max(1, damage)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")



# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    # Add your cast spell method here

    # Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)  # Customize health and attack power
    
    def quick_shot(self, opponent):
        damage = self.attack_power * 2  # Double attack power
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot on {opponent.name} for {damage} damage!")

    def evade(self):
        print(f"{self.name} prepares to evade the next attack.")

# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)  # High health, moderate attack power
    
    def holy_strike(self, opponent):
        damage = self.attack_power + 10  # Bonus damage
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} damage!")

    def divine_shield(self):
        print(f"{self.name} activates Divine Shield and blocks the next attack.")



# wizard class (inherits from Character)
class Evilwizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")


    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
       return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    


# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Archer):
                print("1. Quick Shot")
                print("2. Evade")
                ability_choice = input("Choose an ability: ")
            if ability_choice == '1':
                player.quick_shot(wizard)
            elif ability_choice == '2':
                player.evade()
            elif isinstance(player, Paladin):
                print("1. Holy Strike")
                print("2. Divine Shield")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.holy_strike(wizard)
                elif ability_choice == '2':
                    player.divine_shield(wizard)

        elif choice == '3':
            player.heal()
        
        elif choice == '4':
                player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = Evilwizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()
