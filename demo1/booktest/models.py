from django.db import models
'''
设计和表对应的类，模型类
'''
# Create your models here.

# 一类
class BookInfo(models.Model):
    '''
    图书模型类
    类属性对应表中的字段
    '''
    #图书名称， CharField说明是一个字符串，max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)
    # 出版日期，DateTimeField说明是一个日期类型
    bpub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        #返回书名
        return self.btitle

    def xiaoshuo(self):
        return self.btitle
    xiaoshuo.short_description='金庸小说'

# 多类
class HeroInfo(models.Model):
    '''英雄人物模型类'''
    hname = models.CharField(max_length=20)
    # 性别，BooleanField说明bool类型，default指定默认值，False代表女
    hgender = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=20)
    # 关系属性，建立图书类和英雄人物类之间的一对多关系
    # 关系属性对应表的字段名格式：关系属性名_id
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    def __str__(self):
        # 返回英雄名
        return self.hname

    def name(self):
        return self.hname
    name.short_description='姓名'

    def gender(self):
        return self.hgender
    gender.short_description='性别'

    def actor(self):
        return self.hcontent
    actor.short_description='演员'


