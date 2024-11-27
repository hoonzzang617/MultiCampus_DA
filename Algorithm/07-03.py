## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    # Case 1
    if (rear != SIZE-1):
        return False
    # Case 2
    elif (rear == SIZE-1 and front == -1):
        return True
    # Case 3 
    elif (rear == SIZE-1 and front != -1): # elif 말고 else라고 해도 됨, 그냥 명확하게 써놓기 위해 elif 사용
        for i in range(front+1, SIZE, 1):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False


    # else:
    #     for i in range(front+1, SIZE, 1):
    #         queue[i-1] = queue[i]
    #         queue[i] = None
    #     front -= 1 
    #     rear -= 1
    #     return False

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
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 텅 빔')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 텅 빔')
        return
    return queue[front+1]    

## 변수
SIZE = 5
queue = [None for i in range(SIZE)]
front = rear = -1


## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<----', queue, '<----입구')

retData = deQueue()
print('식사 손님 :', retData)
retData = deQueue()
print('식사 손님 :', retData)

enQueue('재남')
enQueue('뷔')
print('출구<----', queue, '<----입구')

enQueue('길동')
print('출구<----', queue, '<----입구')