# Generated by Django 2.2.12 on 2020-11-02 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0030_auto_20201102_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docshare',
            name='effective_time',
        ),
    ]