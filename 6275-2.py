import sys
from collections import deque
input = sys.stdin.readline

# 방향 정하는 함수
def heading(next_dir):
    global pos, commend
    direction_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
    next_dir_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
    current_dir = direction_map[pos]
    target_dir = next_dir_map[next_dir]

    # 방향 전환 로직
    turn_needed = (target_dir - current_dir) % 4
    if turn_needed == 0:
        commend += 'A'
    elif turn_needed == 1:
        commend += 'RA'
        pos = next_dir
    elif turn_needed == 3:
        commend += 'LA'
        pos = next_dir

# bfs
# staet_end[0]부터 시작해서, start_end[1]에 끝난다.
# 이동할 때 or 회전할 때 커맨드를 입력해야 한다.
dt = ((-1, 0, '^'), (0, 1, '>'), (1, 0, 'v'), (0, -1, '<'))
def bfs(x, y, dr):
    # 큐
    q = deque()

    # 시작지점 큐에 삽입
    q.append((x, y, dr))
    # 방문처리(.으로 바꿔줌)
    location[x][y] = '.'

    # 큐가 빌 때까지 순회를 반복
    while q:
        x, y, d = q.popleft()

        for _x, _y, direct in dt:
            # 다음으로 이동할 곳
            nx, ny = x + _x, y + _y
            n2x, n2y = x + _x * 2, y + _y * 2

            # 다음 갈 좌표들에 #가 있다면 이동
            # 이동할 수 없는 곳이라면
            if (0 <= n2x < H and 0 <= n2y < W
                    and location[nx][ny] == '#'):
                # 방문할 지점 append
                q.append((n2x, n2y, direct))
                # 방문처리(#을 .으로) -> 2칸이동이기 때문에
                location[nx][ny] = '.'
                location[n2x][n2y] = '.'
                heading(direct)


# 세로 크기 H, 가로 크기 W
H, W = map(int, input().split())

# 지도 location
location = [list(input().rstrip()) for _ in range(H)]

# 시작점, 끝점, 방향 찾기
si, sj = 0, 0
pos = ''
flag = False

for i in range(H):
    for j in range(W):
        if location[i][j] == '#':
            cnt = 0
            for _i, _j, dr in dt:
                ni, nj = i + _i, j + _j

                if 0 <= ni < H and 0 <= nj < W and location[ni][nj] == '#':
                    cnt += 1
                    pos = dr
            if cnt == 1:
                # 시작점 저장
                si, sj = i, j
                flag = True
                break
    if flag:
        break

# 커맨드
commend = ''

# bfs 탐색
bfs(si, sj, pos)

print(si+1, sj+1)
print(pos)
print(commend)