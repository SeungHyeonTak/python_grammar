# 아래 코드의 결과를 말해보고 타입은 무엇으로 나오는지 설명해보시오.
# 이 문제는 함수에서 리턴되는 값에 대해서 한개 또는 여러 개의 리턴 값이 어떻게 처리되는지를 아는지 묻는 문제이다.


# [1] : 함수 호출시 입력 파라미터 지정
# -------------------------------------
def my_func(id_, name_, power):
    return id_, name_, power


# -------------------------------------


# [2] : 함수 호출
result = my_func(id_='superman', name_='슈퍼맨', power=3000)
print('[2-1] 하나의 변수로 리턴값을 출력 : ', result, type(result))
print(result[2], type(result[2]))

a, b, c = my_func(id_='batman', name_='배트맨', power=4000)
print('[2-2] 여러개 변수로 리턴값을 받아서 출력 : ', a, b, c, ' - ', type(a), type(b), type(c))
