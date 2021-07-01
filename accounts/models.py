from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Company(models.Model):
    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت'

    name = models.CharField(max_length=200, verbose_name='نام شرکت')
    generalManager = models.CharField(max_length=200, verbose_name='نام مدیرعامل')
    createDate = models.DateField(verbose_name='تاریخ ثبت')
    createNumber = models.IntegerField(verbose_name='شماره ثبت')
    logoAddress = models.TextField(verbose_name='نام فایل لوگو')
    UP_STREAM = 1
    DOWN_STREAM = 2
    Utility = 3
    portfolioChoice = (
        (UP_STREAM, 'بالادستی'),
        (DOWN_STREAM, 'پایین دستی'),
        (Utility, 'برق و یوتیلیتی'),
    )

    portfolio = models.IntegerField(choices=portfolioChoice, verbose_name='پرتفولیو')

    def __str__(self):
        return self.name

    def __get__(self, instance, owner):
        return self


class ProfileAuth(models.Model):
    companyAuth = models.ForeignKey(Company, on_delete=models.PROTECT)
    userAuth = models.ForeignKey(User, on_delete=models.PROTECT)


