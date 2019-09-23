print()

try :
    list = []
    print(list[0])
except :
    print('오류가 발생함')

print('============1=============')

try :
    text = 'text'
    number = int(text)
except :
    print('오류 발생')

print('============2=============')

try :
    list = []
    print(list[0])

    text = 'text'
    number = int(text)
    print(number)

except Exception as ex:
    print('오류 발생', ex)

