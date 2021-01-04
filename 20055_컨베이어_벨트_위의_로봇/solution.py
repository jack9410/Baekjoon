# deque rotate 메소드 알기

from collections import deque

N, K = map(int, input().split())
A = deque(map(int, input().split()))
answer = 1

print(N, K)
print(A)

while True:
    # 1. 벨트가 한 칸 회전한다.
    A.rotate(1)
    
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.


    # 3. 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.

    # 4. 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.

    answer += 1

print(answer)