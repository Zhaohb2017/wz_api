# 设置请求头
headers = {
    'form':{'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Language':'zh-CN,zh;q=0.9'},
    'json':{'Content-Type': 'application/json; charset=UTF-8'},
    'null':{'Content-Type': ''},
    'json_open_account':{'Content-Type': 'application/json','Accept-Language':'zh-CN,zh;q=0.9'},
    'json_and_user_agent':{'Content-Type': 'application/json','User-Agent':'uuid/0000000061cb31f2ffffffffb4353691','Accept-Language':'zh-CN,zh;q=0.9'},
    'form_and_user_agent':{'Content-Type': 'application/x-www-form-urlencoded','User-Agent':'uuid/0000000061cb31f2ffffffffb4353691','Accept-Language':'zh-CN,zh;q=0.9'},
    'json_nebula':{'Content-Type': 'application/json','Connection':'Keep-Alive','User-Agent': 'Apache-HttpClient/4.5.12 (Java/1.8.0_230)','Accept-Language':'zh-CN,zh;q=0.9'},
}

# pc浏览器模拟app端操作user-agent
app_user_agent = 'user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148    zyapp/2.0.7.14 (Apple iPhone11,2; iOS 12.3.1) uuid/91bd7aa71caf5e07867b75760937a2ed red_green_setting/red lauguage/zh-CN"'