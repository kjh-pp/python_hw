import datetime
import random
import math
'''

date = datetime.date(2019, 9, 2)
time = datetime.time(5, 43, 11)

dt = datetime.datetime.combine(date, time)
print(dt)

now = datetime.datetime.now()
nowTuple = now.timetuple()
print(nowTuple)

print(nowTuple.tm_year)
print(nowTuple.tm_zone)

now = datetime.datetime.now()
print(now)

tomorrow = now + datetime.timedelta(days=1)
print(tomorrow)

the_Day_After_Tomorrow = now + datetime.timedelta(days=2)
print(the_Day_After_Tomorrow)

now = datetime.datetime.now()
print(now)

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)

nowTime = now.strftime('%H:%M:%S')
print(nowTime)

nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDateTime)

timeStr = '2019-09-02 17:55:54'
thisTime = datetime.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
print(type(thisTime))
print(thisTime)

myDateTime = datetime.datetime.strptime('2019-09-02 17:55:54', '%Y-%m-%d %H:%M:%S')
yourDateTime = myDateTime.replace(day=23)
print(myDateTime)
print(yourDateTime)

list = random.sample(range(1, 46),6)
list.sort()
print(list)
'''


lottoNum = []
for i in range(1, 46):
    lottoNum.extend([i])
random.shuffle(lottoNum)

lotto = lottoNum[:6]
lotto.sort()
print(lotto)



