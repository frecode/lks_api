# Generated by Django 3.2.7 on 2021-10-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_webreceive'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='接口标题')),
            ],
        ),
    ]