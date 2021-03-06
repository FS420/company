# Generated by Django 2.1.1 on 2018-09-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bxslider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('name', models.CharField(max_length=30)),
                ('img', models.FileField(upload_to='../static/images/bxslider/')),
                ('url', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '轮播图',
                'db_table': 'bxslider',
            },
        ),
    ]
