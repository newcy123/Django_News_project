from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('newsdetail/',views.newsdetail,name='newsdetail'),
    path('addnews/',views.addnews),
    path('addnewsdata/',views.addnewsdata,name='addnewsdata'),
    path('contentmanager/',views.contentmanager),
    path('contentedit/',views.contentedit,name='contentedit'),
    path('contentupdate/',views.contentupdate,name='contentupdate'),
    path('contentdelete/',views.contentdelete,name='contentdelete'),
    path('serachnews/',views.serachnews,name='serachnews'),

   
   
   path('registeruser/',views.registeruser),
   path('adduser/',views.adduser,name='adduser'),
   path('login/',views.login),
   path('logincheck/',views.logincheck,name="logincheck"),
   path('logoff/',views.logoff),

   path('warning/',views.warning),
   path('covid19/',views.covid19),

   
   
    path('result/',views.result,name="result")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) #เกี่ยวกับรูป,เกี่ยวกับ static

