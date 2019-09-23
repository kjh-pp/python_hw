print()
'''
비어있는 클래스와 일반 함수를 따로 만들고 그 일반함수를 다시 비어있는 클래스에
대입하는 방식 --> 번거로움

클래스 안에 함수를 바로 생성
'''

class Human():
    pass
    # 인스턴스 생성
    def create_human(name, height):
        person = Human()
        person.name = name
        person.height = height
        return person

    # 먹기
    def eat(person):
        person.height += 0.3
        print('{} 가 건강하게 먹어서 키가 {} 가 되었습니다.'.format(person.name, person.height))

    # 걷기
    def walk(person):
        person.height += 0.2
        print('{} 가 열심히 운동해서 키가 {}이 되었습니다'.format(person.name, person.height))

    # 일반 함수를 클래스에 따로 대입할 필요가 이제 없어짐
    # 이 때 클래스 내부에 있는 함수를 메소드라고 부름

person = Human.create_human('유관순', 163.5)
person.eat()
person.walk()

print('------------------1--------------------')

person2 = Human.create_human('김마리아', 160.5)
person2.eat()
person2.walk()