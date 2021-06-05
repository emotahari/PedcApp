from django.db import models

# Create your models here.

class Currency(models.Model):
    class Meta:
        verbose_name = 'ارز'
        verbose_name_plural = 'ارز'
    currencyName = models.CharField('نام ارز', max_length=100)



class Income(models.Model):
    class Meta:
        verbose_name = 'درآمد'
    verbose_name_plural = 'درآمد'
    projectName = models.CharField('نام پروژه/خدمت درامدی', max_length=100),
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    realIncomeQ1 = models.IntegerField("مقدار واقعی سه ماهه اول"),
    realIncomeQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم"),
    realIncomeQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم"),
    realIncomeQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم"),
    forcastIncomeQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول"),
    forcastIncomeQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم"),
    forcastIncomeQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم"),
    forcastIncomeQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم"),
    yearOfForcast = models.IntegerField(),


    def __str__(self):
        self.projectName




