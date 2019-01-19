# Generated by Django 2.1.1 on 2018-10-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('alias_name', models.CharField(max_length=100, verbose_name='别名')),
                ('summary', models.CharField(max_length=1000, verbose_name='简介')),
                ('detail', models.CharField(max_length=2000, verbose_name='详细信息')),
            ],
            options={
                'verbose_name_plural': '教师',
            },
        ),
    ]
