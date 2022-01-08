# sort(), sorted() 두 함수의 차이점을 예제로 설명하시오
# 두 함수의 차이점을 아는지 묻는 문제이다.


# [1] : 리스트
lst = [100, 50, 70, 88, 65]

# [2] : sort()
a = lst.sort(reverse=True)
print(a)  # --- None --;;

# [3] : sorted()
b = sorted(lst)
print(b)
print('[원본] : ', lst)
