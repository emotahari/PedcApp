# Generated by Django 3.2.4 on 2021-06-19 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('budgeting', '0004_auto_20210612_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costTypeName', models.CharField(max_length=100, null=True, verbose_name='نوع هزینه')),
            ],
            options={
                'verbose_name': 'نوع هزینه',
                'verbose_name_plural': 'نوع هزینه',
            },
        ),
        migrations.CreateModel(
            name='CostOfSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=100, null=True, verbose_name='نام محصول/خدمت درامدی')),
                ('realCostQ1', models.IntegerField(default=0, verbose_name='مقدار واقعی سه ماهه اول')),
                ('realCostQ2', models.IntegerField(default=0, verbose_name='مقدار واقعی سه ماهه دوم')),
                ('realCostQ3', models.IntegerField(default=0, verbose_name='مقدار واقعی سه ماهه سوم')),
                ('realCostQ4', models.IntegerField(default=0, verbose_name='مقدار واقعی سه ماهه چهارم')),
                ('forcastCostQ1', models.IntegerField(default=0, verbose_name='مقدار پیش بینی سه ماهه اول')),
                ('forcastCostQ2', models.IntegerField(default=0, verbose_name='مقدار پیش بینی سه ماهه دوم')),
                ('forcastCostQ3', models.IntegerField(default=0, verbose_name='مقدار پیش بینی سه ماهه سوم')),
                ('forcastCostQ4', models.IntegerField(default=0, verbose_name='مقدار پیش بینی سه ماهه چهارم')),
                ('yearOfForcast', models.IntegerField(default=1400)),
                ('isInGroupe', models.BooleanField(default=0, verbose_name='هزینه درون گروهی')),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='accounts.company')),
                ('costType', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='budgeting.costtype')),
                ('currency', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='budgeting.currency')),
            ],
            options={
                'verbose_name': 'قیمت تمام شده',
                'verbose_name_plural': 'قیمت تمام شده',
            },
        ),
    ]
