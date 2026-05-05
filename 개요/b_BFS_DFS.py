'''
DFS - 깊이 우선 탐색  -> 루투노드에서 출발하여 가장 깊은곳 까지 먼저 탐색하고 다시돌아와서
다른 경로를 탐색하는 알고리즘     # 주로 재귀호출 또는 스택을 사용    
BFS - 너비 우선 탐색  -> 루트노드에서 가장 인접한 노드로부터 우선적으로 탐색하는 알고리즘
# 주로 큐를 사용해서 구현


스택[LIFO] push(1) -> push(2) -> push(3)    // 꺼낼때 3 -> 2-> 1
==> 최근 거부터 처리  -> DFS
A - B - D
|   |
C   E
[1. a push // 2. a -> b push // 3. b -> d push  // 4. d 더 없음 -> pop // 5. 다시 b->e push]
a : b,c   b : d,e   이렇게 되면   a 들어가고 c(lifo니깐) 그러고 b  그리고 d,e 넣고 e부터 꺼냄
[인접 리스트] 
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

큐[FIFO] enqueue(1) -> enqueue(2) -> enqueue(3) -> // 꺼낼때 1 -> 2-> 3
==> 순서대로 처리
a -> b -> c -> d -> e
'''


# 간단한 인접 리스트 예시
graph = {'A':['B'], 
         'B':['C'],
         'C':['D'],
         'D':[]}

def bfs(graph,start):
    visited, queue = [start], [start]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited
