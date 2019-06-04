import requests
import json

#接口 1 测试程序
r = requests.get('http://localhost:8080/IDEAmaven/springboot/getUserByGet?userName=%E5%90%B4%E8%80%81%E5%B8%88')
print(r.text)

assert r.text == "Hello 吴老师"

#接口 2 测试程序
data = {'userName':'吴老师'}
r = requests.post('http://localhost:8080/IDEAmaven/springboot/getUserByPost',data)
print(r.text)

assert r.text == "Hello 吴老师"

#接口 3 测试程序
data = json.dumps({'username':'吴老师'})
r = requests.post('http://localhost:8080/IDEAmaven/springboot/getUserByJson',data)
print(r.text)

assert r.text == '{"userdata":"吴老师 is a man!"}'










