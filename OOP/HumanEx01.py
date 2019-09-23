print()
'''
# 클래스 생성

class 클래스명 :      # 클래스명은 첫글자 대문자(권장사항)
    변수             # 클래스 선언한 변수는 필드(field)라 부름
    
    함수             # 클래스 선언한 함수는 메소드(method)라고도 부름
    
        # 필드와 메소드를 통틀어 클래스의 속성(attribute)라 부름
'''

class Human :
    pass      # 클래스 생성시 아무런 속성이 없을 경우 pass를 반드시 적을 것!

person1 = Human()    # 객체(화)
person2 = Human()

# print(person1)
# print(person2)

print('-------------1--------------')
# 객체에 특성(특징, 성질)을 주입 - 값 대입
# 비어 있는 틀에 외부에서 채울 수도 있다
person1.language = 'KOREAN'
person2.language = 'ENGLISH'

print(person1.language)
print(person2.language)

print('-------------2--------------')
# 두 사람에게 이름을 부여해서 출력해보세요 (유관순, 안창호)
person1.name = '유관순'
person2.name = '안창호'

print(person1.name)
print(person2.name)

print('-------------3--------------')
# 행위(함수)를 부여할 수도 있음
def speak(person):
    print('{} 님이 {}로 연설합니다'.format(person.name, person.language))

'''
# Human.speak = speak
speak(person1)
speak(person2)

-> 현재 클래스 안에 함수를 적용한 상태 x -> 일반함수를 적용한 상태일 뿐
: 클래스의 메소드로 적용하려면 그 행위(함수)를 인스턴스화 해줘야 한다
'''

Human.speak = speak
person1.speak()
person2.speak()

'''
일반 함수인 speak()를 호출 시 person1과 person2를 인자로 사용
클래스에서 직접 speak를 호출하여 person1과 person2가 사용

말하는 행위가 중심일 때는 행위함수에 '누가' 말한 것인지를 전달.
클래스(객체)가 중심일 때는 말할 사람이 정해져 있으므로 굳이
인자로 사람을 전달할 필요가 없음


'''