country = list(map(str, input().split()))

win_rate = []

for _ in range(6):
    A,B,W,D,L = map(str, input().split())
    win_rate.append([A,B,W,D,L])

print(country)
print(win_rate) 