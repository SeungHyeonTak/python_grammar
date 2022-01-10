# 파이썬 OOP에서 클래스란 무엇인지 설명해보시오.
# [클래스 강의1] : 변수와 리스트를 사용하여 캐릭터 정보를 저장하고 출력해보시오.
# [클래스 강의2] : 함수를 사용하여 각 캐릭터에 파워 레벨을 랜덤으로 부여하고 출력해보시오.
# [클래스 강의3] : 클래스를 만들어보시오.


# [1] : 변수
print('[ 변수를 사용한 캐릭터 정보 출력 ]')
person1_name = '홍길동'
person1_age = '20'
person1_power = '7'  # --- 파워는 1~9 사이에서 랜덤으로 결정 --;;

person2_name = '이순신'
person2_age = '30'
person2_power = '9'

print(f'귀하가 선택하신 {person1_name} 캐릭터의 나이는 {person1_age}살이고 파워는 레벨 {person1_power} 입니다.')
print(f'귀하가 선택하신 {person2_name} 캐릭터의 나이는 {person2_age}살이고 파워는 레벨 {person2_power} 입니다.')
print('-' * 140)

# [2] : 리스트 또는 딕셔너리
# 딕셔너리 타입을 사용하면 리스트 보다는 더 효율적으로, 더 체계적으로 데이터 핸들링을 할 수는 있다.
print('[ 리스트를 사용한 캐릭터 정보 출력 ]')
person1 = ['홍길동', 20, 7]
person2 = ['이순신', 30, 9]

print(f'귀하가 선택하신 {person1[0]} 캐릭터의 나이는 {person1[1]}살이고 파워는 레벨 {person1[2]} 입니다.')
print(f'귀하가 선택하신 {person2[0]} 캐릭터의 나이는 {person2[1]}살이고 파워는 레벨 {person2[2]} 입니다.')
print('-' * 140)

# [3] : 각 캐릭터의 파워 레벨을 랜덤으로 정해줘야 한다면..??? --> 함수 사용
print('[ 함수와 리스트를 사용한 캐릭터 정보 출력 ]')
# ------------------------------------------
import random


def add_power_level(c_id):
    c_id[2] = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    return c_id


# ------------------------------------------

print(person1, person2)  # --- 함수 호출전 --;;
print(add_power_level(person1), add_power_level(person2))  # --- 함수 호출후 --;;
print('-' * 140)

# [4] : 클래스 생성
# 클래스를  사용하면 변수와 함수를 하나로 묶어서 데이터를 굉장히 효율적이면서 더 체계적으로 핸들링 할 수 있다.
# 클래스 내부에서 여러 다양한 변수나 함수가 정의되고 사용되는데 이를 --> 클래스 멤버
# 대표적인 클래스 멤버 --> 변수, 메서드
# 메서드 --> 클래스의 행위나 동작을 구현 --> 함수 --> 클래스에서는 메서드라고 호칭하는 것 뿐임.

# 클래스 작성
# (1) 클래스 작성 --> class 키워드로 선언하고 클래스명 지정.
# (2) 클래스 이름 --> 관례적으로 CamelCase --> 파이썬은 보통 단어 사이에 _를 넣는 편이나 클래스명은 카멜케이스를 따른다.
# (3) 함수가 아니기 때문에 클래스명 뒤에 () 괄호를 하지 않고 바로 콜론(:)을 붙여 종료한다.
# (4) 클래스 선언과 클래스명만 지정하고 바디는 pass 설정만 해놓아도 하나의 클래스가 만들어진다. --> pass는 테스트 용도로 많이 쓰인다.
print('[ 클래스 생성 ]')


# ----------------------------------------
class PersonInfo:
    pass  # --- 테스트시 많이 사용. 없으면 에러 --;;
# ----------------------------------------

# 클래스란 무엇인가?
# 클래스는 이제 하나의 데이터 오브젝트(캐릭터)를 만들어내는 '공장'을 지은거라고 생각하면 된다.
# 이 공장(클래스)을 통해서 우리는 손쉽게 각각의 Person 캐릭터 객체들을 만들어낼 수 있다.