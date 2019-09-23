num = int(input("몇번 문제?"))
if num == 1 :
    print('1번')
    for i in range(2,8) :
        for a in range(1,i) :
            print(a, end='')
        print('')


elif num == 2 :
    print('2번')
    for i in range(1,6) :
        for a in range(0,i) :
            a = '*'
            print(a, end='')
        print('')




elif num == 3 :
    print('3번')
    for i in range(1,4) :
        for a in range(0,i) :
            a = '*'
            print(a, end='')
        print('')

elif num == 4 :
    for i in range(1,6) :
        for a in range(i,6) :
            a = '*'
            print(a, end='')
        print('')

elif num == 5 :
    for dan in range(2,10) :
        for i in range(1,10) :
            print(dan,' * ', i,' = ', (dan*i))
        print('')

elif num == 6 :
    value = input('숫자를 입력하세요 : ')
    dan = int(value)
    for i in range(1,10) :
        print(dan,' * ', i,' = ', (dan*i))
    print('')

elif num == 7 :
    value = input('숫자를 입력하세요 : ')
    a = int(value)
    sum = 0
    for b in range(0,a+1) :
        sum += b
    print(sum)

elif num == 8 :
    value = int(input('숫자를 입력하세요 : '))
    if value%3 == 0 :
        print(value,'은(는) 3의 배수입니다')
    elif value%3 != 0 :
        print(value,'은(는) 3의 배수가 아닙니다')

elif num == 9 :
    sum = 0
    for i in range(1, 11) :
        if i%2 != 0 and i%3 != 0 :
            print(i, end='\t')
            sum += i
    print('')
    print(sum)

elif num == 10 :
   for i in range(1, 7):
       for a in range(1, 7):
           if (i + a) == 4 :
               print(i, a)


elif num == 11 :
    for i in range(1,10):
        print(3,'*',i,'=',(3*i), end=' ')


elif num == 12 :
    for dan in range(2, 10):
        for i in range(1, 10):
            print(dan,'*',i,'=',(dan*i),end=' ')
        print('')