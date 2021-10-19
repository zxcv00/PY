# Quiz
# 3-1.주민등록번호 앞 6자리를 변수 id_number에 넣고,
# 출생년도 끝 두자리\n출생 월일\n그 두개의 곱 출력
# 예시
# id_number = 020316 일 때
# 출력 예시
# 02
# 0316
# 732
id_number = "020316"

print("출생년도 끝 두자리: " + id_number[:2])  # [0:2], [-6:-4]
print("출생월일: " + id_number[2:6])
print(int(id_number[:2]) * int(id_number[2:6]))

print("=======================================")

id_number = "020316"
year = id_number[0:2]
month_day = id_number[2:6]
print(year)
print(month_day)
print("둘의 곱: " + str(int(year) * int(month_day)))

print("=======================================")
# 3-2. 집 전화번호를 phone_number에 넣고,
# 지역번호\n맨 끝 네 자리 출력하기(지역번호의 자리수와 상관없이 동작하도록 하자)
# 예시
# phone_number = 02-1234-5678 또는 032-9876-4321
# 출력 예시
# 02 또는 032
# 5678 또는 4321
phone_number = "02-1234-5678"

print("지역 번호: " + phone_number[:phone_number.index("-")])
print("지역 번호 끝 네 자리: " + phone_number[-4:])

print("=======================================")
# index() 없으면 vlaueError, find() 없으면 -1
phone_number = "02-1234-5678"
print(phone_number[0:2])
print(phone_number[-4:])

phone_number2 = "032-1234-5678"
print(phone_number2[0:3])
print(phone_number2[-4:])

print("=======================================")
# 전화번호 입력시, -가 있든 -가 없든 찰떡같이 알아먹기
phone_number1 = '010-1234-5678'
phone_number2 = '01098765432'
phone_number3 = '010 1111 2222'

phone_number = phone_number1
result = phone_number.replace('-', '').replace(' ', '')
print(result)

print("=======================================")
# 2-1. 학번을 student_number 변수에 넣고, 학급을 출력하고, 학과를 출력하기
# 반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number = '2100' 또는 student_number = '2000'
# <출력 예시>
# 1반 뉴미디어소프트웨어과 또는 잘못 입력했습니다.
student_number = '2312'
num = int(student_number[1])  # str -> int
if 1 <= num <= 2:
    print(student_number[1] + "반 뉴미디어소프트웨어과")
elif 3 <= num <= 4:
    print(student_number[1] + "반 뉴미디어웹솔루션과")
elif 5 <= num <= 6:
    print(student_number[1] + "반 뉴미디어디자인과")
else:
    print("잘못 입력했습니다.")

print("=======================================")
student_number1 = '2000'
num = int(student_number1[1])
# majors = ['뉴미디어소프트웨어과', '뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']
# print(f'{num}반 {majors[num - 1]}')

majors = ['뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어디자인과']
if 1 <= num <= 6:  # 1 <= num && num <= 6 <- in java
    print(f'{num}반 {majors[(num - 1) // 2]}')
else:
    print("잘못입력했습니다.")

print("=======================================")
# 2-2. 학번을 함수의 인수(argument)로 전달하여 호출하면 학년과 학과를 리턴하는 함수 만들기
# <함수 호출>
# grade, major = get_major('2100')
# print(major, grade) #뉴미디어소프트웨어과 2
def get_major(argument):
    if argument[1] == "1" or argument[1] == "2":
        major = "뉴미디어소프트웨어과"
        return argument[0], major
    elif argument[1] == "3" or argument[1] == "4":
        major = "뉴미디어웹솔루션과"
        return argument[0], major
    elif argument[1] == "5" or argument[1] == "6":
        major = "뉴미디어디자인과"
        return argument[0], major
    else:
        print("잘못입력했습니다.")
        return argument[0]

grade, major = get_major("2312")
print(major, grade)

print("=======================================")
# 2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고, 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# <함수 호출>
# print(average(10, 20, 30)) #20.0
# print(average(4, 23)) #13.5
def ave(*insu):
    return (sum(insu) / len(insu))

print("평균: {0}".format(ave(10, 20, 30)))
print("평균: {0}".format(ave(4, 23)))

