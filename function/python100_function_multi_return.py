# 가변길이 입력 파라미터 값들을 함수로 넘겨서 해당 파라미터의 갯수와 홀수들의 합을 구하는 코드를 구현하시오.
# 함수의 리턴은 항상 하나의 값을 반환한다. 
# 그러나 여러개의 값을 리턴하는 경우도 구현할 수 있는데 이러한 예제와 그때의 리턴 자료형은 무엇인지를 묻는 문제이다.
# 아래 코드의 결과로 출력되는 자료형에 대해서 말해보시오.


# [1] : 함수의 리턴 --> 하나의 tuple --> 2개의 값
# -----------------------------------------------------
def my_func(*params):
    count_ = 0
    sum_ = 0
    for i in params:
        count_ += 1
        if i % 2 != 0:  # --- 나머지연산자를 사용하여 결괏값이 0과 같지 않은 홀수들의 합만 구함 --;;
            sum_ += i
    return count_, sum_


# -----------------------------------------------------


# [2] : 함수 호출
a, b = my_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = my_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

print('[2-1] 가변길이 입력 파라미터 갯수와 홀수 합은 : ', a, ',', b, type(a), type(b))  # --- a, b 변수 각각은 int --;;
print('[2-2] result 변수 하나로 리턴되는 결과의 값을 받으면 : ', result, type(result))  # --- 이때는 자료형이 tuple --;;
