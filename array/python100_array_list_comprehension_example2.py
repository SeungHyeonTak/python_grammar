# a = [ i, j for i in range(3) for j in range(3)] <-- 왼쪽의 list comprehension 결과를 말해보시오.
# 이 문제는 중첩된 이중 for문에 대한 사용법과 진행 순서를 아는지를 묻는 문제이다.


# [1] : 중첩 for 반복문 --> 구구단
a = [(i, j) for i in range(2, 4) for j in range(1, 4)]
print(a)
