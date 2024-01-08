# DnD-Generator
A WiP Customizable Random Character Generator for DnD 5e

the plan is to be able to Make a almost complete Character sheet for player and NPC alike and have the ablity to add homebrew

### Currently Generates
- Name and Gender
- Class
- Race and Subrace
- Stats (STR/DEX/CON/INT/WIS/CHA) With Racial buffs

### Goals
*In no particular order*
- Generate basic info (name, gender, Class, race, ect.)
- Generate stats with related racial buffs (str, con, wis, ect.)
- Generate related spelles for spell casters
- Make a ui to show all the informaion
- Ability to regenerate a new character 

this may take a bit because i am mostly self tought and find it difficult to read documention

## How to use
1. Download Python 3.x
2. Download Repository as Zip and extract anywhere
3. Open file in your prefered IDE (I use Visual Studio Code)
4. Run Main.py
5. Success
 
you can add and edit the .json files as long as you follow the formatting
- Classes.json Holds all classes for now
- Names.json Holds Names based off of selected Race, *will crash if name does not exist for selected Race, will fix soon*
- Races.json Holds all Races, Subraces, and Racial Stats. *will crash if Subrace does not exist for selected Race use N/A for no Subrace as seen is the file, will fix soon*