

#使fiddle可以抓包
# proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
# r = session.post(url, headers=header, json=feilds ,proxies=proxies, verify=False)

#start_time = int(round(time.time() * 1000))

# @classmethod
# def api_上传附件(cls, session: requests.Session, feilds: dict, header: dict):
#     api_name = 'api_上传附件'
#     url = Api_Addr_WeRun.werun_apis.get(api_name)
#     m = MultipartEncoder(fields=feilds, boundary='----WebKitFormBoundarynuAGsBlvBWSGBhkU')
#     header.update({'Content-Type': m.content_type})
#     r = session.post(url, data=m, headers=header)
#     Common_Base.logging_api_info(api_name, url, str(header), r.text, str(feilds))
#     return r.json()