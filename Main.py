from os import listdir
from random import randint, choice
from json import load


#Generators
def Generate_Class():
    #Declaring Variables
    x = 0
    Class_List = []
    Class_Dir = listdir(".\\Files\\Classes")
    Class_Dir_Length = len(Class_Dir)
    
    #Checks for files in the Class Folder and errors if no file are found
    if Class_Dir_Length < 1:
        raise FileNotFoundError("No files found in Classes directory")

    #Opens and loads all files into a Class List
    while x != Class_Dir_Length:
        Class_File = open(f"./Files/Classes/{Class_Dir[x]}", "r")
        Class_Json = load(Class_File)
        Class_List = Class_List + Class_Json
        x = x + 1

    #Gets the length of the Class List and randomly picks one
    Class_Length = (len(Class_List)-1)
    Class = (Class_List[randint(0,Class_Length)])
    return Class

def Generate_Race():
    #Declaring Variables
    x = 0
    Race_List = []
    SubRace_Dict = {}
    Race_Dir = listdir(".\\Files\\Races")
    Race_Dir_Length = len(Race_Dir)

    #Checks for files in the Race Folder and errors if no file are found
    if Race_Dir_Length < 1:
        raise FileNotFoundError("No files found in Races directory")

    #Opens and loads all files into a Race list and a SubRace Dictionary
    while x != Race_Dir_Length:
        Race_File = open(f"./Files/Races/{Race_Dir[x]}", "r")
        Race_Json = load(Race_File)
        Race_List = Race_List + Race_Json["Races"]
        Race_Json.pop("Races")
        SubRace_Dict.update(Race_Json)
        x = x + 1

    #Gets the length of the Race list and randomly picks one
    Race_Length = (len(Race_List)-1)
    Race = (Race_List[randint(0,Race_Length)])
    
    #Gets the length of the SubRace Dictionary and randomly picks one based off the Race List
    try:
        SubRace_Length = (len(SubRace_Dict[Race])-1)
        SubRace = (SubRace_Dict[Race][randint(0,SubRace_Length)])

    #if no Subrace exists for that Race it errors and returns N/A
    except:
        SubRace = "N/A"
    return Race, SubRace

