
'''
import sys
import copy
from collections import deque

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

def convert_board(board, x, y):
    ret = copy.deepcopy(board)

    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < 3 and 0 <= ny < 3):
            #이거 판 크기에 맞게 바꾸기
            if(ret[nx][ny]==0):
                ret[nx][ny]=1
            elif(ret[nx][ny]==1):
                ret[nx][ny]=0
    return ret


def bfs(goal):
    time = 0
    init_board = [[0] * 3 for _ in range(3)]
    visit = [0] * 1000

    q = deque([init_board])
    visit[init_board] = 1

    while q:
        for _ in range(len(q)):
            board = q.popleft()
            if board == goal:
                return time

            for row in range(3):
                for col in range(3):
                    next_board = convert_board(board, row, col)
                    binary_code = convert_to_binary(next_board)

                    if not visit[binary_code]:
                        q.append(next_board)
                        visit[binary_code] = 1
        time += 1

def solution(testcase):
    time = bfs(testcase)

    return time

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        testcase = [list(sys.stdin.readline().strip()) for _ in range(3)]
        answer = solution(testcase)
        print(answer)
'''

'''
import sys
import copy
from collections import deque

sys.setrecursionlimit(100000)

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

def convertMap(board, y, x):
    ret = copy.deepcopy(board)
    maxX=len(ret[0])
    maxY=len(ret)
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < maxX and 0 <= ny < maxY):
            #이거 판 크기에 맞게 바꾸기
            #print("x:",nx,"y:",ny)
            if(ret[ny][nx]==0):
                ret[ny][nx]=1
            elif(ret[ny][nx]==1):
                ret[nx][nx]=0
    return ret

def convert_to_binary(board):
    binary_str = ''
    for y in range(len(board)):
        for x in range(len(board[0])):
            if(board[y][x] == 0):
                binary_str += '0' 
            else:
                binary_str += '1' 
    print(binary_str)
    res=int(binary_str, 2)
    print(res)
    return res

def flip(myMap, n, m) :
    #모든 칸을 흰색으로 바꾸기 위해 최소로 클릭해야 하는 횟수를 반환하는 함수를 작성하세요.
    click=0
    whiteMap = [[0] * m for _ in range(n)]
    visit = [0] * 1000000000
    print(1)
    q = deque([myMap])
    visit[convert_to_binary(myMap)] = 1
    print(2)
    while q:
        for _ in range(len(q)):
            board = q.popleft()
            if board == whiteMap:
                return click
            for y in range(n):
                for x in range(m):
                    next_board = convertMap(board, y, x)
                    print(next_board)
                    binary_code = convert_to_binary(next_board)
                    if not visit[binary_code]:
                        print("turn")
                        q.append(next_board)
                        visit[binary_code] = 1
        click += 1
    return click


def main():
    #이 부분은 수정하지 마세요.
    data = [int(x) for x in input().split()]

    n = data[0]
    m = data[1]

    myMap = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        myMap.append(line)
        
    print("result:",flip(myMap, n, m))

if __name__ == "__main__":
    main()
'''

import sys
import copy
from collections import deque

sys.setrecursionlimit(100000)

dx=[0,0,0,1,-1]
dy=[0,-1,1,0,0]
#bfs?
def convert_to_binary(board):
    binary_str = ''
    for y in range(len(board)):
        for x in range(len(board[0])):
            if(board[y][x] == 0):
                binary_str += '0' 
            else:
                binary_str += '1' 
    res=int(binary_str, 2)
    return res

def flipMap(curMap,y,x):
    n=len(curMap)
    m=len(curMap[0])
    copyMap=copy.deepcopy(curMap)
    for i in range(5):
        nx=x+dx[i]
        ny=y+dy[i]
        if(0<=nx<m and 0<=ny<n):
            if(copyMap[ny][nx]==0):
                copyMap[ny][nx]=1
            else:
                copyMap[ny][nx]=0
    return copyMap

def flip(myMap, n, m) :
    '''
    모든 칸을 흰색으로 바꾸기 위해 최소로 클릭해야 하는 횟수를 반환하는 함수를 작성하세요.
    '''
    visit = [0] * 1000000000
    makeMap=False
    click=0
    whiteMap=[[0] * m for i in range(n)]
    visit[convert_to_binary(myMap)] = 1
    q = deque()
    q.append(myMap)
    while(q):
        for i in range(len(q)):
            curMap=q.popleft()
            if(curMap==whiteMap):
                makeMap=True
                return click
            for y in range(n):
                for x in range(m):
                    nextMap=flipMap(curMap,y,x)
                    binary_code = convert_to_binary(nextMap)
                    print(nextMap)
                    if not visit[binary_code]:
                        q.append(nextMap)
                        visit[binary_code] = 1
        click+=1
    if(makeMap==False):
        return -1
    else:
        return click

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    n = data[0]
    m = data[1]

    myMap = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        myMap.append(line)

    print(flip(myMap, n, m))

if __name__ == "__main__":
    main()
