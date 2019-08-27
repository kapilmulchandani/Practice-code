thisdict={
"I": 1,
"V": 5,
"X": 10,
"L": 50,
"C": 100,
"D": 500,
"M":1000
}
newvar = thisdict["D"]
print(thisdict)

romanString = "XXX"
sumnew = 0

for i in range(0, len(romanString)):
    if(i < len(romanString)-1):
        if(thisdict[romanString[i]] < thisdict[romanString[i+1]]):
            thisdict[romanString[i]] = -thisdict[romanString[i]]
    sumnew = sumnew + thisdict[romanString[i]]
print(sumnew)