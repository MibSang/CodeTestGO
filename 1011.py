T = int(input())

def sum_n(n):
    return n*(n+1)/2

for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x
    max_v = 1
    ans = 0
    while sum_n(max_v+1)+sum_n(max_v) <= dist:
        max_v += 1
    if sum_n(max_v)+sum_n(max_v-1) == dist:
        print(max_v*2 - 1)
    elif sum_n(max_v)*2 >= dist:
        print(max_v*2)
    elif sum_n(max_v)*2 < dist:
        print(max_v*2 + 1)

# test
