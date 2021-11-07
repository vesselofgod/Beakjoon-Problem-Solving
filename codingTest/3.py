import heapq

n = int(input())
total_list = []
for i in range(n):
    start, end = map(int, input().split())
    total_list.append([start, end])

total_list.sort()
classroom = []
heapq.heappush(classroom, total_list[0][1])
for i in range(1, len(total_list)):
    if total_list[i][0] < classroom[0]:
        heapq.heappush(classroom, total_list[i][1])
    else:
        heapq.heappop(classroom)
        heapq.heappush(classroom, total_list[i][1])

print(len(classroom))







import sys
def reservation(meetingList) :
    result=0
    meetingList.sort()
    room=[]
    room.append(meetingList[0][1])
    for i in range(len(meetingList)):
        if(meetingList[i][0]<room[0]):
            #시작시간<수업 끝나는 시간-방1개 추가
            room.append(meetingList[i][1])
        else:
            room.pop()
            room.append(meetingList[i][1])
            
    result=len(room)
    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    meetingList = []

    for i in range(n) :
        data = [int(x) for x in input().split()]
        meetingList.append( (data[0], data[1]) )

    print(reservation(meetingList))

if __name__ == "__main__":
    main()


    '''
    회의 일정이 list로 주어질 때, 엘리스씨가 준비해야 하는 회의실의 수의 최솟값을 반환하는 함수를 작성하세요.

    각 일정은 tuple로 주어진다. 예를 들어, 주어진 입력의 경우 다음과 같이 저장된다.
    
    meetingList[0] = (1, 4)
    meetingList[1] = (3, 5)
    meetingList[2] = (2, 7)
    meetingList[3] = (4, 6)
    '''