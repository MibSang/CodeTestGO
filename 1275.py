N, Q = map(int, input().split())
numbers = list(map(int, input().split()))

DP = [[None for _ in range(N)] for _ in range(N)]
DP_change = [0 for _ in range(N)]
for i in range(N):
    DP[i][0] = numbers[i]
for j in range(1, N):
    for i in range(0, N-j):
        DP[i][j] = DP[i][0] + DP[i+1][j-1]

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    x, y, a = x-1, y-1, a-1 # n번째 == n-1 index
    print(DP[x][y-x] + sum(DP_change[x:y]))
    DP_change[a] += b - numbers[a]
