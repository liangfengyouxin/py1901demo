from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import BookInfo,HeroInfo   #导入图书模型类和英雄模型类
from django.template import loader,RequestContext

# Create your views here.

# 定义视图函数,request是HttpRequest类型的对象
def index(request):
    # 进行处理，与M和T进行交互。。。最后给浏览器返回一个应答
    # # 1.加载模板文件，得到模板对象
    # indextem = loader.get_template('booktest/index.html')
    # # 2.定义模板上下文：给模板文件传递数据
    # cont = RequestContext(request,{'username':'zzt'})
    # # 3.使用变量参数渲染模板:产生标准的html内容
    # result = indextem.render(cont)
    # # 返回给浏览器
    # return HttpResponse(result)
    return render(request,'booktest/index.html',{'username':'zzt'})

def list(request):
    # return HttpResponse('列表页')
    #1.通过M查找图书表中的数据
    bl = BookInfo.objects.all()
    # 2.使用模板
    return render(request,'booktest/list.html',{'booklist':bl})

def detail(request,id):
    '''查询图书关联英雄信息'''
    try:
        # book = BookInfo.objects.get(pk=id)
        # return HttpResponse(book)
        # 1.根据id查询图书信息
        bookid = BookInfo.objects.get(pk=id)
        print(bookid)
        # 2.查询和bookid关联的英雄信息
        heros = bookid.heroinfo_set.all()
        # 3.使用模板
        return render(request,'booktest/detail.html',{'book':bookid,'heros':heros})
    except:
        return HttpResponse('请输入正确id')

def delete(request,id):
    BookInfo.objects.get(pk=id).delete()
    bl = BookInfo.objects.all()
    # 使用render没有刷新请求url
    # return render(request, 'booktest/list.html', {'booklist': bl})
    return HttpResponseRedirect('/list/',{'booklist':bl})


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

    if hero.hgender == '1':
        hero.hgender = True
    elif hero.hgender =='0':
        hero.hgender = False
    else:
        print('出现错误')
    hero.hcontent = hcontent
    hero.hbook = book
    hero.save()
    return HttpResponseRedirect('/detail/'+str(bookid)+'/',{'book':book})
    # return HttpResponse('OK')





