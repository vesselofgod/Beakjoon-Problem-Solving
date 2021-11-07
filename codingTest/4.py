import sys
sys.setrecursionlimit(100000)

def numStudents(n_nodes,myInput) :
    #학생들 사이의 친구관계가 myInput으로 주어질 때, 정원이가 퍼트린 소문을 듣게되는 학생의 수를 반환합니다.
    visited=[False] * (n_nodes+1)
    result = -1

    adj_list=[[] for i in range(n_nodes+1)]
    for i in range(len(myInput)):
        adj_list[myInput[i][0]].append(myInput[i][1])
        adj_list[myInput[i][1]].append(myInput[i][0])
        
    def dfs(v):
        visited[v]=True
        #print(str(v)+' ',end='')
        for w in adj_list[v]:
            if not visited[w]:
                dfs(w)
    dfs(1)
    for i in visited:
        if(i==True):
            result+=1
    return result

def main():
    #Do not change this code
    n_nodes = int(input())
    m_edges = int(input())

    myInput = []

    for i in range(m_edges) :
        line = [int(x) for x in input().split()]
        myInput.append(line)

    print(numStudents(n_nodes,myInput))

if __name__ == "__main__":
    main()
