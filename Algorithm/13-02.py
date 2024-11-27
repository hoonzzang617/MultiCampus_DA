## 함수
import random
def binSearch(ary, fdata):
    pos = -1
    start = 0
    end = len(ary)-1
    while start <= end :
        middle = (start + end) // 2
        if ary[middle] == fdata :
            pos = middle
            break
        elif ary[middle] < fdata :
            start = middle + 1 
        else : 
            end = middle - 1


    start = 0
    end = len(ary) -1
    while start <= end:
        middle = (start + end) // 2
        if ary[middle] == findData:
            pos = middle
            break
        elif any[middle] > findData:
            start = middle + 1
        else : 
            end = middle - 1 

    return pos


## 변수
dataAry = [random.randint(30, 190) for i in range(1000000)]
findData = random.choice(dataAry)
dataAry.sort()

## 메인
print('배열 -->', dataAry)
position = binSearch(dataAry, findData)
if position != -1 :
    print(findData,'는',position,'위치에 있음')
else:
    print(findData,'는 없음')






