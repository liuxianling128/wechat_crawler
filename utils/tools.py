# -*- coding: utf-8 -*-

import json
import requests
import urllib.request
import time
import os



def mkdir(path):
    folder = os.path.exists(path)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)
    else:
        print("已存在文件夹")


def getNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
def getNowTime_nosign():
    return time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
def requests_post(url,data):
    req_data = json.dumps(data)
    result = requests.post(url,req_data)
    print (result)
    return result

def urllib_post(url,data):
    print(url)
    edata = json.dumps(data,ensure_ascii=False)
    print(edata)
    req_data=bytes(edata,'utf8')
    headers={'Content-Type':'application/json'}
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req,req_data)
    message = response.read()
    return message



def prdict(content):
    msg = json.dumps(content, indent=1, ensure_ascii=False)
    print(msg)

def list_or_empty(content, contype=None):
    if isinstance(content, list):
        if content:
            return contype(content[0]) if contype else content[0]
        else:
            if contype:
                if contype == int:
                    return 0
                elif contype == str:
                    return ''
                elif contype == list:
                    return []
                else:
                    raise Exception('only cna deal int str list')
            else:
                return ''
    else:
        raise Exception('need list')