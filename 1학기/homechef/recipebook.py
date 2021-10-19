from recipe import Recipe

class Recipebook:
    def __init__(self):
        self.recipe_list = []
        self.food_court()

    def add_recipe(self):
        # 추가할 레시피 이름 입력 받기
        recipe_name = input('>> 레시피의 이름을 입력하세요: ')

        # 중복 레시피 체크
        for recipe in self.recipe_list:
            # 중복되는 레시피가 있으면
            if recipe_name == recipe_name:
                # 존재하는 레시피가 있다고 알려주기
                print('이미 존재하는 레시피입니다.')
                return
        # 중복되는 레시피가 없다면
        # 레시피 생성
        new_recipe = Recipe(recipe_name)
        new_recipe.set_recipe()
        # 레시피 리스트에 추가
        self.recipe_list.append(new_recipe)

    def show_all_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index + 1}')
            print(recipe)

    def search_recipe(self):
        # 찾을 레시피 이름 입력 받기
        recipe_name = input('>> 원하는 레시피를 검색하세요: ')
        searched_recipe = []

        # (반복문 시작) 레시피 리스트를 돌면서 레시피가 있는지 확인
        for recipe in self.recipe_list:
            # 찾는 레시피 이름이 존재한다면
            if recipe_name in recipe.name:  # if '부대' in '부대찌개' --> 찾을 수 있음 / in이 아닌 ==을 사용한다면 '부대'를 검색했을 때 '부대찌개'가 검색되진 않음
                # 그 레시피 보여주기
                print(recipe)
                searched_recipe.append(recipe)
        # (반복문 종료)
        # 찾는 레시피의 이름이 존재하지 않으면
        if len(searched_recipe) == 0:   # 못 찾음
            # 추가할지 묻기
            choice = input('>> 원하는 레시피가 존재하지 않습니다. 추가하시겠습니까? (1. 예 / 2. 아니요')
            # 추가한다고 선택
            if choice == 1:
                # 레시피 추가
                self.add_recipe()
            # 추가하지 않으면
            else:
                return
                # 종료

    def serch_whatin(self):
        whatin_set = set()  # (재료 세트) 빈 세트 생성
        for recipe in self.recipe_list:
            for whatin in recipe.whatin:
                whatin_set.add(whatin)
        # 모든 재료 다 보여주기
        print('다음 재료를 사용해보세요.')
        for index, whatin in enumerate(whatin_set):
             print(f'{index + 1}. {whatin}')
        # 재료 중에 사용할 재료 고르기
        num = int(input('>> 사용할 재료 번호를 입력하세요: '))
        use_whatin = list(whatin_set)[num - 1]
        # 고른 재료가 포함되는 레시피 다 보여주기
        for recipe in self.recipe_list:
            if use_whatin in recipe.whatin:
                print(recipe)

    def food_court(self):
        지원 = Recipe('케이크')
        지원.quantity = 1
        지원.link = 'youtube.com'
        지원.whatin = {'밀가루': '500', '계란': '100', '생크림': '200', '딸기': '100'}
        지원.info = '맛있게 드세요'
        지원.time = 60
        self.recipe_list.append(지원)

        서연 = Recipe('삼겹살김치볶음밥')
        서연.quantity = 4
        서연.link = 'youtube.com'
        서연.whatin = {'삼겹살': '100', '김치': '150', '밥': '100'}
        self.recipe_list.append(서연)

    def __str__(self):
        pass