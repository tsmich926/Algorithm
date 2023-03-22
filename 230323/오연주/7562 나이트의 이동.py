dr = [-1, -2, 1, 2, 1, 2, -1, -2]
dc = [2, 1, 2, 1, -2, -1, -2, -1]

def bfs(row, col):
    Q = []
    visited = [[0]*P for _ in range(P)]

    Q.append((row, col))
    visited[row][col] = 1

    while Q:
        r, c = Q.pop(0)
        for i in range(8):
            newR = r + dr[i]
            newC = c + dc[i]
            if 0<=newR<P and 0<=newC<P and not visited[newR][newC]:
                visited[newR][newC] = visited[r][c] + 1
                Q.append((newR, newC))
                if newR == m1 and newC == m2:
                    return visited[newR][newC]-1
    return 0





T = int(input())

for tc in range(T):
    P = int(input())
    lst = [[0] * P for _ in range(P)]
    n1, n2 = map(int, input().split())
    m1, m2 = map(int, input().split())

    print(bfs(n1, n2))