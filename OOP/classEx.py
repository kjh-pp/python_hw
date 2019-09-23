# class

class Test :   # 클래스 첫글자 대문자
    str = 'This is a Class'     # str : 클래스의 요소(field, member, attribute) // 특성화 성질

test1 = Test()   # 객체화 - 인스턴스화
print(test1.str)

class Person :
    def say(self):       #def say : 클래스 요소 (method, attribute) // 행위
        print('hi')

p1 = Person()
p1.say()

class Person2 :
    pass                # 요소를 지정하고 싶지 않으면 pass 반드시 필요

p2 = Person2()
print(p2)


# 파이썬 클래스에는 여러가지 특별한 메소드가 존재
# __init__ method : 클래스가 인스턴스화(객체화) 될 때 호출
#                 : 객체가 생성될 때 여러가지 초기화 작업을 하고자 할 때 유용
class Person3 :
    def __init__(self, name):
        self.name = name

    def info(self):
        print('내 이름은', self.name)

p3 = Person3('홍길동')
p3.info()
print('-------------------1---------------------')
'''
필드는 일반적인 변수와 같다.
필드는 해당 클래스 또는 객체 내부에서만 의미가 있음(벗어나면 못씀)
이 해당 클래스 내부와 객체 내부를 네임스페이스라고 함

필드는 클래스 변수와 객체 변수가 있음

차이? 공유 여부

네임스페이스 내부에서 공유 - 클래스 변수
각각 객체에서만 사용 - 객체 변수

'''

class Character :
    # 클래스 변수(네임스페이스 전역에 영향을 줌)
    cnt = 0

    # Charater 클래스 초기화
    def __init__(self, name):
        self.name = name  # name : 객체 변수
        print('{} 이/가 생성 중...'.format(self.name))

        # 클래스 변수 접근 : 클래스명.클래스변수명
        Character.cnt += 1

    # 캐릭터 사망 처리
    def die(self):
        print('{} 이/가 사망했습니다.'.format(self.name))

        Character.cnt -= 1
        if Character.cnt == 0 :
            print('{} 이/가 마지막 생존자 였음.'.format(self.name))
        else:
            print('아직 {:d} 명의 생존자가 있다'.format(Character.cnt))


    def info(self):
        print('생성 완료...반갑습니다. 내이름은 {} 입니다'.format(self.name))

    # 현재 생성된 캐릭터 수를 체크
    @classmethod    # 정적 영역으로 올려둔다 / 메소드를 객체화하기전에 미리 올려둔다
    def check(self):
        print('현재 {} 명이 있습니다'.format(Character.cnt))

npc01 = Character('홍길동')
npc01.info()
Character.check()

npc02 = Character('유관순')
npc02.info()
Character.check()

npc03 = Character('신사임당')
npc03.info()
Character.check()

Character.die(npc01)
Character.check()

