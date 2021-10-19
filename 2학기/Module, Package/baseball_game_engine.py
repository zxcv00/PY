# 숫자 야구 게임
# 퀴즈 (숫자 세 자리, 중복 ,X)
import random

def make_quiz():
    # 숫자 세 자리 중복 X
    list_r = random.sample(range(1, 10), 3)
    s_num = "".join(map(str, list_r))

    return s_num

def check(answer, player):
    strike = 0
    ball = 0

    for i, p in enumerate(player):
        for j, a in enumerate(answer):
            if p == a:
                if i == j:          # 번호가 있고 자리가 같으면 strike += 1
                    strike += 1
                else:               # 번호가 있고 자리가 다르면 ball += 1
                    ball += 1

    return strike, ball


if __name__ == '__main__':

    answer = make_quiz()
    print(answer)

    strike, ball = check("238", "241")
    print(strike, ball)

    strike, ball = check("381", "182")
    print(strike, ball)
