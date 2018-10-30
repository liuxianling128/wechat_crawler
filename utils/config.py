# -*- coding: utf-8 -*-

# 缓存配置
cache_dir = 'cache'
cache_session_name = 'requests_wechatsogou_session'

# mysql数据库配置
#host = '10.39.0.242'
#user = 'mi'   # 数据库用户名
#passwd = 'mi'   # 数据库密码

# mysql数据库配置
host = 'localhost'
user = 'root'   # 数据库用户名
passwd = 'root'   # 数据库密码
db = 'mi-crawler'  # 默认数据库
charset = 'utf8mb4'
prefix = ''  # 默认数据表前缀,可以不用写
# 打码平台配置ruokuai  http://www.ruokuai.com/
# 注册并充值后，就可以直接使用，识别一个验证码大约0.008元
# 搜狗微信有点变态，有时明明验证码是正确的，他非说是错误的，这是没有办法的事情,好在这个概率非常低
dama_name = '#####'    #用户名
dama_pswd = '#####'  #密码

#platjs地址
phantom_js = 'E:\soft\python\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe'
req_crawler_url = 'http://localhost:8082/wechat/anaz'
binary_location = 'D:\Program Files\Application\chrome.exe'



