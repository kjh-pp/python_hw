import webbrowser # 사용을 안할때는 회색, 사용할 때는 주황색
# webbrowse : 시스템에서 사용하는 기본 웹브라우저를 자동으로 실행되게하는 모듈
# webbrowser.open('https://m.post.naver.com/viewer/postView.nhn?volumeNo=24266276&memberNo=30120665')
# webbrowser.open_new_tab('https://m.post.naver.com/viewer/postView.nhn?volumeNo=24266276&memberNo=30120665')

import urllib.request
# 웹 정보 읽어오기

url = 'https://m.post.naver.com/viewer/postView.nhn?volumeNo=24266276&memberNo=30120665'
def web_info(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    encode = data.decode("utf-8")
    return encode

context = web_info(url)
print(context)

