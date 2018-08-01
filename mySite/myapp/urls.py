from django.conf.urls import include, url
from . import views

urlpatterns = [
    #空の文字列にマッチなのでmySiteでインポートさせることによってアクセスをかけている。
    url(r'^$',views.index, name='index'),
    #template配下にファイルを設定
    # url(r'^myapp/templates',views.index_templates, name='index_templates'),
    url(r'^templates',views.index_templates, name='index_templates'),
    # url(r'<int:id>',views.index, name='index'),
]