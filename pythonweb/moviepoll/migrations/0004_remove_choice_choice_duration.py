# Generated by Django 2.1.5 on 2019-01-20 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviepoll', '0003_auto_20190120_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_duration',
        ),
    ]