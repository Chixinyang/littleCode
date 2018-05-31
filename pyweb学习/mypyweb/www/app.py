#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
async web application.
'''

import logging, logging.config

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

from config import configs

import orm
from coroweb import add_routes, add_static

from handlers import cookie2user, COOKIE_NAME
# 采用配置文件,配置日志
if os.name == 'posix':  #根据操作系统选取配置文件
    LogConfPath="../conf/loggingLinux.conf"
else :
    LogConfPath = "..\conf\loggingWin.conf"
logging.config.fileConfig(LogConfPath)
# create logger
logger = logging.getLogger("simpleExample")  # 选取日志对象


def init_jinja2(app, **kw):  #配置jinja2网页模板，**kw 把后续多个输入参数组成一个字典
    logging.info('init jinja2...')
    options = dict(
        autoescape=kw.get('autoescape', True),  #自动编码
        block_start_string=kw.get('block_start_string', '{%'),  #块开始标记
        block_end_string=kw.get('block_end_string', '%}'),      #块结束
        variable_start_string=kw.get('variable_start_string', '{{'),    #变量开始
        variable_end_string=kw.get('variable_end_string', '}}'),    #变量结束
        auto_reload=kw.get('auto_reload', True))    #自动加载？？？
    path = kw.get('path', None) 
    if path is None:
        path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'templates')  #获得模板的绝对路径
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options) #环境：设置模板加载方式为文件加载
    filters = kw.get('filters', None)  #获取过滤器
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f   #环境：过滤器添加
    app['__templating__'] = env # 


@asyncio.coroutine
def logger_factory(app, handler):   #日志的中间操作
    @asyncio.coroutine
    def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        # yield from asyncio.sleep(0.3)
        return (yield from handler(request))

    return logger


@asyncio.coroutine
def auth_factory(app, handler): #验证的中间操作
    @asyncio.coroutine
    def auth(request):
        logging.info('check user: %s %s' % (request.method, request.path))
        request.__user__ = None
        cookie_str = request.cookies.get(COOKIE_NAME) #从请求中提取COOKIE_NAME字段-》包含用户名和密码
        if cookie_str:  #如果存在
            user = yield from cookie2user(cookie_str) #在服务端创建用户的cookie
            if user:
                logging.info('set current user: %s' % user.email) #打印user email
                request.__user__ = user #想request中添加__user__
        if request.path.startswith('/manage/') and (request.__user__ is None or request.__user__.admin):
            #mangage 开始的界面 或者__user__不存在 或者管理员都调到登录页
            return web.HTTPFound('/signin')
        return (yield from handler(request))

    return auth


@asyncio.coroutine
def data_factory(app, handler):
    @asyncio.coroutine
    def parse_data(request):
        if request.method == 'POST':
            if request.content_type.startswith('application/json'):
                request.__data__ = yield from request.json()
                logging.info('request json: %s' % str(request.__data__))
            elif request.content_type.startswith(
                    'application/x-www-form-urlencoded'):
                request.__data__ = yield from request.post()
                logging.info('request form: %s' % str(request.__data__))
        return (yield from handler(request))

    return parse_data


@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        logging.info('Response handler...')
        r = yield from handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            template = r.get('__template__')
            if template is None:
                resp = web.Response(
                    body=json.dumps(
                        r, ensure_ascii=False, default=lambda o: o.__dict__)
                    .encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                r['__user__'] = request.__user__
                resp = web.Response(body=app['__templating__'].get_template(
                    template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and t >= 100 and t < 600:
            return web.Response(t)
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            if isinstance(t, int) and t >= 100 and t < 600:
                return web.Response(t, str(m))
        # default:
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp

    return response


def datetime_filter(t):#修改了默认的datetime（t）
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)


@asyncio.coroutine
def init(loop):
    yield from orm.create_pool(loop=loop, **configs.db) #创建数据库连接池，传入数据库的配置信息
    app = web.Application( #通过webapp构架函数构建web App
        loop=loop,  #loop
        middlewares=[logger_factory, auth_factory, response_factory] ) #传入中间操作函数
        #middleware的用处就在于把通用的功能从每个URL处理函数中拿出来，集中放到一个地方
    init_jinja2(app, filters=dict(datetime=datetime_filter)) #初始化jinja2模板，传入app，以及过滤器
    add_routes(app, 'handlers') #注册app的路由处理
    add_static(app) #添加app的静态文件路径
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000) #创建服务
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