print("=======================================")

# 파이썬에는 이미 sum 이라는 변수가 있음
# 그래서 sum을 변수명으로 하면 안됨
def average(*numbers):
    sum_value = 0
    count = 0
    for number in numbers:
        sum_value += number
        count += 1
    return sum_value / count

print(average(10, 20, 30))  # (10, 20, 30) ==> numbers
print(average(4, 23))  # (4, 23) ==> numbers

print("=======================================")

def average2(*numbers):
    return sum(numbers) / len(numbers)

print(average2(10, 20, 30))
print(average(4, 23))

print("=======================================")
# Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고, 함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
# * BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
# 18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만
# <함수 호출>
# bmi = get_bmi(176, 69)
# print(bmi) #22.3
def get_bmi(height, weight):
    bmi = weight / (height * height)
    if bmi < 18.5:
        print("저체중")
        return weight / (height * height)
    elif 18.5 <= bmi < 23:
        print("보통")
        return weight / (height * height)
    elif 23 <= bmi < 25:
        print("과체중")
        return weight / (height * height)
    elif 25 <= bmi:
        print("비만")
        return weight / (height * height)

bmi = round(get_bmi(176 / 100, 69), 1)
print(bmi)

print("=======================================")

def get_bmi(height, weight):
    height /= 100
    return round((weight / height ** 2), 1)


bmi2 = get_bmi(176, 69)
# print(bmi2)

if bmi2 < 18.5:
    print('저체중')
elif bmi2 < 23:
    print('정상')
elif bmi2 < 25:
    print('과체중')
elif 25 <= bmi2:
    print('비만')

print("=======================================")
# 구구단 7단 출력
for i in range(1, 10):  # i: 1 ~ 9
    print(f'7 * {i} = {7 * i}')

print("=======================================")
# 구구단 2 ~9 단 출력
for dan in range(2, 10):  # dan: 2 ~ 9
    for i in range(1, 10):  # i: 1 ~ 9
        print(f'{dan} * {i} = {dan * i}')
    print('-' * 11)

print("=======================================")
# 구구단 2 ~ 7단까지 출력
for dan in range(2, 10):
    for i in range(1, 10):
        print(f'{dan} * {i} = {dan * i}')
    print('-' * 11)
    if dan == 7:
        break

print("=======================================")
# 구구단 2 ~ 7단을 출력하되, x1, x3, x5, x7, x9인 것만 출력
for dan in range(2, 10):
    for i in range(1, 10):
        if i % 2 == 0:  # i == 2 or i == 4 or i == 6 or i == 8:
            continue
        print(f'{dan} * {i} = {dan * i}')
    print('-' * 11)
    if dan == 7:
        break

print("=======================================")
# Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 10자리 숫자보다 작은 숫자를 넣으면,
# 각 자리의 숫자의 합계를 리턴한다. 10자리 이상이면 -1 리턴한다.
'''
result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1
'''

def n_sum(argument):
    if argument < 10:
        return argument
    elif len(str(argument)) >= 10:
        return -1
    else:
        return argument % 10 + int(n_sum(argument / 10))  # 408: 8 + int(n_sum(40.8))    #n_sum(40.8): 0.8+int(n_sum(4.08))  #n_sum(4.08): 4.08

result = n_sum(10)
print(result)  # 1
result = n_sum(331)
print(result)  # 7
result = n_sum(408)
print(result)  # 12
result = n_sum(1000000000)
print(result)  # -1

print("=======================================")
# Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
'''
fare = get_subway_fare(5)
print(fare)        #720
fare = get_subway_fare(26)
print(fare)        #1120
fare = get_subway_fare(61)
print(fare)        #1720
'''
import math

def get_subway_fare(km):
    money = 720
    ttf = money + math.ceil((km - 10) / 5) * 100
    moreFifty = money + (50 - 10) // 5 * 100 + math.ceil((km - 50) / 8) * 100
    if km < 10:
        return int(720)
    elif 10 < km <= 50:
        return int(ttf)
    elif km > 50:
        return int(moreFifty)

fare = get_subway_fare(5)
print(fare)  # 720
fare = get_subway_fare(26)
print(fare)  # 1120
fare = get_subway_fare(61)
print(fare)  # 1720

