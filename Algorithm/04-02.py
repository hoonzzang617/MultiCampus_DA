## 함수 및 클래스
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while (current.link != None): # 핵심 ! current의 링크가 비지 않을 때 까지 !
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre
    # Case 1 : head 앞에 삽입하는 경우
    if head.data == findData: # 다현, 화사
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # Case 2 : 찾는 애가 중간에 있을 때 사나 찾고 솔라를 앞에
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == findData):
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # Case 3 : 찾는 애가 없을 때 마지막에 추가 하는 경우
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData):
    global memory, head, current, pre
    # Case 1 : head 노드를 삭제할 때 
    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return
    # Case 2 : 
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return   # 이게 없으면 current를 삭제했기 때문에 에러가 난다
    # Case 3 : 지울 데이터가 없을 때
    return

def findeNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    
    return Node()



## 변수
memory = [] # 노드를 보관할 메모리 (안 중요하고 다른 언어에서 사용되는 개념)
head, current, pre = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효'] # 실무에서 쓰일 데이터, 크기에 제한 없다


## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 안 중요! 생략 가능.

for data in dataArray[1:] :
    pre = node
    node = Node()  ## 까먹지 말기 ! 
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

# insertNode('다현', '화사') # 다현을 찾아서, 그 앞에 화사를 넣어라
#insertNode('사나', '솔라')
# insertNode('재남', '문별')

# deleteNode('다현')
# deleteNode('쯔위')
# deleteNode('재남')
# printNodes(head)


retNode = findeNode('사나')
print(retNode.data,'의 뮤비가 나옵니다.')










# node = Node()
# head = node
# node.data = dataArray[0]
# memory.append(node)

# for data in dataArray[1:]:
#     pre = node
#     node = Node()
#     node.data = data
#     pre.link = node
#     memory.append(node)

# printNodes(head)















