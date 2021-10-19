# 파이썬 객체 그대로 저장
import pickle
from person import Person

번호1 = Person('공도윤', '곰 세 마리')
번호4 = Person('김설', 'stay (저스틴 비버)')

절친 = [번호1, 번호4]
if __name__ == '__main__':
    with open('object.bin', 'wb') as f:
        pickle.dump(번호1, f)

    with open('objects.bin', 'wb') as f:
        pickle.dump(절친, f)

    with open('object.bin', 'rb') as f:
        data = pickle.load(f)
    print(f'load한 데이터 => {data}')