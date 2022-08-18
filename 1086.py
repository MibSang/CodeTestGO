from math import factorial

N = int(input())
S = []
for _ in range(N):
    S.append(int(input()))
K = int(input())

p, q = 0, factorial(N)