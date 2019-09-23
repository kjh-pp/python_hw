print()
'''
메소드 특별한 규칙 : 메소드 호출 시 첫번째 인자를 생략하면 자기 자신으로 채워줌
 - keyword : self -> 자기 자신을 호출하는 매개변수
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
    def eat(self):
        self.height += 0.3
        print('{} 가 건강하게 먹어서 키가 {} 가 되었습니다.'.format(self.name, self.height))

    # 걷기
    def walk(self):
        self.height += 0.1
        print('{} 가 열심히 운동해서 키가 {}이 되었습니다'.format(self.name, self.height))

    def speak(self, message):
        print(message)

    def dontEat(self):
        self.height -= 0.2
        print('{} 가 단식투쟁으로 {} 이 되었습니다'.format(self.name, self.height))
person = Human.create_human('유관순', 163.5)
person.eat()
person.walk()

'''
인스턴스화한 객체에서 함수 호출시 매개변수 첫번째 인자가 self이면 생략가능
파이썬이 첫번째 매개변수를 자동 호출
'''
person.speak('안녕하세요')

print('----------------------1------------------------')
# 출력 : 윤동주 열사가 단식투쟁으로 178.5가 되었음
person2 = Human.create_human('윤동주', 178.7)
person2.dontEat()
