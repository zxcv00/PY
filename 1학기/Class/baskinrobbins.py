class Icecream:
    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor

    def set_description(self, description):
        self.description = description

    def __str__(self):
        return f'이름: {self.name}\t맛: {self.flavor}'

# 엄마는외계인 = Icecream('엄마는 외계인', '밀크 초콜릿, 다크 초콜릿, 화이트 무스 + 초코볼')
# 엄마는외계인.set_description('밀크 초콜릿, 다크 초콜릿, 화이트 무스 세 가지 아이스크림에 달콤 바삭한 초코볼이 더해진 아이스크림')
# print(엄마는외계인)
# print(엄마는외계인.description)

# 아몬드봉봉 = Icecream('아몬드 봉봉', '초콜릿, 아몬드')
# print(아몬드봉봉)

# 오레오쿠앤크 = Icecream('오레오 쿠키 앤 크림', '바닐라향, 오레오 쿠키')
# print(오레오쿠앤크)

class Cup:
    _CUP_CATEGORIES = ['싱글컵', '더블컵', '파인트']
    _PRICES = [4000, 6200, 8200]
    def __init__(self, name, count_flavor):
        self.name = name
        self.count_flavor = count_flavor
        self.price = Cup._PRICES[self.count_flavor]
        self.menu = []
        self.add_menu()
        self.order_menu = []

    def add_menu(self):
        엄마는외계인 = Icecream('엄마는 외계인', '밀크 초콜릿, 다크 초콜릿, 화이트 무스 + 초코볼')
        엄마는외계인.set_description('밀크 초콜릿, 다크 초콜릿, 화이트 무스 세 가지 아이스크림에 달콤 바삭한 초코볼이 더해진 아이스크림')

        아몬드봉봉 = Icecream('아몬드 봉봉', '초콜릿, 아몬드')

        오레오쿠앤크 = Icecream('오레오 쿠키 앤 크림', '바닐라향, 오레오 쿠키')

        self.menu.append(엄마는외계인)
        self.menu.append(아몬드봉봉)
        self.menu.append(오레오쿠앤크)

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(index + 1, icecream)

    def order(self):
        for n in range(self.count_flavor):
            self.show_menu()
            flavor = input('맛을 고르세요: ')
            flavor = int(flavor)
            icecream = self.menu[flavor - 1]
            self.order_menu.append(icecream)
        print('주문한 아이스크립입니다.')
        for icecream in self.order_menu:
            print(icecream)

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t종류: {Cup._CUP_CATEGORIES[self.count_flavor - 1]}'

# A = Cup('더블컵', 2)
# print(A)
# A.order()

B = Cup('싱글컵', 1)
print(B)
B.order()