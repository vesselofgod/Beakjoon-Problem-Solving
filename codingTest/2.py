import sys

def getRect(heights) :
    '''
    n개의 판자의 높이가 주어질 때, 이를 적당히 잘라 얻을 수 있는 직사각형의 최대 넓이를 반환하는 함수를 작성하세요.
    '''
    result=0
    cur=0
    stack=[[0,heights[0]]]
    for i in range(len(heights)):
        cur=i
        while(stack and stack[-1][1]>heights[i]):
            cur,height=stack.pop()
            width=i-cur
            result=max(result,height*width)
        stack.append([cur,heights[i]])
    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getRect(data))

if __name__ == "__main__":
    main()
