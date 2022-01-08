# 딕셔너리 타입에 대해서 예제를 통해서 설명하시오.
# 딕셔너리 사용법을 잘 익혀놓자.


# [ ! ] :  딕셔너리(dict)가 뭐지..??? 사전..???
# 딕셔너리 자료형은 키(key)와 값(value)이 하나의 쌍으로 이루어진 데이터 값이다.
# 예를들면, { key : value } 이런식으로 key, value가 하나의 쌍을 이루어서 만들어지는 데이터 값이다.
# 즉, 딕셔너리는 데이터(key : value)를 연관지어서 배열의 형태로 저장할 수 있는 자료구조이다.

# [ ! ] : 딕셔너리 특징
# 순서없이 저장 --> 입력한 데이터 값에 접근할 때는 key를 참조하여 접근 --> index 접근이 불가능 --> dic[0] 이런거 에러!
# key 값은 중복도 안되고, 변경도 불가능하다. 그러나 중복된 key 값이 입력은 가능하나 기존 값이 대체되어 버린다.
# value 값은 중복이 가능하고, 변경도 가능하다.
# 데이터 입력을 숫자, 문자 외에도 리스트와 같은 배열 객체로도 입력이 가능하다.


# [1] : 딕셔너리 선언
dict_ = {}  # --- dict_ 라는 이름의 딕셔너리 자료형을 생성 --;;

# [2] : 데이터 입력
dict_['id'] = 'hong'
dict_['name'] = [1, 2, 3, 4, 5]
dict_['age'] = 20
dict_['hp'] = '010-1234-5678'
dict_['address'] = '서울시 영등포구 여의도동 한강아파트 1000동 1000호'

# [3] : 데이터 출력
print(dict_['id'])
print(dict_['name'])
print(dict_['age'])
print(dict_['hp'])
print(dict_['address'])
print('-' * 140)
print('[3] 한줄로 출력 : ', dict_['id'], dict_['name'], dict_['age'], dict_['hp'], dict_['address'])
print('-' * 140)

# [4] : 반복문을 사용한 데이터 출력 - key
for i in dict_.keys():
    print(i, end=' ')
print()
print('-' * 140)

# [5] : 반복문을 사용한 데이터 출력 - value
for i in dict_.values():
    print(i, end=' ')
print()
print('-' * 140)

# [6] : key, value 모두 출력 --> ( key, value ) 값이 하나의 쌍으로 묶여서 출력 --> tuple 자료형.
for i in dict_.items():
    print(i, type(i))
print()
print('-' * 140)

# [7] : 빈 딕셔너리 만들기
a = dict()
b = {}
print('[7-1]', a, type(a))
print('[7-2]', b, type(b))
print('-' * 140)

# [8] : 가독성
dict1 = {
    'name': '홍길동',
    'id': 'hongkildong',
    'age': 20
}
print('[8-1]', dict1)
print('[8-2]', dict1['name'])
print('[8-3]', dict1['id'])
print('-' * 140)

# [9] : 중첩 딕셔너리( Nested Dictionary )
dict2 = {
    'name': '을지문덕',
    'age': 30,
    'pastime': {
        'reading': 30,
        'walking': 60
    }
}
print('[9-1]', dict2)
print('[9-2]', dict2['pastime'])
print('[9-3]', dict2['pastime']['walking'])  # --- 60
print('-' * 140)

# [10] : 삽입, 수정, 삭제
dict3 = {
    'name': '홍길동',
    'id': 'hongkildong'
}
print('[10-1] 최초 : ', dict3)

dict3['age'] = 22  # --- 삽입 --;;
print('[10-2] 삽입 : ', dict3)

dict3['age'] = 33  # --- 수정 --;;
print('[10-3] 수정 : ', dict3)

del dict3['age']  # --- 삭제 --;;
print('[10-4] 삭제 : ', dict3)
print('-' * 140)
