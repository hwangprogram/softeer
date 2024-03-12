import sys
import copy
input = sys.stdin.readline


dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
path = []
def dfs(x, y, sec, sm):
    global fruit, route
    # 기저조건: 3초 지나면 종료
    if sec == 3:
        if fruit < sm:
            fruit = sm
            route = copy.deepcopy(path)
        return

    vis[x][y] = 1

    # 재귀
    for _x, _y in dt:
        nx, ny = x + _x, y + _y

        if (0 <= nx < N) and (0 <= ny < N) and not vis[nx][ny]:
            # 방문처리
            path.append((nx, ny))
            dfs(nx, ny, sec+1, sm+trees[nx][ny])
            path.pop()

    vis[x][y] = 0


order = []
orders = []
def sets():
    global orders
    # 기저조건: 순서 길이가 M이 되면 return
    if len(order) == M:
        orders.append(copy.deepcopy(order))
        return

    for i in range(0, M):
        if not visited_lst[i]:
            visited_lst[i] = 1
            order.append(i)
            sets()
            order.pop()
            visited_lst[i] = 0


# NxN크기의 격사, M명의 친구
N, M = map(int, input().split())
# 나무들 이차원리스트
trees = [list(map(int, input().split())) for _ in range(N)]

og_trees = copy.deepcopy(trees)
ans = 0
visited_lst = [0]*(M+1)
vis = [[0]*(N) for _ in range(N)]
friends = []

# 친구들의 위치를 각각 튜플로 하는 배열을 받는다
for _ in range(M):
    friends.append(tuple(map(int, input().split())))

# 수열 만들기 (친구들의 순서)
sets()

# 먼저 할 친구 결정해서 완전탐색
for o in orders:
    mx_fruit = 0
    trees = copy.deepcopy(og_trees)
    for i in o:
        route = []
        fruit = 0
        # 최대값 경로 찾기
        dfs(friends[i][0]-1, friends[i][1]-1, 0, 0)
        route.append((friends[i][0]-1, friends[i][1]-1))

        for x, y in route:
            mx_fruit += trees[x][y]
            trees[x][y] = 0
    if ans < mx_fruit:
        ans = mx_fruit

print(ans)