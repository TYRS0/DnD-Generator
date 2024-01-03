from os import listdir
from random import randint, choice
from json import load


#Generators
def Generate_Class():
    x = 0
    Class_List = []
    Class_Dir = listdir(".\\Files\\Classes")
    Class_Dir_Length = len(Class_Dir)
    if Class_Dir_Length < 1:
        raise FileNotFoundError("No files found in Classes directory")
    while x != Class_Dir_Length:
        Class_File = open(f"./Files/Classes/{Class_Dir[x]}", "r")
        Class_Json = load(Class_File)
        Class_List = Class_List + Class_Json
        x = x + 1
    Class_Length = (len(Class_List)-1)
    Class = (Class_List[randint(0,Class_Length)])
    return Class

def Generate_Race():
    x = 0
    Race_List = []
    SubRace_Dict = {}
    Race_Dir = listdir(".\\Files\\Races")
    Race_Dir_Length = len(Race_Dir)
    if Race_Dir_Length < 1:
        raise FileNotFoundError("No files found in Races directory")
    while x != Race_Dir_Length:
        Race_File = open(f"./Files/Races/{Race_Dir[x]}", "r")
        Race_Json = load(Race_File)
        Race_List = Race_List + Race_Json["Races"]
        Race_Json.pop("Races")
        SubRace_Dict.update(Race_Json)
        x = x + 1
    Race_Length = (len(Race_List)-1)
    Race = (Race_List[randint(0,Race_Length)])
    SubRace_Length = (len(SubRace_Dict[Race])-1)
    SubRace = (SubRace_Dict[Race][randint(0,SubRace_Length)])
    return Race, SubRace

def Generate_Name():
    x = 0
    Gender_List = []
    Name_Dict = {}
    Name_Dir = listdir(".\\Files\\Names")
    Name_Dir_Length = len(Name_Dir)
    if Name_Dir_Length < 1:
        raise FileNotFoundError("No files found in Names directory")
    while x != Name_Dir_Length:
        Name_File = open(f"./Files/Names/{Name_Dir[x]}", "r")
        Name_Json = load(Name_File)
        Gender_List = Gender_List + Name_Json["Gender"]
        Name_Json.pop("Gender")
        Name_Dict.update(Name_Json)
        x = x + 1
    Gender_Length = (len(Gender_List)-1)
    Gender = (Gender_List[randint(0,Gender_Length)])
    if Race in Name_Json["Pools"]:
        Race_Name_Pool = (len(Name_Json[Race + " Race Pool"])-1)
        Race_Selction = (Name_Json[Race + " Race Pool"][randint(0,Race_Name_Pool)])
        First_Name_Length = (len(Name_Json[Race_Selction + " " + Gender])-1)
        Last_Name_Length = (len(Name_Json[Race_Selction + " Last"])-1)
        First_Name = (Name_Json[Race_Selction + " " + Gender][randint(0,First_Name_Length)])
        Last_Name = (Name_Json[Race_Selction + " Last"][randint(0,Last_Name_Length)])
    else:   
        First_Name_Length = (len(Name_Json[Race + " " + Gender])-1)
        Last_Name_Length = (len(Name_Json[Race + " Last"])-1)
        First_Name = (Name_Json[Race + " " + Gender][randint(0,First_Name_Length)])
        Last_Name = (Name_Json[Race + " Last"][randint(0,Last_Name_Length)])
    return First_Name, Last_Name, Gender


#Generation
Class = Generate_Class()
Race, SubRace = Generate_Race()
First_Name, Last_Name, Gender = Generate_Name()


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