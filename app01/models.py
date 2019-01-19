from django.db import models

# 老师信息
class Teacher(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="姓名"
    )
    img = models.ImageField(
        upload_to="./static/images/teacher"
    )
    alias_name = models.CharField(
        max_length=100,
        verbose_name="别名"
    )
    summary = models.CharField(
        max_length=1000,
        verbose_name="简介"
    )
    detail = models.CharField(
        max_length=2000,
        verbose_name="详细信息"
    )
    class Meta:
        verbose_name_plural="教师"


# 轮播图
class BxSlide(models.Model):
    status = models.IntegerField(
        choices=[(1,"线上"),(2,"线下")],
        default=1
    )
    name=models.CharField(
        null=False,
        max_length=30,
    )
    img=models.FileField(
        null=False,
        # 上传的路径
        upload_to="images/bxslider/"
    )
    url=models.CharField(
        null=False,
        max_length=200,
    )
    class Meta:
        # 数据库中生成的表名称  默认 app名称 + 下划线 + 类名
        db_table = "bxslider"
        # admin中显示的表名称
        verbose_name = "轮播图"

    def __str__(self):
        return self.name
# 公告
class Inform(models.Model):
    status = models.IntegerField(
        choices=[(1,"显示"),(2,"不显示")],
        default=1
    )
    weight = models.IntegerField()
    title = models.CharField(
        max_length=50,
    )
    # 简介
    summary = models.CharField(
        max_length=200
    )
    # 内容
    content=models.CharField(
        max_length=10000,
    )
    class Meta:
        verbose_name="公告"
# 课程
class Course(models.Model):
    status = models.IntegerField(
        choices=[(1,"线上"),(2,"线下")],
        default=1,
        verbose_name="状态"
    )
    weight = models.IntegerField(
        verbose_name="权重"
    )
    img = models.ImageField(
        verbose_name="图片",
        upload_to="static/images/course/"
    )
    name = models.CharField(
        verbose_name="名称",
        max_length=40
    )
    summany = models.CharField(
        verbose_name="简介",
        max_length=200,
    )
    class Meta:
        verbose_name="课程"
# 学生信息
class Student(models.Model):
    status = models.IntegerField(
        choices=[(1,"线上"),(2,"线下")],
        default=1,
        verbose_name="状态"
    )
    weight = models.IntegerField(
        verbose_name="权重"
    )
    img = models.ImageField(
        upload_to="static/images/avatar/",
        verbose_name="头像",
    )
    name = models.CharField(
        max_length=30,
        verbose_name="姓名"
    )
    company = models.CharField(
        max_length=50,
        verbose_name="就业单位"
    )
    salary=models.IntegerField(
        verbose_name="薪水"
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="学生表"
# 学生的感谢信
class StudentLetter(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=True,
        verbose_name="学生"
    )
    weight = models.IntegerField(
        verbose_name="权重"
    )
    letter  = models.CharField(
        max_length=1000,
        verbose_name="学员感谢信"
    )
    class Meta:
        verbose_name="学生更多信息"


# 企业合作
class Company(models.Model):
    weight = models.IntegerField(
        verbose_name="权重"
    )
    url = models.CharField(
        max_length=100,
        verbose_name="企业链接"
    )
    logo = models.ImageField(
        upload_to="static/images/company",
        verbose_name="LOGO"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="公司名称"
    )
    class Meta:
        verbose_name="企业合作"

class Xxx(models.Model):
    name=models.CharField(max_length=20)



