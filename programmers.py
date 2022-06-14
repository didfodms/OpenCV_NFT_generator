INF = int(1e9)

def solution(n, edge):
    answer = 0
    
    # 인접 행렬 (연결되어 있는 것은 1로)
    matrix = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in edge:
        a, b = _[0], _[1]
        matrix[a][b] = 1
        matrix[b][a] = 1
        
    # 최단 거리 정보
    distance = [0] * (n + 1)
    
    # 플로이드 와샬 알고리즘
    # k는 거쳐가는 노드, i는 현재 노드(1으로 고정되었으므로 생략), j는 거리 계산할 노드
    for k in range(1, n + 1):
        for j in range(1, n + 1):
            distance[j] = min(matrix[1][j], matrix[1][k] + matrix[k][j])
    
    print(distance)
    # 결과 구하기
    distance.sort()
    
    maximum = distance[n]
    i = n
    while i > 0:
        if distance[i] == maximum :
            answer += 1
            i -= 1
        else :
            break
        
    print(distance)
    return answer

edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(6, edges))