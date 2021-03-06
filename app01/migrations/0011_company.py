# Generated by Django 2.1.1 on 2018-09-30 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20180929_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(verbose_name='权重')),
                ('url', models.CharField(max_length=100, verbose_name='企业链接')),
                ('logo', models.ImageField(upload_to='static/images/company', verbose_name='LOGO')),
                ('name', models.CharField(max_length=100, verbose_name='公司名称')),
            ],
            options={
                'verbose_name': '企业合作',
            },
        ),
    ]
