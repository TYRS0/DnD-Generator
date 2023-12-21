from random import randint, choice
from json import load



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



Class = Generate_Class()
Race, SubRace = Generate_Race()



if SubRace == "N/A":
    print (Race)
else:
    print (SubRace + " " + Race)

print (Class)