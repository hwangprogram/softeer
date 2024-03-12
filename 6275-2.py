import sys
from collections import deque
input = sys.stdin.readline

# 방향 정하는 함수
def heading(dr):
    global pos, commend
    # 위를 바라보고 있는 상황
    if pos == '^':
        if dr == '<':
            commend += 'LA'
            pos = '<'
        elif dr == '>':
            commend += 'RA'
            pos = '>'
        elif dr == '^':
            commend += 'A'
    # 왼쪽
    elif pos == '<':
        if dr == 'v':
            commend += 'LA'
            pos = 'v'
        elif dr == '^':
            commend += 'RA'
            pos = '^'
        elif dr == '<':
            commend += 'A'
    # 오른쪽
    elif pos == '>':
        if dr == '^':
            commend += 'LA'
            pos = '^'
        elif dr == 'v':
            commend += 'RA'
            pos = 'v'
        elif dr == '>':
            commend += 'A'
    # 아래
    elif pos == 'v':
        if dr == '>':
            commend += 'LA'
            pos = '>'
        elif dr == '<':
            commend += 'RA'
            pos = '<'
        elif dr == 'v':
            commend += 'A'

# bfs
# staet_end[0]부터 시작해서, start_end[1]에 끝난다.
# 이동할 때 or 회전할 때 커맨드를 입력해야 한다.
dt = ((1, 0, 'v'), (-1, 0, '^'), (0, 1, '>'), (0, -1, '<'))
def bfs(x, y):
    global commend, pos

    # 큐
    q = deque()

    # 시작지점 큐에 삽입
    q.append((x, y))
    # 방문처리(.으로 바꿔줌)
    location[x][y] = '.'

    # 큐가 빌 때까지 순회를 반복
    while q:
        x, y ,dr = q.popleft()

        # 종료지점이라면
        if x == start_end[1][0] and y == start_end[1][1]:
            return

        for _x, _y, direct in dt:
            # 다음으로 이동할 곳
            nx, ny = x + _x, y + _y
            n2x, n2y = x + _x * 2, y + _y * 2

            # 다음 갈 좌표들에 #가 있다면 이동
            # 이동할 수 없는 곳이라면
            if nx < 0 or nx >= H or ny < 0 or ny >= W or (location[nx][ny] != '#' and location[n2x][n2y] != '#'):
                # pass
                continue
            # 방문할 지점 append
            q.append((n2x, n2y, direct))
            # 방문처리(#을 .으로) -> 2칸이동이기 때문에
            location[nx][ny] = '.'
            location[n2x][n2y] = '.'

    return 0    # 도착지점에 도달할 수 없다면


# 세로 크기 H, 가로 크기 W
H, W = map(int, input().split())

# 지도 location
location = [list(input().rstrip()) for _ in range(H)]

# 시작점, 끝점 찾기
start_end = []

for i in range(H):
    for j in range(W):
        if location[i][j] == '#':
            cnt = 0
            for _i, _j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + _i, j + _j

                if 0 <= ni < H and 0 <= nj < W and location[ni][nj] == '#':
                    cnt += 1
            if cnt == 1:
                # 시작점 저장
                start_end.append((i, j))

# 방향 찾기
pos = ''

si, sj = start_end[0][0], start_end[0][1]
for _i, _j, direction in ((1, 0, 'v'), (-1, 0, '^'), (0, 1, '>'), (0, -1, '<')):
    ni, nj = si + _i, sj + _j

    if location[ni][nj] == '#':
       pos = direction

# 커맨드
commend = ''

# bfs 탐색
bfs(si, sj)

print(commend)