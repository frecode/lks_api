# Generated by Django 3.2.7 on 2021-10-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20211009_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('content', models.CharField(max_length=1024, verbose_name='详细描述')),
            ],
        ),
    ]
