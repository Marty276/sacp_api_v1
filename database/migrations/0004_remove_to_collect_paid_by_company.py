# Generated by Django 4.2.5 on 2023-09-05 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_to_collect_to_pay_or_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='to_collect',
            name='paid_by_company',
        ),
    ]
