
# Deploying Django

## make tornado as a server(wsgi)
* [超实用压力测试工具－ab工具 - CSDN博客](https://blog.csdn.net/u012891504/article/details/53436808)
```
ab -n 10000 -c 10 http://127.0.0.1:8000/
```

## Deployment schema 
* django + nginx + (tornado)
* uwsgi + nginx
* gunicorn + nginx
* gunicorn + nginx + gevent (gunicorn -k gevent)



## Refer
1. [Deploying Django | Django documentation | Django](https://docs.djangoproject.com/en/dev/howto/deployment/)
2. [How to use Django with **Gunicorn** | Django documentation | Django](https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/gunicorn/)
3. [How to use Django with **uWSGI** | Django documentation | Django](https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/uwsgi/)
4. [Django|Tornado项目部署 - CSDN博客](https://blog.csdn.net/selectY/article/details/78502788?locationNum=9&fps=1)
5. [Python Django 生产环境部署到 Ucloud - 简书](https://www.jianshu.com/p/55c3fc8ea9b0)
6. [django-kit/**celery**.py at master · aFraley/django-kit](https://github.com/aFraley/django-kit/blob/master/project_name/celery.py)
7. [TodoApiList/celery.py at master · sharawy/TodoApiList](https://github.com/sharawy/TodoApiList/blob/master/TodoList/celery.py)
8. [celerywork/tasks.py at master · firetaker/celerywork](https://github.com/firetaker/celerywork/blob/master/workapp/tasks.py)
9. [Python Django **Celery** 实现异步任务 - CSDN博客](https://blog.csdn.net/xie_0723/article/details/78277707)
10. [django+django-celery+celery的整合 - CSDN博客](https://blog.csdn.net/yeyingcai/article/details/78647553)


## test
1. [Python Web服务器并发性能测试 - 51Testing软件测试网](http://www.51testing.com/html/82/n-3715882.html)
2. [siege压力测试工具安装和介绍 - CSDN博客](https://blog.csdn.net/shangmingtao/article/details/73850292)
3. [几款Web服务器性能压力测试工具 - CSDN博客](https://blog.csdn.net/u012942982/article/details/55251930)