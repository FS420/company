# Generated by Django 2.1.1 on 2018-09-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20180929_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, '显示'), (2, '不显示')], default=1)),
                ('weight', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AlterField(
            model_name='bxslide',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
