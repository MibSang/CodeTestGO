N = int(input())
DP = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N)]

for i in range(1, 10):
	DP[0][i][1 << i] = 1

for i in range(1, N):
	for j in range(1, 9):
		for k in range(1 << 10):
			DP[i][j][k|1<<j] = DP[i][j][k|1<<j] + DP[i-1][j-1][k] + DP[i-1][j+1][k]
	for k in range(1 << 10):
		DP[i][0][k|1<<0] += DP[i-1][1][k]
		DP[i][9][k|1<<9] += DP[i-1][8][k]

ans = 0
#for i in DP[-1]:
#	print(i)
for i in range(10):
	ans += DP[-1][i][1023]

print(ans % 1000000000)
