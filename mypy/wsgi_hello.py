def application(env,start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])  #响应状态  和headers
    return [b'<h1>Hello, web!</h1>']     #html页面