# 함수 호출시 입력 파라미터 값을 지정하여 함수를 호출하는 예제를 만들어보시오.


# [1] : 함수 호출시 입력 파라미터 지정
# ------------------------------------------
def my_func(id_, name_, strength):
    return id_, name_, strength


# ------------------------------------------


# [2] : 함수 호출
result = my_func(id_='batman', name_='배트맨', strength='900')
print(result, type(result))
