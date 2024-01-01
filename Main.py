from random import randint, choice
from json import load


#Generators
def Generate_Class():
    Class_File = open("Classes.json", "r")
    Class_Json = load(Class_File)
    Class_Length = (len(Class_Json)-1)
    Class = (Class_Json[randint(0,Class_Length)])
    return Class

def Generate_Race():
    Race_File = open("Races.json", "r")
    Race_Json = load(Race_File)
    Race_Length = (len(Race_Json["Races"])-1)
    Race = (Race_Json["Races"][randint(0,Race_Length)])
    SubRace_Length = (len(Race_Json[Race])-1)
    SubRace = (Race_Json[Race][randint(0,SubRace_Length)])
    return Race, SubRace

def Generate_Name():
    Name_File = open("Names.json", "r")
    Name_Json = load(Name_File)
    Gender_Length = (len(Name_Json["Gender"])-1)
    Gender = (Name_Json["Gender"][randint(0,Gender_Length)]) 

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
    print ("Name: " + First_Name)
else:
    print ("Name: " + First_Name +" "+ Last_Name)
    
print ("Gender: " + Gender)

if SubRace == "N/A":
    print ("Race: "+ Race)
else:
    print ("Race: " + SubRace + " " + Race)

print ("Class: "+ Class)