print("=======================================")
# Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
# * 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
# 힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음
'''
result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)        #짝짝
'''

def get_three_six_nine(num):
    count = str(num).count('3') + str(num).count('6') + str(num).count('9')
    if count == 0:
        return num
    else:
        return "짝" * count

result = get_three_six_nine(1)
print(result)  # 1
result = get_three_six_nine(3)
print(result)  # 짝
result = get_three_six_nine(16)
print(result)  # 짝
result = get_three_six_nine(36)
print(result)  # 짝짝

print("=======================================")
'''
Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
1. 함수의 이름을 정해준다.
2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
3. 리턴하는 것을 말해준다.
4. 출력 예시를 보여준다.
5. 내가 낸 문제의 답안을 제출한다.
'''
'''
finding_height() 함수에 인수로 부모님의 키를 넣어 딸의 예상 키를 구한 후 
예상 키가 고등학교 2학년 기준 평균인지 평균 이하인지 이상인지 구하는 프로그램
>> 소수 첫째자리까지 나타내기
여자 아이 예측 키(cm) 구하는 공식 = (엄마 키 + 아빠 키) / 2 - 6.5(cm) 
(학년별 평균 키 - 교육부 2020.7 발표)
고등학교 2학년 여자 평균 키 => 161.2(cm)

출력 예시
height = finding_height(162.7, 178)
print(height) # 163.8
'''
# 풀이
def finding_height(height_m, height_d):
    dau_height = (height_m + height_d) / 2 - 6.5
    if dau_height > 161.2:
        print("평균 이상입니다.")
        return (height_m + height_d) / 2 - 6.5
    elif dau_height == 161.2:
        print("평균입니다.")
        return (height_m + height_d) / 2 - 6.5
    else:
        print("평균 이하입니다.")
        return (height_m + height_d) / 2 - 6.5

height = round(finding_height(162.7, 178), 1)
print(height)
height = round(finding_height(151, 176), 1)
print(height)
height = round(finding_height(165, 175), 1)
print(height)

print("=======================================")
# Quiz 4-1 [학생 퀴즈] 소수 판별하기
# is_prime() 함수를 만든다
# 인수로 1개의 숫자를 받는다
# 인수로 넘어온 숫자가 소수이면 "소수" 아니면 "소수 아님"을 리턴
"""
result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님
"""
def is_prime(num):
    if num == 2:
        return "소수"
    for i in range(2, num):
        if num % i == 0:
            return "소수 아님"
        else:
            return  "소수"
result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님

print("=======================================")
'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 
이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!'
특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 

result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황') 
print(result) # 요모야..! 
result = get_compliment('좋은 마음가짐이다!') 
print(result) # 으무!
'''
def get_compliment(st):
    if '고구마' in st:
        return "왓쇼이!"
    elif '맛있는' in st:
        return "우마이!"
    elif '놀랄 만한'in st:
        return "요모야...!"
    elif '황당한' in st:
        return "요모야...!"
    elif '굉장한' in st:
        return "요모야...!"
    else:
        return "으무!"

result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result) # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result) # 으무!

'''
Quiz 5 - 1. 모듈이란?
-> 함수장이나 클래스 등의 파이썬 문장들을 담고 있는 파일을 모듈이라고 함

Quiz 5 - 2. 패키지란?
-> 모듈들을 모아둔 집합

Quiz 5 - 3. theater_module.py 모듈(파일)의 price 함수를 p학번이라는 이름으로 호출 하도록 import문을 작성하세요
-> import theater_module as p2312

Quiz 5 - 4. __all__의 역할은?
-> 임포트 되길 원하는 모듈을 정의하여 인식하게 만드는 것

Quiz 5 - 5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
-> if __name__ 

Quiz 5 - 6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage 클래스를 생성하고 
            detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
import travel.vietnam
< 가 > 
A = travel.vietnam.ThailandPackage()
A.detail()

from travel import vietnam
< 나 > 
A = vietnam.ThailandPackage()
A.detail()

from travel.vietnam import ThailandPackage
< 다 > 
A = ThailandPackage()
A.detail()
'''



