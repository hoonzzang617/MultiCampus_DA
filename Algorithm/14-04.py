## 함수
def countDown(n):
    if n == 0:
        print('발사!')
    else:
        print(n)
        n -= 1
        countDown(n)



## 메인
countDown(5)
