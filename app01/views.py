from django.shortcuts import render,HttpResponse,redirect
from app01.models import *
from django.db.models import Max


# 教师团队
def teacher(request):
    teacher_list = Teacher.objects.all()[0:4];

    return render(request,"teacher.html",{"teacher_list":teacher_list})
# 首页
def index(request):
    # 获得轮播
    BxSlide_list = BxSlide.objects.all();
    # 公告
    inform_list = Inform.objects.all()[0:3]
    # 课程
    course_list = Course.objects.all()[0:3]
    # 权重最大的学生的二种方式：
    # 1.aggregate 是用在内置函数上的，结果是字典  {"weight_max":5}   5是权重值
    # print(stu_dict1)
    # stu_dict = Student.objects.values("id").aggregate(Max("weight"))
    # student = Student.objects.filter(weight=stu_dict["weight__max"])[0]
    # 2.order_by先排序，再选     -XXX倒序   XXX正序
    student = Student.objects.all().order_by("-weight")[0]
    # 查询学生的感谢信
    studentLetter = StudentLetter.objects.filter(student_id=student.id)[0]

    # 选出权重6个最大的学生
    student_list = Student.objects.all().order_by("-weight")[1:7]

    # 企业合作
    company_list = Company.objects.all()[0:7]
    return render(request , "index.html",
                  {
                     "BxSlide_list":BxSlide_list,
                      "inform_list":inform_list,
                      "course_list":course_list,
                      "student":student,
                      "studentLetter":studentLetter,
                      "student_list":student_list,
                      "company_list":company_list
                  }
    )

# 轮播图例子
def slider(request):
    return render(request,"slider.html")
