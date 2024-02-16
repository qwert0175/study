# swea 노드의 거리

'''
V, E : 1~V번까지 V개의 정점, E개의 간선
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(s, V, G):  # 시작정점 s, 노드개수 N
    q = []
    visited = [0] * (N+1)
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        if t == G:
            return visited[t] - 1
        for i in adjl[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
    return 0

T = int(input())
for test_case in range(1,T+1):
    V, E = map(int,input().split())
    arr = [[] for _ in range(V+1)]

    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int,input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    S, G = map(int,input().split())

    print(f'#{test_case} {bfs(1,V,G)}')