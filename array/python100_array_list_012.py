# 2개의 리스트를 하나의 리스트로 묶는 병합 처리에 대한 코드를 구현하시오.
# 이 문제는 리스트와 리스트를 하나로 병합하는 방법에 대해서 아는지를 묻는 문제이다.


# [1] : a, b 2개의 리스트
a = [0, 1, 2, 3, 4]
b = [5, 6, 7, 8, 9]

# [2] : a, b 리스트 --> 하나로 병합 --> 더하기(+) 연산자 사용.
ab_plus = a + b
print('[2-1] a + b 병합 리스트 : ', ab_plus, len(ab_plus), '개 요소')

# [3] : a * b 병합 --> 지원 X --> 리스트 * 숫자하고의 곱셈은 가능.
ab_multiplication = a * 3
print('[2-2] a * 3 병합 리스트 : ', ab_multiplication, len(ab_multiplication), '개 요소')
