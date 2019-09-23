# 상속(inheritance) - 코드 재사용하는 한가지 방법
# 부모 클래스    ----    자식클래스
# super class  ----    sub class

class Animal():
    def eat(self):
        print('삼시 세끼를 잘 먹자')

    def sleep(self):
        print('쿨쿨 자요')

class Human(Animal):
    def coding(self):
        print('ctrl+c ctrl+v')


class Dog(Animal):
    def protect(self):
        print('집을 잘 지키자')
person = Human() # 객체(인스턴스)화
person.eat()
person.sleep()
person.coding()

print('-----------------1-------------------')
# 강아지가 먹고, 자고, 집을 지키도록 해보세요

dog = Dog()
dog.eat()
dog.sleep()
dog.protect()