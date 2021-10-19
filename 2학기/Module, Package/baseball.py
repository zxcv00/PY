from turtledemo.minimal_hanoi import play
from baseball_game_engine import make_quiz, check
from custome_error import InvalidCountError

answer = make_quiz()
count = 0

def save_history(player, count):
    with open('baseball_history.txt', 'a') as f:
        f.write(f'{player}\t{count}\n')

def load_history():
    count_list = []

    with open('baseball_history.txt', 'r') as f:
        while True:
            line = f.readline()

            if line == '':
                break
            # print(line.rstrip())
            line_data = line.rstrip().split('\t')
            count_list.append(line_data[1])

    # 중복 제거
    count_list = set(count_list)
    count_list = list(count_list)
    count_list.sort()
    return count_list[:3]

# 무한 반복
while True:
    # 숫자 세 자리 중복 없이 묻기
    player = input("숫자 세 자리 (t: TOP 3) => ")       # player: "123" "fun"

    if player == 't':
        try:
            history = load_history()
        except FileNotFoundError:
            print('history 파일이 없습니다.')
            continue
        print(history)
        continue

    # 숫자가 아닐 때 예외 처리
    try:
        player_int = int(player)                # valueError
    except ValueError:
        continue

    # 길이가 3이 아닐 때 에러 처리
    if len(player) != len(answer):
        # raise InvalidCountError("세 자리가 아닙니다.")
        print(f'입력한 숫자의 개수가 정답과 다릅니다. 정답: {len(answer)} 글자')

    # strike, ball 확인
    count += 1
    strike, ball = check(answer, player)

    # 출력
    print(f'{player}\tstrike: {strike}\tball: {ball}\t | {count} try')

    # strike == 3 => 종료
    if strike == 3:
        # 저장
        save_history(player, count)
        break

print("축하합니다. 🎉🎉")

