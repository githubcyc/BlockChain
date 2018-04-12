import os.path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from rest_demo import views
 
from rest_framework import routers
 
appname = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
 
router = routers.DefaultRouter()
router.register('users', views.UserViewSet, appname)
 
urlpatterns = [url(r'^', include(router.urls)),

]