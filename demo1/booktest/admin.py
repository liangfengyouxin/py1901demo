from django.contrib import admin
from .models import BookInfo,HeroInfo
# 后台管理相关文件
# Register your models here.
class HeroInfoInlines(admin.StackedInline):
    model = HeroInfo
    # 关联个数
    extra = 1


# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ['id','xiaoshuo','bpub_date']
    list_per_page = 5
    # 在添加书的时候，可以额外添加英雄
    inlines = [HeroInfoInlines]

# 注册模型类
admin.site.register(BookInfo,BookInfoAdmin)




class HeroInfoAdmin(admin.ModelAdmin):
    # 显示对象指定列，列名一致
    list_display = ['name','gender','actor']
    # 显示过滤规则，列名一致
    list_filter = ['hname','hgender']
    # 显示搜索字段，支持模糊查询
    search_fields = ['hname','hcontent']
    # 分页，每页显示个数
    list_per_page = 5

admin.site.register(HeroInfo,HeroInfoAdmin)