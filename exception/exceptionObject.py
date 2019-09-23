'''
    예외의 최상위 객체 : Exception

    사용자 정의로 새 예외를 만들 때 Exception 을 사용해도 되고
    흔한 오류라 생각되면 ValueError 를 사용해도 됨

'''

class Unexpected_exception(Exception):
    pass
    print('new exception')