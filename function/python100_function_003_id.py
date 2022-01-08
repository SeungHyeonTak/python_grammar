# 변수의 메모리 주소값을 출력하여 다른 함수내 같은 변수의 값들이 어떤 주소를 가지고 있는지 출력하시오.


# [1] : 함수 작성
# ------------------------------------
def a():
    result = '붕어빵'
    result_loc = id(result)
    return result_loc


def b():
    result = '개구리빵'
    result_loc = id(result)
    return result_loc


# ------------------------------------


# [2] : 함수 호출
print('[2-1] a() 함수내 result 변수의 메모리 주소 : ', a())
print('[2-2] b() 함수내 result 변수의 메모리 주소 : ', b())
