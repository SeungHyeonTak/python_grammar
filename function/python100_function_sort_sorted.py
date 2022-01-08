# 오름차순, 내림차순 정렬을 sort(), sorted() 함수로 구현하시오.
# sort(), sorted() 함수의 차이점을 아는지 묻는 문제이다.


# [1] : 리스트
lst = [100, 50, 70, 88, 65]

# [2] : sort() 함수를 이용한 오름차순, 내림차순 정렬
# sort() 함수나 sorted() 함수나 아무런 옵션 없이 사용하면 디폴트 정렬 --> 오름차순
# lst.sort()  #--- 오름차순 --;;
lst.sort(reverse=True)  # --- 먼저 오름차순으로 정렬이 되고나서 내림차순으로 정렬 --;;
# print( '[원본] : ', lst )

# [3] : sorted()
# reverse 옵션을 안쓰면 디폴트가 False가 되므로 기본 정렬 --> 오름차순 --> reverse=False
asc_ = sorted(lst)  # --- 원본 배열인 lst 리스트는 그대로 유지 --;;
# print( '[변경]', asc_ )
# print( '[원본] : ', lst )


# [4] : sorted() --> 내림차순
desc_ = sorted(lst, reverse=True)  # --- reverse 옵션을 True 주면 내림차순 정렬. 먼저 오름차순으로 정렬 후 내림차순으로 정렬 --;;

# [5] : 출력
print('[1] sort() 함수로 정렬 : ', lst)  # --- 내림차순 --;; [ 100, 88, 70, 65, 50 ]
print('[2] sorted() 함수로 정렬 : ', asc_, desc_)
