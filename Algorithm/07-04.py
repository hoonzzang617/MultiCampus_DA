## 함수
def isQueueFull():
    global SIZE, queue, front, rear

    if (rear +1)%5 == front: ### % 가 킥이다 ! 
        return True
    else: 
        return False




def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear :
        return True
    else: 
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('큐 꽉 참')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 텅 빔')
        return
    front = (front +1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 텅 빔')
        return
    return queue[(front+1)%SIZE]    

## 변수
SIZE = 5
queue = [None for i in range(SIZE)]
front = rear = 0


## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<----', queue, '<----입구')

retData = deQueue()
print('식사 손님 :', retData)
print('출구<----', queue, '<----입구')
retData = deQueue()
print('식사 손님 :', retData)
print('출구<----', queue, '<----입구')
enQueue('재남')
enQueue('뷔')
print('출구<----', queue, '<----입구')

enQueue('길동')
print('출구<----', queue, '<----입구')