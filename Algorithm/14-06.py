## 함수
def gugu(dan, num):
    print(dan,'x',num,'=',dan*num)
    if num < 9:
        num += 1
        gugu(dan, num)


## 메인
for i in range(2,10):
    print(i,'단')
    gugu(i,1)