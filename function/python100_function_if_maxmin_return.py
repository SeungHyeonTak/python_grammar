# 한 반의 학생들 10명에 대한 영어 점수표가 리스트로 있다.
# 함수를 만들어 영어 점수표를 함수로 전달하면 최고 점수와 최저 점수가 동시에 나오도록 구현해본 것이다.
# (문제1) 아래 코드의 결과를 말해보시오. 
# (문제2) 만약 예상한 결과가 출력되지 않았다면 왜 그런지 이유를 말해보시오.

# [1] : 함수 작성
def max_min_in_list(lst):
    return min(lst)
    # return max(lst)


# [2]  : 영어 점수표 --> list
english_score = [35, 90, 58, 30, 98, 56, 89, 78, 91, 67]

# [3] : 함수 호출 및 결과 출력하기
result = max_min_in_list(english_score)
print(result)
