## 함수
import random
def selectSort(ary):
    n = len(ary) # 데이터 개수
    for i in range(n-1): # 사이클 (큰 회전)
        minIdx = i
        for j in range(i+1, n) : # 작은 반복문
            if (ary[minIdx] > ary[j]):
                minIdx = j
        ary[i], ary[minIdx] = ary[minIdx], ary[i]  # 데이터 교환
    return ary        

## 변수
dataAry = [random.randint(30, 190) for i in range(4)]

## 메인
print('정렬전-->', dataAry)
dataAry = selectSort(dataAry)
print('정렬 후-->', dataAry)







