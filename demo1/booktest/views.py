from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import BookInfo,HeroInfo
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
    bl = BookInfo.objects.all()
    return render(request,'booktest/list.html',{'booklist':bl})

def detail(request,id):
    try:
        # book = BookInfo.objects.get(pk=id)
        # return HttpResponse(book)
        bookid = BookInfo.objects.get(pk=id)
        return render(request,'booktest/detail.html',{'book':bookid})
    except:
        return HttpResponse('请输入正确id')

def delete(request,id):
    try:
        BookInfo.objects.get(pk=id).delete()
        bl = BookInfo.objects.all()
        # 使用render没有刷新请求url
        # return render(request, 'booktest/list.html', {'booklist': bl})
        return HttpResponseRedirect('booktest/list/',{'booklist':bl})

    except:
        return HttpResponse('删除成功')

def addhero(request,bookid):
    return render(request, 'booktest/addhero.html', {'bookid': bookid})

def addherohandler(request):
    bookid = request.POST['bookid']
    hname = request.POST['heroname']
    hgender = request.POST['gender']
    hcontent = request.POST['herocontent']

    book = BookInfo.objects.get(pk=bookid)
    hero = HeroInfo()
    hero.hname = hname
    # hero.hgender = True
    if hero.hgender == '1':
        hero.hgender = True
    elif hero.hgender =='0':
        hero.hgender = False
    else:
        print('出现错误')
    hero.hcontent = hcontent
    hero.hbook = book
    hero.save()
    return HttpResponseRedirect('/booktest/detail/'+str(bookid)+'/',{'book':book})
    # return HttpResponse('OK')





