
import asyncio, logging
import aiomysql
import logging.config
import sqlalchemy
logging.config.fileConfig("D:\mydocument\GIT\mygit\littleCode\mypy\mypyweb\conf\logging.conf")    # 采用配置文件,配置日志
 # create logger  
logger = logging.getLogger("simpleExample")  # 选取日志对象

def log(sql,args=''):
    logging.info('SQL: %s' % sql)

# 链接数据库创建连接池，封装成一个函数
'''
async def create_pool(loop, **kw):  
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host='localhost',
        port= 3306,
        user='root',
        password='root',
        db='cxy',
        loop=loop
    )
'''
async def create_pool(loop, **kw):  
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )
async def select(sql, args=None, size=None): #定义select
    log(sql, args)
    global __pool
    async with __pool.get() as conn: #获取一个连接
        async with conn.cursor(aiomysql.DictCursor) as cur:  #获取一个字典游标
            await cur.execute(sql.replace('?', '%s'), args or ()) #替换占位符，执行sql
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs   #返回查询结果
async def test(loop):
    await create_pool(loop,
                    host='localhost',
                    port= 3306,
                    user='root',
                    password='root',
                    db='myweb'
                )
    sql="select * from users"
    print(sql)
    rs = await select(sql);
    print(rs)
if __name__ == '__main__' :  
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.run_forever()