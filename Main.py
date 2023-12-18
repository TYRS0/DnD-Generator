from random import randint, choice
from json import load

def Generate_Class():
    Class_File = open("Classes.json", "r")
    Class_Json = load(Class_File)
    Class_Length = (len(Class_Json)-1)
    Class = (Class_Json[randint(0,Class_Length)])
    return Class


Class = Generate_Class()


print (Class)