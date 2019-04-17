from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from django.template import loader

# Create your views here.
# 定义视图函数
def index(request):
    # print('请求',request)
    # return HttpResponse('首页')
    # # 加载模板
    # indextem = loader.get_template('booktest/index.html')
    # cont = {'username':'ltt'}
    # # 使用变量参数渲染模板
    # result = indextem.render(cont)
    # # 返回模板
    # return HttpResponse(result)
    return render(request,'booktest/index.html',{'username':'ltt'})

def list(request):
    # return HttpResponse('列表页')
    b1 = BookInfo.objects.all()
    return render(request,'booktest/list.html',{'booklist':b1})

def detail(request,id):
    try:
        # book = BookInfo.objects.get(pk=id)
        # return HttpResponse(book)
        bookid = BookInfo.objects.get(pk=id)
        return render(request,'booktest/detail.html',{'book':bookid})
    except:
        return HttpResponse('请输入正确id')