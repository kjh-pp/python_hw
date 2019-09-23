print()

# 절차(구조)적 프로그래밍
showInfo = ''

def person(name, age):
    global showInfo
    showInfo += '이름 : ' + name + ', 나이 : ' + age +'\n'
    return showInfo

person('홍길동','20')
person('유관순','17')

print(showInfo)

print('===================1=====================')
# 객체 지향
class Person: # 틀
    def __init__(self):
        self.info = ''

    def showInfo(self, name, age):
        self.info += '이름 : ' + name + ', 나이 : ' + age + '\n'
        print(self.info)

man = Person() # man 이 객체
man.showInfo('홍길동', '20')

woman = Person()
woman.showInfo('유관순', '17')

print('===================2=====================')
# 객체 정보 찾기 - type()
print(type(5))

# 자료형 정보 찾기 - isinstance() - t/f
# python 에서는 class 는 객체가 아니고 어떤 객체를 이루기 전인 '틀' 이다
# 인스턴스화를 한 후 객체
print(isinstance(5, float))

print('===================3=====================')
num1 = []
print(type(num1))
num2 = list(range(10)) # 0 이상 10 미만의 정수로 된 배열

text = list('hello python')

print(type(num2))
print(type(text))

print('===================4=====================')

print(isinstance(num2, list))
print(isinstance(text, list))

print('===================5=====================')
print(num1 == list) # 내용 비교
print(isinstance(num1, list)) # num1 자료형 list 냐?