# NPC Calculator
A web page featuring a calculator that displays the results of a battle based on the user's input parameters.

This calculator is designed for Dungeon Masters to enhance their Dungeon and Dragons campaigns by providing a quick way to incorporate battles among NPCs (Non Player Characters).

Calculations are based on the d20 system. (d20 + Attack bonus against armor class, damage according to weapon). Dice rolls perfermed using Python randomizer.)

## User Parameters
User selects the number of heroes and the number of villains. (Maximum 10000 each). In addition, the user selects the race of both heroes and villais using the (radio button) selector. 

Hero races:
- Dwarf
- Elf
- Human

Villain races:
- Goblin
- Orc

## Battle Terrain
After selecting heros and villains, the user determines the battle ground; again by using the (radio buttons) selector. A number of diverse enviroments (terrains) are provided. 

Each terrain is designed to give a certain race an Advantage (+2). 
- Mountain
    - Advantage: Dwarf
- Dungeon
    - Advantage: Goblin
- Fortress
    - Advantage: Human
- Swamp 
    - Advantage: Orc
- Forest
    - Avantage: Elf

## Start Battle / Results
After hitting START Battle, a result readout will display (also triggering 1 second blood animation video).
The result readout will display the following:
- Winner of the battle 
- Number of survivors (Winner only, calculator runs until one party is killed completly)
- count of head to head (one on one) rounds
- count of Critical Hits (natural roll of 20)
- summary of user inputed parameters (pre-battle)


## Features and properties of page
- Django/Python page
    - Python version 3.7
    - Django version 2.2.4
- Background elements desinged with Photoshop and Premiere PRO
- HTML page with CSS and Bootstrap
- User input
- Radio buttons 

## Areas to improve
This is a work in progress. The following areas could be improved.
- Overall responsiveness
- Radio buttons should remember last selections
- More features (for example Hit-dice per race)
