# 아래의 다양한 list comprehension 문제들을 코드로 구현하시오.
# [1] list comprehension 괄호([])를 사용하지 않고 list() 와 for 문으로 1~10까지의 리스트를 만들어보시오.
# [2] 1~10까지의 수를 list comprehension으로 각 숫자를 제곱한 값을 저장하는 리스트를 만들어보시오.
# [3] 위 2번 문제에서 5의 제곱 값은 제외하고 출력시키시오. (★★★)
# [4] list comprehension에서 if 조건문을 사용하여 1~50까지의 수에서 짝수, 홀수만 저장하는 리스트를 각각 만들어보시오.
# [5] list comprehension에서 함수를 사용하는 것이 가능한지 예제를 작성해보시오.


# [1] : for문 + list() --> 리스트 생성
for i in range(1, 11):
    print(i, end=' ')
print()

a = list(i for i in range(1, 11))  # --- 이렇게도 가능하구나.. 정도만 기억.. 당연히 권장은 a = [] <-- 이걸 권장 --;;
print('[1] for문 + list() 사용한 리스트 생성 : ', a)

# [2] : 1~10까지 수 --> 각 숫자를 제곱한 값 --> 리스트 생성
b = [i * i for i in range(1, 11)]
print('[2] 1~10까지의 수를 제곱한 값 --> ', b)

# [3] : 1~10까지 수 --> 제곱한 값 리스트 생성 --> 5제곱 값 제외 --> if 조건문 사용.
# 이 문제는 list comprehension에서 조건문을 사용시 어떤 순서대로 절차가 진행되면서 조건 비교가 되는지를 잘 이해해야 한다.
c = [i * i for i in range(1, 11) if i != 5]
print('[3] 1~10까지의 수를 제곱한 값에서 5제곱 값은 제외한 리스트 --> ', c)

# [4] : 짝수, 홀수 리스트 생성
d = [i for i in range(1, 51) if i % 2 != 0]
print('[4] 1~50까지의 수에서 홀수만 출력 --> ', d)


# [5] : 함수 사용
def my_func(i):
    i = i * 2
    return i


e = [my_func(abs(i)) for i in [1, 2, -3, 4, 5, -6, 7, 8, -9, 10]]
print('[5] 함수 사용 --> ', e)
