# 학생들의 영어 점수를 오름차순으로 출력하는 코드를 구현하시오.
# 영어 점수는 리스트로 구성한다.
# 내림차순도 구현해본다.


# [1] : 영어 점수
eng_scores = [100, 30, 80, 90, 50]

# [2] : 정렬 --> sort() 또는 sorted() 함수 사용 --> 정렬은 디폴트가 오름차순.
# eng_scores.sort()
eng_scores.sort(reverse=True)  # --- 오름차순 --> 내림차순 --;;

# [3] : 반복문을 사용해서 출력하기
for i in range(len(eng_scores)):
    print(eng_scores[i], end='\t')

print()
