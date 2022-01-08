# 리스트 컴프리헨션(list comprehension)이란 무엇인지 예제를 통해 설명해보시오.
# 이 문제는 파이썬에서 굉장히 많이 사용되는 list comprehension 사용법과 개념에 대해서 알고 있는지를 묻는 문제이다.
# 파이썬 외에도 판다스, 넘파이 등 데이터 분석 분야에서도 굉장히 많이 사용되는 문법이므로 중요하다.
# 추가로.. 람다식과 같이 사용하는 방법도 알고 있어야 한다.


# [ ! ] : comprehension
# 컴프리헨션 넌 도대체 뭐냐? --> 사실 단어의 사전적인 의미만 알고 있어도 개념은 다 끝났다. --> 영어 사전을 검색.
# 결국 comprehension 개념은 보다 더 쉽게 만들어 쓰자는 것이다. --> list 또는 그 외의 것들도..(set, dict)
# 따라서, 대표로 list 관련한 comprehension을 잘 알아두면 다른 타입의 comprehension도 쉽게 이해할 수 있다.
# 수동 리스트 생성 방식과 for 문을 사용한 list comprehension 방식을 비교해보자.


# [1] : 수동 리스트 생성 --> 1~10까지의 요소를 갖는 리스트 생성
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('[1] 수동으로 리스트 생성 --> ', a, type(a))
print('-' * 140)

# for 반복문
for i in range(1, 11):
    print(i, end=' ')
print()
print('-' * 140)

# [2] : for 반복문 --> 빈 리스트 --> append
b = []
for aaa in range(1, 11):
    b.append(aaa)  # --- 1 ~ 10까지

print('[2] 자동으로 리스트 생성 --> ', b, type(b))

# [3] : list comprehension
c = [x for x in range(1, 11)]
print('[3] 자동으로 리스트 생성 list comprehension --> ', c, type(c))
