# Generated by Django 3.2.7 on 2021-10-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='ip',
            field=models.CharField(default=1, max_length=1024, verbose_name='IP'),
            preserve_default=False,
        ),
    ]
