# Generated by Django 3.2.4 on 2021-06-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام شرکت')),
                ('generalManager', models.CharField(max_length=200, verbose_name='نام مدیرعامل')),
                ('createDate', models.DateField(verbose_name='تاریخ ثبت')),
                ('createNumber', models.IntegerField(verbose_name='شماره ثبت')),
                ('logoAddress', models.TextField(verbose_name='نام فایل لوگو')),
                ('portfolio', models.IntegerField(choices=[(1, 'بالادستی'), (2, 'پایین دستی'), (3, 'برق و یوتیلیتی')], verbose_name='پرتفولیو')),
            ],
            options={
                'verbose_name': 'شرکت',
                'verbose_name_plural': 'شرکت',
            },
        ),
    ]
