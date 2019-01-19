from django.contrib import admin

from app01.models import *


# 自己定义BxSlideAdmin
class BxSlideAdmin(admin.ModelAdmin):
    # 记录的展示，展示所列出的属性 list_display可以是一对多(publish)，不能多对多
    list_display = ('id','status','name','img','url')
    # 分页，每页显示2条记录
    list_per_page = 5
    # 按照属性查询，日期也可以的
    # date跟publish_name不能同时用的！！！ like查询的时候会出错的
    search_fields = ('name','status')
    # 右边列出查询的条件
    list_filter = ('name','status')
# 公告
class InformAdmin(admin.ModelAdmin):
    # 记录的展示，展示所列出的属性 list_display可以是一对多(publish)，不能多对多
    list_display = ('status', 'weight', 'title', 'summary', 'content')
    # 分页，每页显示2条记录
    list_per_page = 5
    # 按照属性查询，日期也可以的
    # date跟publish_name不能同时用的！！！ like查询的时候会出错的
    search_fields = ('title', 'status')
    # 右边列出查询的条件
    list_filter = ('title', 'status')
# 课程
class CoursemAdmin(admin.ModelAdmin):
    # 记录的展示，展示所列出的属性 list_display可以是一对多(publish)，不能多对多
    list_display = ('status', 'weight', 'img', 'name', 'summany')
    # 分页，每页显示2条记录
    list_per_page = 5
    # 按照属性查询，日期也可以的
    # date跟publish_name不能同时用的！！！ like查询的时候会出错的
    search_fields = ('name', 'status')
    # 右边列出查询的条件
    list_filter = ('name', 'status')
# 学生
class StudentAdmin(admin.ModelAdmin):
    # 记录的展示，展示所列出的属性 list_display可以是一对多(publish)，不能多对多
    list_display = ('id','status', 'weight', 'name', 'company', 'salary',"img")
    # 分页，每页显示2条记录
    list_per_page = 5
    # 按照属性查询，日期也可以的
    # date跟publish_name不能同时用的！！！ like查询的时候会出错的
    search_fields = ('name', 'status')
    # 右边列出查询的条件
    list_filter = ('name', 'status')
class StudentLetterAdmin(admin.ModelAdmin):
    # 记录的展示，展示所列出的属性 list_display可以是一对多(publish)，不能多对多
    list_display = ('id', 'student', 'weight', 'letter')
    # 分页，每页显示2条记录
    list_per_page = 5
    # 按照属性查询，日期也可以的
    # date跟publish_name不能同时用的！！！ like查询的时候会出错的
    search_fields = ('student', 'weight')
    # 右边列出查询的条件
    list_filter = ('student', 'weight')
class CompanyAdmin(admin.ModelAdmin):
    # 记录的展示，展示所列出的属性 list_display可以是一对多(publish)，不能多对多
    list_display = ('id','weight', 'url', 'logo', 'name')
    # 分页，每页显示2条记录
    list_per_page = 5
    # 按照属性查询，日期也可以的
    # date跟publish_name不能同时用的！！！ like查询的时候会出错的
    search_fields = ('weight', 'name')
    # 右边列出查询的条件
    list_filter = ('weight', 'name')

# 自己定义BxSlideAdmin
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','name','img','alias_name','summary','detail')
    list_per_page = 5
    # date跟publish_name不能同时用的！！！ like查询的时候会出错的
    search_fields = ('name','alias_name')
    # 右边列出查询的条件
    list_filter = ('name','alias_name')

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(BxSlide,BxSlideAdmin)
admin.site.register(Inform,InformAdmin)
admin.site.register(Course,CoursemAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(StudentLetter,StudentLetterAdmin)
admin.site.register(Company,CompanyAdmin)