import re
import sys

stageWords = ["Enter", "Re-enter", "Exeunt", "Alarums", "Exit"]

def isStageLine(line):
    for word in stageWords:
        if word in line:
            return True
    return False

with open("plays/" + sys.argv[1] + ".txt", "r") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines] 
        
with open("roles/" + sys.argv[2] + ".txt", "r") as f:
    roles = f.readlines()
roles = [x.strip() for x in roles] 

ff = open("formattedPlays/" + sys.argv[1] + "Formatted.txt", "w")

isScene = False
isStart = True

for line in lines:
    
    if line == "":
        continue
    if line.startswith("ACT"):
        continue
    if line.startswith("SCENE"):
        isScene = True
        continue
    if isStageLine(line):
        continue
    
    if line in roles:
        isScene = False
        if not isStart:
            ff.write("\n")
        ff.write(line + ":\n")
        isStart = False      
        
    elif isScene == True:
        continue
    else:
        ff.write(line + "\n")
        
ff.close
