from django.db import models

__all__ = ['Web', 'WebVersion', 'Mail', 'WebReceive']


class Web(models.Model):
    """ 网站推荐数据表 """
    kind = models.CharField(max_length=8, verbose_name='期数分类')
    title = models.CharField(max_length=32, verbose_name='网站标题')
    href = models.CharField(max_length=128, verbose_name='网站链接')
    slogan = models.CharField(max_length=64, verbose_name='网站简介')
    kind_name = models.CharField(max_length=16, verbose_name='分类名称')
    star = models.CharField(max_length=8, verbose_name='星标', null=True, blank=True)

    def __str__(self):
        return self.title


class WebVersion(models.Model):
    """ 数据版本号 """
    version = models.CharField(max_length=16, verbose_name='数据版本号')

    def __str__(self):
        return self.version


class Mail(models.Model):
    """ 留言 """
    title = models.CharField(max_length=32, verbose_name="标题")
    content = models.TextField(max_length=1024, verbose_name="详细描述")

    def __str__(self):
        return self.title


class WebReceive(models.Model):
    """ 收到的网站链接 """
    href = models.CharField(max_length=256, verbose_name="网站链接")
    content = models.TextField(max_length=256, verbose_name="网站描述")

    def __str__(self):
        return self.href
