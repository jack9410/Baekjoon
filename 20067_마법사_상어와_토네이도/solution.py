def map_prnt(map):
    for i in map:
        print(i)

def InBound(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False

def move 

N = int(input())
map = [list(input().split()) for _ in range(N)]
# map_prnt(map)

direction = [(0,1), (1,0), (0,-1), (-1,0)]

curr_x, curr_y = N//2 + 1, N//2+1



