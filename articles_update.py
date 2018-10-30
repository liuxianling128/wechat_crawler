# -*- coding: utf-8 -*-
#查找公众号最新文章
from utils import config
import datetime
import logging.config
import random

from wechatsogou import *
from utils.tools import *
# 日志
from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'resources/articles_update.conf')
logging.config.fileConfig(log_file_path)
#logging.config.fileConfig('resources/articles_update.conf')
logger = logging.getLogger()

# 搜索API实例
wechats = WechatSogouApi() #不使用外部Cookie



#数据库实例
mysql = mysql('wechat_info_list')
def articles_update_function():

    #循环获取数据库中所有公众号
    mysql.order_sql = " order by _id desc"
    mp_list = mysql.find(0)
    succ_count = 0

    now_time = datetime.datetime.today()
    now_time = datetime.datetime(now_time.year, now_time.month, now_time.day, 0, 0, 0)


    for item in mp_list:
        try:
            time.sleep(random.randrange(1,3))
            #查看一下该号今天是否已经发送文章
            last_qunfa_id = item['last_qunfa_id']
            last_qunfa_time = item['last_qufa_time']

            cur_qunfa_id = last_qunfa_id
            wz_url = ""
            if  'wz_url' in item :
                wz_url = item['wz_url']
            else :
                wechat_info = wechats.get_gzh_info(item['wx_hao'])
                if not 'url' in wechat_info:
                    continue
                wz_url = wechat_info['url'];

            print(item['name'])

            #获取最近文章信息
            wz_list = wechats.get_gzh_message(url=wz_url)
            if u'链接已过期' in wz_list:
                wechat_info = wechats.get_gzh_info(item['wx_hao'])
                if not 'url' in wechat_info:
                    continue
                print('guo qi sz chong xin huo qu success')
                wz_url = wechat_info['url'];
                wz_list = wechats.get_gzh_message(url=wz_url)
                mysql.where_sql = " _id=%s" %(item['_id'])
                mysql.table('wechat_info_list').where({'_id':item['_id']}).save({'wz_url':wechat_info['url'],'logo_url':wechat_info['img'],'qr_url':wechat_info['qrcode']})
            #type==49表示是图文消息
            qunfa_time = ''
            for wz_item in wz_list :
                temp_qunfa_id = int(wz_item['qunfa_id'])
                if(last_qunfa_id >= temp_qunfa_id):
                    print(u"没有更新文章")
                    print(u"")
                    break
                if(cur_qunfa_id < temp_qunfa_id):
                    cur_qunfa_id = temp_qunfa_id
                    qunfa_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(wz_item['datetime']))
                succ_count += 1
                if wz_item['type'] == '49':
                    #把文章写入数据库
                    #更新文章条数
                    print(succ_count)
                    print(wz_item['content_url'])

                    if not wz_item['content_url'] :
                        continue

                    sourceurl = wz_item['source_url']
                    if len(sourceurl) >= 300 :
                        sourceurl = ''



                    #请求入索引接口
                    data = {'title':wz_item['title'],
                            'source_url':sourceurl,
                            'content_url':wz_item['content_url'],
                            'cover_url':wz_item['cover'],
                            'description':wz_item['digest'],
                            'date_time': time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(wz_item['datetime'])),
                            'mp_id':item['_id'],
                            'author':wz_item['author'],
                            'msg_index':wz_item['main'],
                            'copyright_stat':wz_item['copyright_stat'],
                            'qunfa_id':wz_item['qunfa_id'],
                            'type':wz_item['type'],
                            #'content':content_src,
                            'like_count':0,
                            'read_count':0,
                            'comment_count':0}

                    #message = urllib_post(config.req_crawler_url,data)

                    mysql.table('article_info').add(data)

            #更新最新推送ID
            if(last_qunfa_id < cur_qunfa_id):
                mysql.where_sql = " _id=%s" %(item['_id'])
                mysql.table('wechat_info_list').save({'last_qunfa_id':cur_qunfa_id,'last_qufa_time':qunfa_time,'update_time':time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))})
        except KeyboardInterrupt:
            break
        # except: #如果不想因为错误使程序退出，可以开启这两句代码
        #     print u"出错，继续"
        #     continue

    print('success')