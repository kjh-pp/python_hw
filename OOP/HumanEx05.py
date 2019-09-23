print()
'''
특별한 기능을 하는 메소드 : 메소드 이름 양쪽에 __(underbar 두개)
'''

class Human():
    # 초기화 메소드
    def __init__(self):
        pass
        print('__init__ 실행됨')

    def __init__(self, name, height):
        pass
        print('__init__(self, name, height) 실행됨')
        print('이름 : {}, 키 : {} '.format(name, height))

    # init => 인스턴스 생성 및 초기화
    def __init__(self,name,height):
        self.name = name
        self.height = height

    #__str__ : 문자열화 메소드 - 인스턴스를 문자열로 변환
    def __str__(self):
        pass
        return '{} (키 {} cm)'.format(self.name, self.height)

    # __init__ : 인스턴스화 되는 순간에 자동으로 생성되어 호출되는 함수
    # init -> 매개변수가 있는 메소드로 확장
# person = Human('유관순', 163.4)

person = Human('유관순', 163.4)
print(person.name, person.height)

print('-------------------1---------------------')
print(person)