import logging 
import logging.config
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web
logging.config.fileConfig("D:\mydocument\GIT\mygit\littleCode\mypy\mypyweb\conf\logging.conf")    # 采用配置文件,配置日志
 # create logger  
logger = logging.getLogger("simpleExample")  # 选取日志对象

def index(request):  #主页
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html') #写html页面时，要制定文档类型

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)  #通过get 方法 访问根目录，会触发index函数
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()