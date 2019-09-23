from urllib.request import urlopen, Request
import urllib

url = 'https://www.example.com'

data = {"key1":"value1", "key2":"value2"}

data = urllib.parse.urlencode(data)
data = data.encode('utf-8')

req_get = Request(url+'?key1=value1&key2=value2', None)

page = urlopen(req_get)

print(page.url)
print(page.code)