Wizard Game 
---
Hello, this is a turn-based battle game I made for Coding Temple as part of my Python module.
The game features a classic RPG encounter, the evil wizard in this case, and the player's objective is to defeat the evil wizard.

This encounter simulation features 4 classes for the player to play as with each having their own unique set of abilities.  

1. Warrior - a standard combatant who sports a jack-of-all-trades playstyle
   
    - Power Strike - strong attack that hits for 80% more damage.
    - Shield Bash - a debuff attack thats hits for 20% more damage while lowering the wizard's attack by 5.

2. Mage - a combatant who lacks health but is strong in their attacks.

    - Fireball - a strong attack that hits for 60% more damage.
    - Arcane Siphon - an attack that deals 15% damage while also draining the enemy and restoring the Mage's health by the same amount.
  
3. Archer - a combatant who, though potentially fragile, is capable of outputting a lot fo damage.

    - Double Shot - the Archer shoots 2 arrows each dealing 70% damage
    - Piercing Shot - the Archer shoots an empowered arrow that deals 50% more damage.

4. Paladin - a combatant who specializes in healing while also dealing damage.

    - Holy Smite - the Paladin strikes for 40% more damage while healing 10% of his max health.
    - Divine Heal - the Paladin heals himself for 35% of his max health.

During the encounter, the player will have the following options:

1. Attack - attacks the wizard for a randomized amount of damage set within a range, depending on which class they chose.
2. Use Special Ability - use a special ability corresponding to the class the player chose.
3. Heal - a generalized heal, healing for 25% of the player's max health.
4. View Stats - allows the player to view their current health out of their max health and their class's attack power (this option does not consume a turn).

Depending on if the player wins or loses, they will be shown the relevant confirmation message. 

This encounter is made to be very simple and straightforward, but it is very possible to expand with future iterations.
