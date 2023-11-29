# Generated by Django 4.2.5 on 2023-11-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_to_collect_company_name_to_pay_or_paid_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256)),
                ('work_data', models.JSONField()),
                ('worker_name', models.CharField(max_length=256)),
                ('company_name', models.CharField(blank=True, max_length=256)),
                ('totals', models.JSONField(blank=True)),
                ('status', models.CharField(max_length=256)),
                ('dates', models.JSONField()),
                ('notes', models.TextField(blank=True, max_length=1024)),
            ],
        ),
    ]