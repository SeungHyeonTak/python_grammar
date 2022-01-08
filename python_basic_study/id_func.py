# id 함수에 대해서
a = '붕어빵'
print(a, id(a))

b = a
print(b, id(b))  # a와 동일하다. (a가 가르키고 있는 메모리를 그대로 b가 가르키고 있기때문에 주소 값이 변경되지 않는다.)

a = '잉어빵'
print(a, id(a))
