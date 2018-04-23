# [tornado + Django + nginx + MySQL搭建网站 - CSDN博客]
# (https://blog.csdn.net/sinat_29957455/article/details/78759894)
# [使用Tornado作为Django App的服务器 - CSDN博客](https://blog.csdn.net/fancyyuan/article/details/49383575)
import os  
from tornado.options import options, define, parse_command_line  
from multiprocessing import Pool  
import tornado.httpserver  
import tornado.ioloop  
import tornado.web  
import tornado.wsgi  
from django.core.wsgi import get_wsgi_application  
define('port', type=int, default=8000)  

class HelloHandler(tornado.web.RequestHandler):  
    def get(self):  
        self.write('Hello from tornado:%s'%os.getpid())  


def run(port):  
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlockChain.settings')  
    parse_command_line()  
    
    wsgi_app = get_wsgi_application()  
    container = tornado.wsgi.WSGIContainer(wsgi_app)  
  
    tornado_app = tornado.web.Application(  
        [  
            ('/', HelloHandler),  
            ('.*', tornado.web.FallbackHandler, dict(fallback=container)),  
        ])  
  
    server = tornado.httpserver.HTTPServer(tornado_app)  
    server.listen(port)  
  
    tornado.ioloop.IOLoop.instance().start()  
  
if __name__ == '__main__':  
    pool = Pool(4)  
    pool.map(run,[8000,8001,8002,8003]) 