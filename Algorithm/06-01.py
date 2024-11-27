## 함수




## 변수
stack = [None, None, None, None, None]
top = -1



## 메인
print('바닥:',stack)

## push()
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'

print('바닥:',stack)

## pop()
retData = stack[top]
stack[top] = None
top -= 1
print('팝 :', retData)

retData = stack[top]
stack[top] = None
top -= 1
print('팝 :', retData)

retData = stack[top]
stack[top] = None
top -= 1
print('팝 :', retData)
print('바닥:',stack)