def Generate_Stats():
    #Declaring Variables
    x = 0
    STR_Bonus = 0
    DEX_Bonus = 0
    CON_Bonus = 0
    INT_Bonus = 0
    WIS_Bonus = 0
    CHA_Bonus = 0
    Strength_Bonus_Dictionary = {}
    Dexterity_Bonus_Dictionary = {}
    Constitution_Bonus_Dictionary = {}
    Intelligence_Bonus_Dictionary = {}
    Wisdom_Bonus_Dictionary = {}
    Charisma_Bonus_Dictionary = {}
    Stat_Loop_List = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
    Bonus_loop = [f"{Race}",f"{SubRace} {Race}"]
    Race_Dir = listdir(".\\Files\\Races")
    Race_Dir_Length = len(Race_Dir)
    
    #Checks for files in the Race Folder and errors if no file are found
    if Race_Dir_Length < 1:
        raise FileNotFoundError("No files found in Races directory")
    
    #Opens and loads all files into a six sepreate Stat Dictionarys
    while x != Race_Dir_Length:
        Race_File = open(f"./Files/Races/{Race_Dir[x]}", "r")
        Race_Json = load(Race_File)
        Strength_Bonus_Dictionary.update(Race_Json[("Strength")])
        Dexterity_Bonus_Dictionary.update(Race_Json[("Dexterity")])
        Constitution_Bonus_Dictionary.update(Race_Json[("Constitution")])
        Intelligence_Bonus_Dictionary.update(Race_Json[("Intelligence")])
        Wisdom_Bonus_Dictionary.update(Race_Json[("Wisdom")])
        Charisma_Bonus_Dictionary.update(Race_Json[("Charisma")])
        x = x + 1

    #Checks for relevent Stat Bonuses based off of Race and SubRace
    for y in Bonus_loop:
        if {y} <= Strength_Bonus_Dictionary.keys():
            STR_Bonus = STR_Bonus + Strength_Bonus_Dictionary[y]
        if {y} <= Dexterity_Bonus_Dictionary.keys():
            DEX_Bonus = DEX_Bonus + Dexterity_Bonus_Dictionary[y]
        if {y} <= Constitution_Bonus_Dictionary.keys():
            CON_Bonus = CON_Bonus + Constitution_Bonus_Dictionary[y]
        if {y} <= Intelligence_Bonus_Dictionary.keys():
            INT_Bonus = INT_Bonus + Intelligence_Bonus_Dictionary[y]
        if {y} <= Wisdom_Bonus_Dictionary.keys():
            WIS_Bonus = WIS_Bonus + Wisdom_Bonus_Dictionary[y]
        if {y} <= Charisma_Bonus_Dictionary.keys():
            CHA_Bonus = CHA_Bonus + Charisma_Bonus_Dictionary[y]
    
    #Rolls 4D6 and removes the smallest number then adds the Bonus for each Stat
    for y in Stat_Loop_List:
        Dice_roll = [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
        Dice_roll.remove(min(Dice_roll))
        
        if y == "Strength":
            Strength = sum(Dice_roll) + STR_Bonus
            STR_Mod = ((Strength - 10) // 2)
        elif y == "Dexterity":
            Dexterity = sum(Dice_roll) + DEX_Bonus
            DEX_Mod = ((Dexterity - 10) // 2)
        elif y == "Constitution":
            Constitution = sum(Dice_roll) + CON_Bonus
            CON_Mod = ((Constitution - 10) // 2)
        elif y == "Intelligence":
            Intelligence = sum(Dice_roll) + INT_Bonus
            INT_Mod = ((Intelligence - 10) // 2)
        elif y == "Wisdom":
            Wisdom = sum(Dice_roll) + WIS_Bonus
            WIS_Mod = ((Wisdom - 10) // 2)
        elif y == "Charisma":
            Charisma = sum(Dice_roll) + CHA_Bonus
            CHA_Mod = ((Charisma - 10) // 2)
    
    return Strength, STR_Mod, Dexterity, DEX_Mod, Constitution, CON_Mod, Intelligence, INT_Mod, Wisdom, WIS_Mod, Charisma, CHA_Mod

def Generate_Name():
    #Declaring Variables
    x = 0
    Gender_List = []
    Name_Dict = {}
    Name_Dir = listdir(".\\Files\\Names")
    Name_Dir_Length = len(Name_Dir)

    #Checks for files in the Names Folder and errors if no file are found
    if Name_Dir_Length < 1:
        raise FileNotFoundError("No files found in Names directory")
    
    #Opens and loads all files into a Gender list and a Name Dictionary
    while x != Name_Dir_Length:
        Name_File = open(f"./Files/Names/{Name_Dir[x]}", "r")
        Name_Json = load(Name_File)
        Gender_List = Gender_List + Name_Json["Gender"]
        Name_Json.pop("Gender")
        Name_Dict.update(Name_Json)
        x = x + 1
        
    #Gets the length of the Gender list and randomly picks one
    Gender_Length = (len(Gender_List)-1)
    Gender = (Gender_List[randint(0,Gender_Length)])

    #if Race has multiple pools of Names then it randomly picks a pool then is randomly picks one based off of gender
    if Race in Name_Json["Pools"]:
        Race_Name_Pool = (len(Name_Json[Race + " Race Pool"])-1)
        Race_Selction = (Name_Json[Race + " Race Pool"][randint(0,Race_Name_Pool)])
        First_Name_Length = (len(Name_Json[Race_Selction + " " + Gender])-1)
        Last_Name_Length = (len(Name_Json[Race_Selction + " Last"])-1)
        First_Name = (Name_Json[Race_Selction + " " + Gender][randint(0,First_Name_Length)])
        Last_Name = (Name_Json[Race_Selction + " Last"][randint(0,Last_Name_Length)])
    
    else:
        #Gets the length of the Name Dictionary and randomly picks one based off Race and Gender
        try:
            First_Name_Length = (len(Name_Json[Race + " " + Gender])-1)
            Last_Name_Length = (len(Name_Json[Race + " Last"])-1)
            First_Name = (Name_Json[Race + " " + Gender][randint(0,First_Name_Length)])
            Last_Name = (Name_Json[Race + " Last"][randint(0,Last_Name_Length)])
            
        #if no Names exists for that Race it errors and returns Generic Names   
        except:
            First_Name_Length = (len(Name_Json[Gender])-1)
            Last_Name_Length = (len(Name_Json["Last"])-1)
            First_Name = (Name_Json[Gender][randint(0,First_Name_Length)])
            Last_Name = (Name_Json["Last"][randint(0,Last_Name_Length)])

    return First_Name, Last_Name, Gender


#Generation
Class = Generate_Class()
Race, SubRace = Generate_Race()
First_Name, Last_Name, Gender = Generate_Name()
Strength, STR_Mod, Dexterity, DEX_Mod, Constitution, CON_Mod, Intelligence, INT_Mod, Wisdom, WIS_Mod, Charisma, CHA_Mod = Generate_Stats()


#Output
if Last_Name == "N/A":
    print (f"Name: {First_Name}")
else:
    print (f"Name: {First_Name} {Last_Name}")

print (f"Gender: {Gender}")

if SubRace == "N/A":
    print (f"Race: {Race}")
else:
    print (f"Race: {SubRace} {Race}")

print (f"Class: {Class}")
print (f"Str / {Strength} ({STR_Mod})")
print (f"Dex / {Dexterity} ({DEX_Mod})")
print (f"Con / {Constitution} ({CON_Mod})")
print (f"Int / {Intelligence} ({INT_Mod})")
print (f"Wis / {Wisdom} ({WIS_Mod})")
print (f"Cha / {Charisma} ({CHA_Mod})")