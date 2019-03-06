num = int(input())
riceballs = input().split()
for x in range (num):
    riceballs[x]=int(riceballs[x])
counts = [[0 for x in range(200)] for y in range(200)]
for y in range(num):
    for x in range(num):
        counts[y][x]=-1

def can_range_be_combined(start, end):
    if (start == end)
        return(True)
    return(counts[start][end]!=-1)

def get_range_count(start,end):
    if (start == end):
        return(riceballs[start])
    return(count[start][end])

def search_combs(y, x):
    for x1 in range(x+1,y+1):
        xend = x-1
