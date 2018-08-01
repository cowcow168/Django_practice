from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from .forms import ContactForm

#初期表示画面
def index(request):
    # return HttpResponse('This is urls test. id = ' + str(id))
    # return HttpResponse('This is urls test.')
    return render(request,'index_templates.html')

#ページの読み込まれる順番はまだ把握していない。
def index_templates(request):
    #フォームを追加する
    form = ContactForm()
    return render(request, 'myapp/templates/index.html',{
        'form': form,
    })


class IndexTemplateView(TemplateView):
    template_name = "myapp/templates/index.html"

    #多段になるのでTemplateViewのgetではなく、新たにメソッドを作って上げたほうが簡潔で読みやすい
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "MyPages(管理画面をよばないように設定する必要あり)"
        return context


