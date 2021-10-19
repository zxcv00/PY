# 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?
import math
import random
import datetime

bill = 59827
bill = math.floor(bill / 100) * 100
print(bill)

print('-' * 30)

# 2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
score = 56

score = round(score, -1)
print(round(score / 10) * 10)

print(score)

print('-' * 30)

# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
lotto = random.sample(range(1, 46), 6)

print(lotto)

print('-' * 30)

# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
list_r = random.sample(range(1, 9 + 1), 3)

print("".join((str(n) for n in list_r)))
print("".join(map(str, list_r)))

print('-' * 30)

# 5. 내가 태어난 날로부터 며칠이 지났는지?
now = datetime.datetime.now()

bday = datetime.datetime(2004, 5, 14)

print(now - bday)

print('-' * 30)

# 6. 올해 크리스마스까지 며칠이 남았는지?
xmas = datetime.datetime(2021, 12, 25, 12, 0)

print(xmas - now)

print('-' * 30)

# 7. 내 생일이 며칠 남았는지?
mybd = datetime.datetime(2022, 5, 14, 12, 0)
print(mybd - now)

yj_bday = datetime.datetime(2021, 1, 4)
if yj_bday < now:
    yj_bday = yj_bday.replace(year=yj_bday.year + 1)

print(yj_bday - now)

print('-' * 30)

# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
last_num = input("마지막 번호: ")
list_class = list(range(1, int(last_num) + 1))
print(list_class)

while True:
    exclude_num = input("뺄 번호 (ENTER = 끝냄) ")

    if exclude_num == '':
        print("<종료>")
        break
    list_class.remove(int(exclude_num))

    random.shuffle(list_class)

print("자리\t\t학생 번호")
for index, n in enumerate(list_class):
    print(f'{index + 1}\t\t{n}')

