q = int(input())
num = int(input())
arr1 = input().split()
arr2 = input().split()
for x in range(num):
    arr1[x] = int(arr1[x])
    arr2[x] = int(arr2[x])
total = 0
if (q == 2):
    arr1.sort()
    arr2.sort()
    arr2.reverse()
    for x in range(num):
        total+=max(arr1[x],arr2[x])
if (q == 1):
    arr1.sort()
    arr2.sort()
    for x in range(num):
        total+=max(arr1[x],arr2[x])
print(total)
