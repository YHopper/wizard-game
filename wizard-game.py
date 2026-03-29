import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def heal(self):
        heal_amount = int(self.max_health * 0.25)
        old_health = self.health
        self.health = min(self.health + heal_amount, self.max_health)
        restored = self.health - old_health
        print(f"{self.name} heals for {restored} health! Current health: {self.health}/{self.max_health}")

    def attack(self, opponent):
        low = int(self.attack_power * 0.8)
        high = int(self.attack_power * 1.0)
        damage = random.randint(low, high)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def get_ability_names(self):
        return ["No Ability", "No Ability"]

    def use_ability(self, ability_choice, opponent):
        print(f"{self.name} does not have special abilities yet.")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def get_ability_names(self):
        return ["Power Strike", "Shield Bash"]

    def use_ability(self, ability_choice, opponent):
        if ability_choice == '1':
            damage = int(self.attack_power * 1.8)
            opponent.health -= damage
            print(f"{self.name} uses Power Strike for {damage} damage!")
        elif ability_choice == '2':
            damage = int(self.attack_power * 1.2)
            opponent.health -= damage
            opponent.attack_power = max(1, opponent.attack_power - 5)
            print(f"{self.name} uses Shield Bash for {damage} damage and lowers {opponent.name}'s attack by 5!")
        else:
            print("Invalid ability choice.")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def get_ability_names(self):
        return ["Fireball", "Arcane Siphon"]

    def use_ability(self, ability_choice, opponent):
        if ability_choice == '1':
            damage = int(self.attack_power * 1.6)
            opponent.health -= damage
            print(f"{self.name} casts Fireball for {damage} damage!")
        elif ability_choice == '2':
            damage = self.attack_power
            opponent.health -= damage
            drain = int(self.max_health * 0.15)
            old_health = self.health
            self.health = min(self.health + drain, self.max_health)
            restored = self.health - old_health
            print(f"{self.name} uses Arcane Siphon for {damage} damage and restores {restored} health!")
        else:
            print("Invalid ability choice.")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health = min(self.health + 5, self.max_health)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)

    def get_ability_names(self):
        return ["Double Shot", "Piercing Arrow"]

    def use_ability(self, ability_choice, opponent):
        if ability_choice == '1':
            hit_damage = int(self.attack_power * 0.7)
            total_damage = hit_damage * 2
            opponent.health -= total_damage
            print(f"{self.name} uses Double Shot for {hit_damage} + {hit_damage} damage!")
        elif ability_choice == '2':
            damage = int(self.attack_power * 1.5)
            opponent.health -= damage
            print(f"{self.name} uses Piercing Arrow for {damage} damage!")
        else:
            print("Invalid ability choice.")

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)

    def get_ability_names(self):
        return ["Holy Smite", "Divine Heal"]

    def use_ability(self, ability_choice, opponent):
        if ability_choice == '1':
            damage = int(self.attack_power * 1.4)
            opponent.health -= damage
            heal_amount = int(self.max_health * 0.1)
            old_health = self.health
            self.health = min(self.health + heal_amount, self.max_health)
            restored = self.health - old_health
            print(f"{self.name} uses Holy Smite for {damage} damage and restores {restored} health!")
        elif ability_choice == '2':
            heal_amount = int(self.max_health * 0.35)
            old_health = self.health
            self.health = min(self.health + heal_amount, self.max_health)
            restored = self.health - old_health
            print(f"{self.name} uses Divine Heal and restores {restored} health!")
        else:
            print("Invalid ability choice.")

def create_character():
    print("Welcome to the wizard game! Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

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
        print("Invalid choice. Please type the number corresponding to your class choice.")
        return create_character()

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- The Evil Wizard stands before you. It is your turn! ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            abilities = player.get_ability_names()
            while True:
                print(f"1. {abilities[0]}")
                print(f"2. {abilities[1]}")
                ability_choice = input("Choose an ability: ")
                if ability_choice in ('1', '2'):
                    player.use_ability(ability_choice, wizard)
                    break
                print("Invalid ability choice. Please enter 1 or 2.")
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated! Is this truly the end?")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}! The day is saved!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()