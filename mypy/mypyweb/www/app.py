import logging 
import logging.config
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
import aiomysql
import jinja2

logging.config.fileConfig("D:\mydocument\GIT\mygit\littleCode\mypy\mypyweb\conf\logging.conf")    # 采用配置文件,配置日志
 # create logger  
logger = logging.getLogger("simpleExample")  # 选取日志对象

from myorm import create_pool
from myorm import IntegerField,StringField,DateTimeField,TextField,Model

'''
async def mytest(time):
    # 创建实例:
    user =  user_info(user_id=123,user_name='Michael',password='ccc',create_date=time,comment='ooo')
    # 存入数据库:
    await user.save()
    # 查询所有User对象:
    users = user_info.findAll()
    logging.info(users)
'''
import mymodule
async def dbtest():
    user = mymodule.users(
            id='2',
            email='100@qq.com',
            passwd='2'
            )
    await user.save()
    alluser=mymodule.users.findAll()
    logging.info(alluser)

async def index(request):  #主页
    curTime=time.strftime("%Y-%m-%d %X",time.localtime())
    #await mytest(curTime);
    await dbtest()
    html="<h1>Awesome:{}</h1>".format(curTime)
    return web.Response(body=html,content_type='text/html') #写html页面时，要制定文档类型

async def init(loop):
    app = web.Application(loop=loop)
    await create_pool(loop,     
                    host='localhost',
                    port= 3306,
                    user='root',
                    password='root',
                    db='myweb'
                )
    app.router.add_route('GET', '/', index)  #通过get 方法 访问根目录，会触发index函数
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

if __name__ == '__main__' :
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()