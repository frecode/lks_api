from rest_framework import serializers
from .models import Web, WebVersion, Mail, WebReceive


class WebSerializer(serializers.ModelSerializer):
    """ 网站数据推荐 """

    class Meta:
        model = Web
        fields = '__all__'

    def create(self, validated_data):
        kind = validated_data['kind']
        title = validated_data['title']
        href = validated_data['href']
        slogan = validated_data['slogan']
        kind_name = validated_data['kind_name']
        star = validated_data['star']
        return Web.objects.create(kind=kind, title=title, href=href, slogan=slogan, kind_name=kind_name, star=star)


class WebVersionSerializer(serializers.ModelSerializer):
    """ 版本号 """

    class Meta:
        model = WebVersion
        fields = '__all__'

    def create(self, validated_data):
        version = validated_data['version']
        return WebVersion.objects.create(version=version)


class MailSerializer(serializers.ModelSerializer):
    """ 留言 """

    class Meta:
        model = Mail
        fields = "__all__"

    def create(self, validated_data):
        title = validated_data["title"]
        content = validated_data["content"]
        return Mail.objects.create(title=title, content=content)


class WebReceiveSerializer(serializers.ModelSerializer):
    """ 留言 """

    class Meta:
        model = WebReceive
        fields = "__all__"

    def create(self, validated_data):
        href = validated_data["href"]
        content = validated_data["content"]
        return WebReceive.objects.create(href=href, content=content)
