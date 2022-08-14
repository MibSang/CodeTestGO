from math import sqrt, floor, ceil

MIN, MAX = map(int, input().split())
Ss = []
NoNoNums = [1 for _ in range(MIN, MAX+1)]

for i in range(2, floor(sqrt(MAX))+1):
    Ss.append(i*i)
# list of square numbers =< MAX

for i in Ss:
    count = ceil(MIN/i)
    while MIN <= i*count <= MAX:
        NoNoNums[i*count-MIN] = 0
        count += 1

#print(NoNoNums)
print(sum(NoNoNums))