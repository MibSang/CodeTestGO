import decimal
from math import sqrt


def arithmetic_mean(L) -> decimal.Decimal:
    return sum(L) / len(L)

def variance(L, Ls) -> decimal.Decimal:
    return arithmetic_mean(Ls) + arithmetic_mean(L) * arithmetic_mean(L)

def square(x: decimal.Decimal) -> decimal.Decimal:
    return x * x


N, K = map(int, input().split())
Likes = list(map(decimal.Decimal, input().split()))
Likes_sq = list(map(square, Likes[:]))
min_var = variance(Likes, Likes_sq)

# note: VAR(X) = E[(X-m)^2] = E[X^2]-E[X]^2
for i in range(N - K + 1):
    AVG_DP = [arithmetic_mean(Likes[i:i + K])]
    sq_AVG_DP = [arithmetic_mean(Likes_sq[i:i + K])]
    min_var = min(min_var, sq_AVG_DP[-1] - AVG_DP[-1] * AVG_DP[-1])
    for j in range(i + K, N):
        AVG_DP.append((AVG_DP[-1] * (j - i) + Likes[j]) / (j - i + 1))
        sq_AVG_DP.append((sq_AVG_DP[-1] * (j - i) + Likes_sq[j]) / (j - i + 1))
        min_var = min(min_var, sq_AVG_DP[-1] - AVG_DP[-1] * AVG_DP[-1])

print("{:.11f}".format(sqrt(min_var)))
