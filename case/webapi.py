import requests,json,pprint

class APIOm():


    def __init__(self):
        self.s = requests.Session()

    def _printResponse(self,response):
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        # for k,v in response.headers.items():
        #     print(f'{k}: {v}')

        print('')

        print(response.content.decode('utf8'))
        print('-------- HTTP response * end -------\n\n')



    #运营登录后台
    def om_login(self):

        host = "http://2.32.249.133:9001"
        path = "/login"
        url = host + path

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        data = {
            "password": "C4hOC9qa7rGw4mUMxJv4kw==",
            "userName": "whyman",
            "verifyCode": "1234"
        }
        proxies = {
            "http": "http://221.224.13.79:8006"
        }

        response = self.s.post(url,json=data,headers=headers,proxies=proxies)

        # self._printResponse(response)
        cookie = response.headers["Set-Cookie"]
        return cookie,response

    #运营列出申请虚拟户列表
    def getVirtualAccountList(self):
        print('列出商家')
        host = "http://2.32.249.133:9001"
        path = "/mallAccount/getVirtualAccountList"
        url = host+path
        params = {
            "shopName": None,
            "page": "1",
            "rows": "10",
        }
        self.om_login()

        proxies = {
            "http": "http://221.224.13.79:8006"
        }
        response = self.s.get(url,params=params, proxies=proxies)
        return response.json()


r = APIOm()
# 先调用登录
r.om_login()

r.getVirtualAccountList()
