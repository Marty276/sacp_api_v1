# Generated by Django 4.2.5 on 2023-11-29 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_delete_works'),
    ]

    operations = [
        migrations.DeleteModel(
            name='To_Collect',
        ),
        migrations.DeleteModel(
            name='To_Pay_Or_Paid',
        ),
    ]