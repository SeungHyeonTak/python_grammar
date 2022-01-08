# 역인덱스를 사용하여 영어 점수를 오름차순과 내림차순으로 출력시키시오.
# 영어 점수는 리스트로 구성한다.


# [1] : 영어 점수
eng_scores = [100, 40, 70, 90, 60, 55, 45, 85, 95, 25]

# [2] : 정렬 --> sort(), sorted()
eng_scores.sort(reverse=True)

# [3] : 반복문 사용해서 출력
start = -len(eng_scores)
last = -1

for i in range(start, last + 1):
    print(eng_scores[i], '(', i, ')', end='\t')

print()
