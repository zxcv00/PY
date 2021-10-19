class Entertainer: # 이름,
    def __init__(self, name):
        self.name = name
        pass

    def set_height(self, height):
        self.height = height

    def set_face(self, face):
        self.face = face

    def set_kind(self, kind):
        self.kind = kind

    def set_name(self, name):
        self.name = name

    # def info(self):
    #     print(f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}')

    def __str__(self):
        return f'이름: {self.name}\t키: {self.height}\t얼굴: {self.face}\t인성: {self.kind}'

아이유 = Entertainer('아이유')
# 아이유.set_name('이지은')
아이유.set_height('161')
아이유.set_face('형섭쌤이상형')
아이유.set_kind("That's very good.")
print(아이유)
# 아이유.info()

nana = Entertainer('나재민')
nana.set_height('176cm')
nana.set_face('공주임 잘생기고 예쁨 완전 토끼')
nana.set_kind('애기토끼천사')
print(nana)

class Singer(Entertainer):
    def __init__(self, name, song):
        super().__init__(name)
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t대표곡: {self.song}'

class Talent(Entertainer):
    def __init__(self, name, drama):
        super().__init__(name)
        self.drama = drama

        def __str__(self):
            return super().__str__() + f'\t드라마: {self.drama}'

심수련 = Talent('심수련', '펜트하우스')
심수련.set_height('168cm')
심수련.set_face('짱 예쁘시다')
심수련.set_kind('최고~')
print(심수련)

jeno = Singer('이제노', 'WE GO UP')
jeno.set_height('177cm')
jeno.set_face('얼사몸도 잘생김 최고~')
jeno.set_kind('순함 걍 강강지')
print(jeno)

nana = Singer('나재민', 'WE GO UP')
nana.set_height('177cm')
nana.set_face('공주임 잘생기고 예쁨 완전 토끼')
nana.set_kind('애기토끼천사')
print(nana)

nct_dream = []
nct_dream.append(jeno)
nct_dream.append(nana)
print(nct_dream)