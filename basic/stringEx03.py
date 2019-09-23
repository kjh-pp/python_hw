str = '믿음은 선의의 거짓이 아닌 사실에 근거해야 한다. ' \
      '사실에 근거하지 않는 믿음은 저주받아 마땅한 헛된 희망이다.'
print(str)

print(str[2])
'''
문자열에 번호가 부여되어있음 : 문자열 인덱싱(색인 연산)
인덱스 번호는 0번부터 시작함에 유의!
'''
print(str.index('선'))
print(str[4])

print(str.index('망'))
print(str[57])

# 문자를 뒤에서부터 읽어올 수 있음 0이 아닌 -1 부터 시작
print(str[-4])

print('---------------------------------')

str = '나는 단 한번도 이성적인 사고를 통해 발견한 적이 없다.'

# '이성적인' 글자 추출
print(str.index('이'), str.index('인'))
print(str[9]+str[10]+str[11]+str[12])
print(str[9:13]) # 문자열 슬라이싱 ([시작인덱스 : 끝자리수])
                 #                  이상    :  미만
# '사고를' 추출
print(str.index('사'),str.index('를'))
print(str[14:18]) # 공백문자도 출력됨에 유의!
                  # '사고를'와 '사고를 '는 다른 문자!

print(str[9:]) # 끝자리수를 생략하면 그 문자열의 끝까지 리턴
print(str[:8]) # 시작 인덱스를 생략하면 문자열의 처음부터 끝자리수까지 리턴
print(str[:]) # 시작 인덱스와 끝자리수 모두 생략하면 그 문자열 전부 출력

print(str[9:-4]) # 인덱싱과 같이 사용하므로 - 기호도 사용 가능

print('---------------------------------------')
regdate = '20190829THU'
year = regdate[:4]
month = regdate[4:6]
date = regdate[6:-3]
day = regdate[-3:]
print(year, month, date, day)

# year, month, date, day,로 구분하여 변수에 담아서 출력해보세요


