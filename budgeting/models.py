from django.db import models


# Create your models here.

class Currency(models.Model):
    class Meta:
        verbose_name = 'ارز'
        verbose_name_plural = 'ارز'

    currencyName = models.CharField('نام ارز', max_length=100)

    def __str__(self):
        return self.currencyName

    def __get__(self, instance, owner):
        return self


class Income(models.Model):
    class Meta:
        verbose_name = 'درآمد'
        verbose_name_plural = 'درآمد'

    projectName = models.CharField('نام محصول/خدمت درامدی', max_length=100, null=True)
    realIncomeQ1 = models.IntegerField("مقدار واقعی سه ماهه اول", default=0)
    realIncomeQ2 = models.IntegerField("مقدار واقعی سه ماهه دوم", default=0)
    realIncomeQ3 = models.IntegerField("مقدار واقعی سه ماهه سوم", default=0)
    realIncomeQ4 = models.IntegerField("مقدار واقعی سه ماهه چهارم", default=0)
    forcastIncomeQ1 = models.IntegerField("مقدار پیش بینی سه ماهه اول", default=0)
    forcastIncomeQ2 = models.IntegerField("مقدار پیش بینی سه ماهه دوم", default=0)
    forcastIncomeQ3 = models.IntegerField("مقدار پیش بینی سه ماهه سوم", default=0)
    forcastIncomeQ4 = models.IntegerField("مقدار پیش بینی سه ماهه چهارم", default=0)
    yearOfForcast = models.IntegerField(default=1400)
    isInGroupe = models.BooleanField('درآمد درون گروهی', default=0)
    # currency = models.ForeignKey('Currency', on_delete=models.PROTECT)

    def __str__(self):
        return self.projectName
