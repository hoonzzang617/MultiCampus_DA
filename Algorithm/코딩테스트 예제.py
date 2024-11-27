ARRAY_LENGTH = 5  # 배열의 행과 열 크기(고정)

def replaceData(numData): # numData	2차원 정수 배열
    retData = [] # 조건에 따라서 전처리된 2차원 배열

#     def isLowerThan0(num):
#         return 0

#     for array in df:
#         filteredList = list(map(lambda x: 0 if x < 0 else x, array))
#         filteredList = list(map(lambda x: x%100 if x > 100 else x, filteredList))
#         print(filteredList)

    ###########   여기부터 코딩 (1) ---------------->
    for array in numData:
        filteredList = list(map(lambda x: 0 if x < 0 else x, array))
        filteredList = list(map(lambda x: x%100 if x > 100 else x, filteredList))
        # print(filteredList)
        retData.append(filteredList)
    ###########   <-------------- 여기까지 코딩 (1)

    return retData


# 2x2 크기의 배열의 최대합을 구한다.
def getMaxSum(numData): # 요구 사항에 맞춰 처리된 2차원 정수 배열
    maxSum = 0 # 최대합

    ###########   여기부터 코딩 (2) ---------------->
    global head, current, pre

    def arrange(n1, n2):
        node1 = Node()
        node1.data = numData[n1][n2]
        head = node1

        node2 = Node()
        node2.data = numData[n1][n2+1]
        node1.link = node2

        node3 = Node()
        node3.data = numData[n1+1][n2+1]
        node2.link = node3

        node4 = Node()
        node4.data = numData[n1+1][n2]
        
        node_sum = node1.data + node2.data + node3.data + node4.data
        return node_sum, node1.data, node2.data, node3.data, node4.data

    n1, n2 = 0, 0
    while True:
        tmp_maxSum, tmp_data1, tmp_data2, tmp_data3, tmp_data4 = arrange(n1,n2)
        if maxSum < tmp_maxSum:
            maxSum = tmp_maxSum
            data1, data2, data3, data4 = tmp_data1, tmp_data2, tmp_data3, tmp_data4
        
        n2 += 1
        if n2 >= 4:
            n1 += 1
            n2 = 0
        
        if n1 >= 4:
             break
    print(data1, data2, data3, data4)
    ###########   <-------------- 여기까지 코딩 (2)

    return maxSum

## 전역 변수 선언 부분
numData =[] # 5x5 배열
ARRAY_LENGTH = 5 # 배열의 행과 열 크기(고정)
head, current, pre = None, None, None

class Node() :
    def __init__(self):
        self.data = None
        self.link = None


def main() :
        global numData

        loadData() # 2차원 배열 읽어오기

        ## 원본 출력
        print(' ----- 초기 배열 -----')
        printData()

        # 1. 데이터 치환 작업
        numData = replaceData(numData)
        print(' ----- 치환 후 배열 -----')
        printData()

        # 2. 최대 합 구하기.(2x2 크기)
        maxSum = getMaxSum(numData)
        print('최대 영역의 합: %d' % maxSum)

       
## 함수 선언 부분
def  loadData() : # 데이터 불러오기
    global numData

    ###########
    # 제공 데이터 세트 1 
    # 5x5 숫자 배열. 
    ###########
    numData = \
    [
        [ 5, 7, -5, 100, 73 ],
        [ 35, 23, 4, 190, 33 ],
        [ 49, 85, 662, 39, 81 ],
        [ 124, -59, 86, 46, 52 ],
        [ 27, 7, 8, 33, -56 ] 
    ]
    
    

def printData() :
        for i in range(0, ARRAY_LENGTH) :
                for k in range(0, ARRAY_LENGTH) :
                        try :
                                print("%5d" % numData[i][k], end='')
                        except :
                                pass
                print()
        print('--------------------------------------')

## 메인 함수 호출 ##
if __name__ == "__main__" :
    main()