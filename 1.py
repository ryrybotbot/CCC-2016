out = "A"
str1 = input()
str2 = input()
removed = 0
while ("*" in str2):
    x = str2.find("*")
    str2 = str2[0:x]+str2[x+1:]
    removed+=1
if (len(str2)+removed)==len(str1):
    while (len(str2)>0):
        if (str2[0] in str1):
            z = str1.find(str2[0])
            str1 = str1[:z]+str1[z+1:]
            y = str2.find(str2[0])
            str2 = str2[:y]+str2[y+1:]
        else:
            out = "N"
            break
else:
    out = "N"
print(out)
