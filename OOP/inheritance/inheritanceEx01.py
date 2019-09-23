# 사람 클래스
class Human:
    def eat(self):
        print('삼시세끼를 잘 먹자')
    
    def sleep(self):
        print('쿨쿨 자요')
        
    def walk(self):
        print('두 발로 걸어요')
        
    def coding(self):
        print('ctrl+c ctrl+v')
        
        
# 개 클래스
class Dog:
    def eat(self):
        print('사료를 맛있게 먹어요')
    
    def sleep(self):
        print('쿨쿨 잘 자요')
    
    def walking(self):
        print('네 발로 걸어요')
    
    def detect(self):
        print('집을 잘 지키자')
    
'''
각 객체가 많은 부분을 공유하고 있음
각 객체가 동물이기 때문...
이 공유되는 부분을 따로 만들어 두고(추상화)
각 객체가 이 공유되는 부분을 받아다 쓰는게 효율적 -> 상속

'''