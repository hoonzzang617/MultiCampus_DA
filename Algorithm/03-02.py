## 함수 
# 데이터 추가 함수
def add_data(friend):
    # 1단계 : 빈칸 추가
    katok.append(None)
    # 2단계 : 배열의 길이를 파악
    kLen = len(katok)
    # 2단계 : 마지막 칸에 친구 넣기
    katok[kLen-1] = friend

#데이터 삽입 함수
def insert_data(position, friend):
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 반복문 처리
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계 : 미나를 넣기
    katok[position] = friend

# 데이터 삭제 함수
def delete_data(position):  # 4
    # 1단계 : 그 위치 지우기
    katok[position] = None
    kLen = len(katok)
    # 2단계 : 지운 위치 다음부터, 마지막 친구까지 한칸씩 앞으로
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    # 3단계 : 마지막 칸을 완전히 제거
    del(katok[kLen-1])
    


## 전역
katok = []



## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)

delete_data(4)
print(katok)
