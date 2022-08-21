N = input().strip()
M = int(input())
numbers = [True for _ in range(10)]
if M > 0:
    broke = map(int, input().split())
    for i in broke:
        numbers[i] = False

channel = None
for i in range(int(N), 1000001):
    flag = True
    for j in str(i):
        if not numbers[int(j)]:
            flag = False
            break
    if flag:
        channel = i
        break
for i in range(int(N), -1, -1):
    flag = True
    for j in str(i):
        if not numbers[int(j)]:
            flag = False
            break
    if flag:
        if not channel or int(N) - i + len(str(i)) < int(channel) - int(N) + len(str(channel)):
            channel = i
        break

if channel is not None:
    print(min(abs(int(N) - 100), len(str(channel)) + abs(int(N) - channel)))
else:
    print(abs(int(N) - 100))
