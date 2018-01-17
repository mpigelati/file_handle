import json

with open("Dev.json","r") as fd:
    data=json.load(fd)
    #print(type(data))
    #print(data["AddNewAPN"]["ipv4"])

fs=open("new_test.txt","w")

fd= open ("test.txt","r")
for line in fd:
    #print(line)
    print(line.rstrip())
    #print(line)






