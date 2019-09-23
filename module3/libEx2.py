# time 모듈

import time

# 1970년 1월 1일 0시 0분 0초 기준( UTC [Universal Time Coordinated : 세계 협정 표준시] )
# 현재까지 시간을 초단위로 return => 실수 형태로 반환
print(time.time())

t = time.time()
result = time.localtime(t)

print(result)
'''
+ struct_time 시퀀스 객체 속성
 - tm_year : 년도
 - tm_mon : 월(1~12)
 - tm_mday : 일
 - tm_hour : 시 (0~23)
 - tm_min : 분
 - tm_sec : 초
 - tm_wday : 요일을 숫자로 표현 (월요일 : 0 ~ 일요일 : 6)
 - tm_yday : 1월 1일부터 누적된 날짜를 나타냄(1~366)
 - tm_isdst : 서머타임제(일광절약 시간제 0, 1, -1)
'''

print(time.gmtime(t))    # UTC기준 현재 시각

print(time.asctime())    # 알아보기 쉬운 날짜와 시간을 반환

print(time.ctime())      # asctime 개량형

print(time.strftime('%Y %m %d %X'))
'''
+ 형식지정자(포맷코드) 
 - %y : 년도 축약(2019->19), %Y : 네자리수 년도
 - %a : 요일 축약(Sun, Mon, ...), %A : 요일 (Sunday, ..)
 - %b : 영문 월 축약(Jan, ..), %B : 영문 월(January, ...)
 - %c : 날짜와 시간 출력 (19/09/06 10:15:20)
 - %d : 날짜 [01~31]
 - %H : 시간을 24시간 [0~23]
 - %I : 시간을 12시간 [01~12]
 - %j : 누적날짜를 표현 [01 ~ 366]
 - %m : 숫자 월 (1 ~ 12)
 - %M : 분 (01~59)
 - %p : 오전 오후 (AM, PM)
 - %S : 초 (00 ~ 59)
 - %U : 누적 주 (시작은 일요일부터, 00 ~ 53)
 - %w : 요일 (0 ~ 6)
 - %W : 누적 주 (시작을 월요일부터, 00 ~ 53)
 - %x : 날짜 출력 (19/09/06)
 - %X : 시각 출력 (10:19:30)
 - %Z : 시간대 출력 (local)
 
 


'''
# struct_time => strftime
print(time.strftime('%Y %m %d %X %x %j', time.localtime(time.time())))

# sleep
# for i in range(10):
#    print(i)
#    time.sleep(1)  # time.sleep(sec) : 반복문 안에서 많이 사용. 일정한 시간 간격을 주기 위해서 많이 사용

print('-----------------------1---------------------------')
import calendar
# print(calendar.calendar(2019))   # 해당년도의 전체 달력 출력
# calendar.prcal(2019)             # 해당년도의 전체 달력 출력

# calendar.prmonth(2019, 9)          # 해당년도의 해당 월만 출력

# 입력받은 날짜의 요일을 숫자로 return : 월 ~ 일 (0 ~ 6)
# print(calendar.weekday(2019, 9, 6))

# 입력받은 달의 1일이 무슨 요일인지를 숫자로 return
#  입력받은 달의 마지막 일자를 숫자로 return => 튜플로 return
print(calendar.monthrange(2019, 9))       # (6, 30) 일요일, 30일

print('-----------------------2---------------------------')
import datetime
# datetime 모듈 안에는 같은 이름의 클래스가 존재함
# 그러므로 함수를 호출하려면 모듈.클래스.함수 이런 형태로 호출

# now() : 현재 시간 (년-월-일 시:분:초.마이크로초[100만분의 일])
print(datetime.datetime.now())

print(type(datetime.datetime.now()))

# 시각정보를 변경 : replace()
now_time = datetime.datetime.now()

print(now_time)

print(now_time.replace(year=2018, month=1, day=1))
# replace()는 현재 시각을 바로 바꾸는게 아니라 새로 인스턴스를 만들어서 바꾸므로
#  실제 원 시각을 바꾸려면 다시 대입하는 형태로 한다.
print('-----------------------3---------------------------')

print(now_time)

now_time = now_time.replace(year=2018, month=1, day=1)

print(now_time)

print('-------------------------4----------------------------')

now_time = datetime.datetime(2020, 1, 1)
print(now_time)

print('-------------------------5----------------------------')
# 날짜 계산 : 빼기 연산 지원
result = now_time - datetime.datetime.now()
print(result)

print(type(result))
# timedelta : 시간을 잴 때 사용하는 클래스
#           : 일과 초를 각각 days, seconds 를 저장

print(result.days, result.seconds)

print('-------------------------6----------------------------')
# timedelta는 시와 분을 알려주지 않으므로 seconds를 응용해서 계산하여야 함
# 2019년 9월 1일 부터 ~일 ~시간이 지났습니다. 출력
time2 = datetime.datetime(2019, 9, 1)
result = datetime.datetime.now() - time2
print(result)
print(result.days, result.seconds)

print('2019년 9월 1일 부터 {} 일 {} 시간이 지났습니다'.format(result.days, result.seconds//3600))


print('-------------------------7----------------------------')
# 오늘부터 추석까지는 {}일 남았습니다 - 출력해보세요
# 함수로 만들어서 출력해보세요
def tgiving(x):
    d_day = x - datetime.datetime.now()
    print('오늘부터 추석까지는 {}일 남았습니다'.format(d_day.days))

time3 = datetime.datetime(2019, 9, 13)
tgiving(time3)


def tgiving1():
    d_day = datetime.datetime(2019, 9, 13)
    res = (d_day - datetime.datetime.now()).days
    return res
print('오늘부터 추석까지는 {}일 남았다'.format(tgiving1()))

print('--------------------------8----------------------------')
# 오늘 기준으로 30일 후 구하기
# - timedelta는 시간의 양만 구해주므로 최종 구하고 싶은 날짜를 얻으려면
#   기준일이 필요
print(datetime.timedelta(days=30))

thirty = datetime.timedelta(days=30)

print(datetime.datetime.now()+thirty)
# print(datetime.datetime.now()+30)


print('--------------------------9----------------------------')
# 오늘 기준으로 30일 전 구해보세요
print(datetime.datetime.now()-thirty)

bf_thirty = datetime.timedelta(days=-30)
print(datetime.datetime.now()+bf_thirty)

print('--------------------------10----------------------------')
# datatime, timedelta 이용해서 특정 시간대 지정
end_time = \
    datetime.datetime.now().replace(hour=18, minute=20, second=0)\
    +datetime.timedelta(days=48)

print('최종 종강 시간은 {} 입니다'.format(end_time))

print('--------------------------11----------------------------')
print(datetime.datetime.today())
