import requests as rq

url = 'https://www.naver.com'
url_x = 'https://www.naver.com/a'

# rq.get(url)         # get 방식 호출
# rq.post(url)        # post 방식 호출

res = rq.get(url)

print(res)

res = rq.get(url_x)

print(res.status_code)

print('-------------------------1----------------------------')
# 응답 코드에 따른 처리
def url_check(address):
    result = rq.get(address)

    # print(result)

    code = result.status_code
    
    if code == 200:
        print('요청 성공')
    elif code == 404:
        print('주소 오류')
    else : 
        print('알 수 없는 에러')
        
url_check(url)
url_check(url_x)