N, M = map(int, input().split(' ')) # N < 50, M < 50
C = [] # Castle
for i in range(N):
    C.append(input())

Xr = [] # indexs require guard
Yr = []
for i in range(N):
    if 'X' not in C[i]:
        Xr.append(i)
for j in range(M):
    is_guard = False
    for i in range(N):
        if 'X' == C[i][j]:
            is_guard = True
            break
    if not is_guard:
        Yr.append(j)
        
print(max(len(Yr), len(Xr))) # number of guard required
