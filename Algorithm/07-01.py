## 함수



## 변수
SIZE = 5
queue = [None for i in range(SIZE)]
front = rear = -1



## 메인


## enQueue()
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print('출구<----', queue, '<----입구')

## deQueue()
front += 1
retData = queue[front]
queue[front] = None
print('손님 이리로 :', retData)
front += 1
retData = queue[front]
queue[front] = None
print('손님 이리로 :', retData)
front += 1
retData = queue[front]
queue[front] = None
print('손님 이리로 :', retData)
print('출구<----', queue, '<----입구')


