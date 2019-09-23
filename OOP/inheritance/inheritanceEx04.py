# 부모를 호출 가능 - super()

class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('삼시세끼를 잘 먹자')

    def sleep(self):
        print('쿨쿨 자여')

    # override method
    def move(self):
        print('걷는 것은 {} 이다'.format(self.name))


'''
[출력]
두 발로 서서 전방 15도를 주시하며 걷는 것은 사람이다
네 발로 서서 사방을 돌아보며 걷는 것은 강아지이다

 - 변수 : name, angle
'''

class Human(Animal):
    def __init__(self, name, angle):
        super().__init__(name)
        self.angle = angle

    def coding(self):
        print('ctrl+c ctrl+v')

    def walk(self):
        print('두발로 서서 전방 {}도를 주시하며'.format(self.angle))

    def move(self):
        self.walk()
        super().move()

person = Human('사람', 15)
person.move()

class Dog(Animal):
    def __init__(self, name, angle):
        Animal.__init__(self, name)
        self.angle = angle

    def walk(self):
        print('네 발로 서서 {}을 돌아보며'.format(self.angle))

    def move(self):
        self.walk()
        super().move()

dog = Dog('강아지', '사방')
dog.move()