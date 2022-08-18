N = int(input())
DP = [[0 for _ in range(10)] for _ in range(N)]
for i in range(1, len(DP[0])):
    DP[0][i] = 1

for i in range(1, len(DP)):
    for j in range(1, 9):
        DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]
    DP[i][0] = DP[i-1][1]
    DP[i][9] = DP[i-1][8]
print(sum(DP[-1]) % 1000000000)
