import sys
from collections import deque

input = sys.stdin.readline

h, w = map(int, input().split())  #지도의 크기를 입력받는다.
arr = [list(map(str, input())) for _ in range(h)]

answer = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'W': #바다라면 무시
            continue
        vis = [[False] * w for _ in range(h)] #방문을 체크할 배열을 만들어준다
        q = deque()
        q.append([i, j, 0]) #큐에 탐색할 좌표를 넣어준다
        vis[i][j] = True  #방문했음을 알린다. 
        while q: #큐에 들어있는 동안은
            x, y, value = q.popleft() #시작점부터 탐색시작
            answer = max(answer, value) #현재값과 이전에 저장한 값중 큰것을 저장
            for k in range(4): #상하좌우 4방향 탐색
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 'L' and not vis[nx][ny]: #방향이 유효하고 육지이면서 방문을 하지 않았을때
                    q.append([nx, ny, value + 1]) #좌표넣어주고 걸린시간 +1
                    vis[nx][ny] = True #방문체크

print(answer)