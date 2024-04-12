import sys
from collections import deque
input =sys.stdin.readline
N, M = map(int, input().split())

q = deque()
maze = []
for _ in range(N):
    maze.append(list(map(int, input().rstrip())))

def bfs(x, y):
    # 상 하 좌 우 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))

    return maze[N-1][M-1]

print(bfs(0,0))