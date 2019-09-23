# 상속 - method override

class Animal():
    def eat(self):
        print('삼시 세끼를 잘 먹자')

    def sleep(self):
        print('쿨쿨 자요')

    # override를 위한 method : 사람과 개는 동일하게 걷지 않으므로 각각 표현 방식이 달라야 함
    def move(self):
        print('걷는다')

class Human(Animal):
    def coding(self):
        print('ctrl+c ctrl+v')

    def walk(self):
        print('두발로 걸어요')

    def move(self):
        self.walk()

class Dog(Animal):
    def protect(self):
        print('집을 지켜요')

    def walking(self):
        print('네 발로 걸어요')

    def move(self):
        self.walking()

person = Human()
person.eat()
person.sleep()
person.move()
person.coding()

print('---------------1---------------')

dog = Dog()
dog.eat()
dog.sleep()
dog.move()
dog.protect()