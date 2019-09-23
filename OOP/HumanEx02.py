class Human():
    pass

person1 = Human()
person1.name = '유관순'
person1.height = 155

print(person1)
print(person1.name, person1.height)
'''
객체를 생성할 때 마다 데이터를 초기화하는 것은 불편함. 권장(x)
함수로 만들어 놓고 인스턴스를 생성
'''
def create_human(name, height):
    person = Human()
    person.name = name
    person.height = height
    return person

Human.create = create_human
person = Human.create('윤봉길', 180.2)

print(person)
print(person.name, person.height)

print('--------------1---------------')
# 이 윤봉길 의사가 먹고, 운동하도록 하고 싶습니다.
'''
출력 
 - 윤봉길 의사가 건강하게 먹어서 키가 180.5가 되었습니다
'''

def eat(person):
    person.height += 0.3
    print('{} 가 건강하게 먹어서 키가 {} 가 되었습니다.'.format(person.name, person.height))
# Human 클래스의 내부 함수로 지정
Human.eat = eat
# 실제화 -> 모델링
person.eat()

print('--------------2---------------')
'''
출력
 - 윤봉길 의사가 열심히 운동해서 키가 180.3이 되었습니다
'''
def walk(person):
    person.height -= 0.2
    print('{} 가 열심히 운동해서 키가 {}이 되었습니다'.format(person.name, person.height))
Human.walk = walk
person.walk()
