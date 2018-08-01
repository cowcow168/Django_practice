"""mySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import IndexTemplateView

#デフォルト
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# from django.conf.urls import include, url
# from django.contrib import admin
urlpatterns = [
    # 管理画面を表示する
    url(r'^admin/', admin.site.urls),
    #下の書き方だとhttp://127.0.0.1:8000/の入り口に来た時にmyappを指定しないとエラーになる。
    # url(r'^myapp/', include('myapp.urls')),
    #myappにリダイレクトさせる
    url(r'', include('myapp.urls')),
    #index_templates.htmlとヒモ付
    # url(r'^myapp/', include(('myapp.urls','myapp'),namespace='myapp')),
    #TemplateViewクラスを継承したviewのクラスを呼ぶように変更する
    url(r'^myapp/',IndexTemplateView.as_view()),
]

