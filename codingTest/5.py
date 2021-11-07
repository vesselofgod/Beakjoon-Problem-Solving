'''
import sys
input = sys.stdin.readline

 
 
num=0
for i in range(len(Elist)):
    if(Elist[i][2]<MIN):
        num+=1
for i in range(num):
    Elist.pop(0)

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]
 
answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if (sRoot > eRoot):
            Vroot[sRoot] = eRoot
        elif(sRoot < eRoot):
            Vroot[eRoot] = sRoot
        answer += w
 
print(answer)
'''
import sys
import heapq
sys.setrecursionlimit(100000)



def getPseudoMST(graph, c) :
    '''
    graph가 주어질 때, 간선의 가중치가 c 이상인 신장 트리 중 그 가중치가 최소가 되는 신장트리의 가중치의 합을 반환하는 함수를 작성하세요.
    '''
    result=0
    visited = [0] * (len(graph)+1)
    newGraph = [ [] for i in range(len(graph)) ]

    #c이하의 가중치 간선 지우기
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if(graph[i][j][1]>=c):
                newGraph[i].append((graph[i][j][1],i,graph[i][j][0]))

    visited[0]=1
    adjEdge = newGraph[0] # 인접 간선 추출
    heapq.heapify(adjEdge) # 우선순위 큐 생성
    MST = [] # mst

    while adjEdge:
        weight, u, v = heapq.heappop(adjEdge) # 가중치가 가장 적은 간선 추출
        if visited[v] == 0: # 방문하지 않았다면
            visited[v] = 1 # 방문 갱신
            MST.append((u,v)) # mst 삽입
            result += weight # 전체 가중치 갱신

            for edge in newGraph[v]: # 다음 인접 간선 탐색
                if visited[edge[2]] == 0: # 방문한 노드가 아니라면, (순환 방지)
                    heapq.heappush(adjEdge, edge) # 우선순위 큐에 edge 삽입
    return result

def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]
    c = line[2]

    graph = [ [] for i in range(n) ]

    for i in range(m) :
        line = [int(x) for x in input().split()]

        graph[line[0]].append((line[1], line[2]))
        graph[line[1]].append((line[0], line[2]))
    print(getPseudoMST(graph, c))
    
if __name__ == "__main__":
    main()