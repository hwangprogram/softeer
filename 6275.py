'''
Softeer 6275 로봇이 지나간 경로

1. 2중 for문으로 배열을 돌면서 #을 만나면 거기서부터 DFS 시작
2. 4방향 탐색하며 내가 서 있는 칸 보다 두칸 뒤에 #이 있는지 확인
3. #이 있다면 전진, 없다면 return
4. 처음에 방향을 정하고, #가 안 나올 때까지 탐색을 해야한다.
5. #가 안 나오면 다음 방향으로 바꾸고, 그 방향으로 계속해서 탐색해야 함
'''
from collections import deque
import sys
input = sys.stdin.readline
dt = ((2, 0), (-2, 0), (0, 2), (0, -2))
def bfs(x, y):
    global commend

    # 큐
    q = deque()

    # 시작지점 큐에 삽입
    q.append((x, y))
    # 방문처리(.으로 바꿔줌, 두칸 다)
    location[x][y] = '.'

    # 큐가 빌 때까지 순회를 반복
    while q:
        x, y = q.popleft()

        for _x, _y in dt:
            # 다음으로 이동할 곳
            nx, ny = x + _x, y + _y

            # 다음 갈 좌표들에 #가 있다면 이동
            # 이동할 수 없는 곳이라면
            if nx < 0 or nx >= H or ny < 0 or ny >= W or location[nx][ny] != '#':
                # pass
                continue
            # 방문할 지점 append
            q.append((nx, ny))
            # 방문처리(#을 .으로) -> 2칸이동이기 때문에
            location[x:nx][y:ny] = '.'
    return 0    # 도착지점에 도달할 수 없다면


# 세로 크기 H, 가로 크기 W
H, W = map(int, input().split())

location = [list(input()) for _ in range(H)]

# 명령 입력할 문자열
commend = ''

# 배열 순회하며 #찾아서 DFS 실시
for i in range(H):
    for j in range(W):
        if location[i][j] != '#':
            bfs(i, j)