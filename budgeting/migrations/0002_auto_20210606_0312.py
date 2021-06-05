# Generated by Django 3.2.4 on 2021-06-05 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'verbose_name': 'درآمد', 'verbose_name_plural': 'درآمد'},
        ),
        migrations.RemoveField(
            model_name='income',
            name='currency',
        ),
        migrations.AddField(
            model_name='income',
            name='forcastIncomeQ1',
            field=models.IntegerField(default=0, verbose_name='مقدار پیش بینی سه ماهه اول'),
        ),
        migrations.AddField(
            model_name='income',
            name='forcastIncomeQ2',
            field=models.IntegerField(default=0, verbose_name='مقدار پیش بینی سه ماهه دوم'),
        ),
        migrations.AddField(
            model_name='income',
            name='forcastIncomeQ3',
            field=models.IntegerField(default=0, verbose_name='مقدار پیش بینی سه ماهه سوم'),
        ),
        migrations.AddField(
            model_name='income',
            name='forcastIncomeQ4',
            field=models.IntegerField(default=0, verbose_name='مقدار پیش بینی سه ماهه چهارم'),
        ),
        migrations.AddField(
            model_name='income',
            name='isInGroupe',
            field=models.BooleanField(default=0, verbose_name='درآمد درون گروهی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='projectName',
            field=models.CharField(default='swww', max_length=100, verbose_name='نام پروژه/خدمت درامدی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='realIncomeQ1',
            field=models.IntegerField(default=0, verbose_name='مقدار واقعی سه ماهه اول'),
        ),
        migrations.AddField(
            model_name='income',
            name='realIncomeQ2',
            field=models.IntegerField(default=0, verbose_name='مقدار واقعی سه ماهه دوم'),
        ),
        migrations.AddField(
            model_name='income',
            name='realIncomeQ3',
            field=models.IntegerField(default=0, verbose_name='مقدار واقعی سه ماهه سوم'),
        ),
        migrations.AddField(
            model_name='income',
            name='realIncomeQ4',
            field=models.IntegerField(default=0, verbose_name='مقدار واقعی سه ماهه چهارم'),
        ),
        migrations.AddField(
            model_name='income',
            name='yearOfForcast',
            field=models.IntegerField(default=1400),
        ),
    ]
