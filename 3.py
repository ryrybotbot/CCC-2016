def DFS():
    visited = []
    queue = [0]
    global Rs
    global phoRs
    end = 0
    while (len(queue)>0):
        next = queue.pop(0)
        if (next not in visited):
            if (next in phoRs):
                end = next
            visited+=[next]
            for x in range(len(Rs[next])):
                queue+=[Rs[next][x]]
    return(end)
import math
def SP(k):
    global Rs
    visited= []
    dists = [math.inf()]*(len(Rs))
    queue = [k]
    while(len(queue)>0):
        next = queue.pop(0)
        if (next not in visited):
            visited+=[next]
            for x in range(len(Rs[next])):
                queue+=[Rs[next][x]]

phoRs = []
data = input().split()
Rs=[[]for x in range( int(data[0]))]

data2 = input().split()
for x in range(int(data[1])):
    phoRs +=[int(data2[x])]
for x in range(int(data[0])-1):
    data2 = input().split()
    Rs[int(data2[0])]+=[int(data2[1])]
    Rs[int(data2[1])]+=[int(data2[0])]
#print(Rs)
#print(phoRs)
print(DFS())
