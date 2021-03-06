# Generated by Django 2.1.1 on 2018-09-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20180929_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, '线上'), (2, '线下')], default=1, verbose_name='状态')),
                ('weight', models.IntegerField()),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('company', models.CharField(max_length=50, verbose_name='就业单位')),
                ('salary', models.IntegerField(verbose_name='薪水')),
            ],
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '课程'},
        ),
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(upload_to='static/images/course/', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=40, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.IntegerField(choices=[(1, '线上'), (2, '线下')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='course',
            name='summany',
            field=models.CharField(max_length=200, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='course',
            name='weight',
            field=models.IntegerField(verbose_name='权重'),
        ),
    ]
