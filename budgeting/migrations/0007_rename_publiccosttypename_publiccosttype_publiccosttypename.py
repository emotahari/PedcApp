# Generated by Django 3.2.4 on 2021-09-09 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0006_etcoprationalcost_etcoprationalincome_loancost_nonoprationalcost_nonoprationalincome_publiccost_publ'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publiccosttype',
            old_name='PublicCostTypeName',
            new_name='publicCostTypeName',
        ),
    ]