import json
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WebSerializer, WebVersionSerializer
from .models import Web, WebVersion


class ApiWeb(APIView):
    """ 网站推荐数据接口 """

    def get(self, request):
        """ 获取网站推荐数据 """
        queryset = Web.objects.all()
        ser_obj = WebSerializer(queryset, many=True)
        web_list = []
        for data in ser_obj.data:
            web_list.append({
                'kind': data['kind'],
                'title': data['title'],
                'href': data['href'],
                'slogan': data['slogan'],
                'kind_name': data['kind_name'],
                'star': data['star'],
            })
        return Response(web_list)


class ApiWebVersion(APIView):
    """ 数据版本号 """

    def get(self, request):
        """ 获取云端版本号 """
        queryset = WebVersion.objects.all()
        ser_obj = WebVersionSerializer(queryset, many=True)
        return Response({
            'version': ser_obj.data[-1]['version']
        })


def init_web(request):
    """ 初始化数据库 """
    with open('db/web_list.json', 'r') as f:
        web_list = json.load(f)
    for web in web_list:
        Web.objects.create(kind=web['kind'], title=web['title'], href=web['href'], slogan=web['slogan'],
                           kind_name=web['kind_name'], star=web['star'])
        print('网站写入成功「%s」' % web['title'])
    return HttpResponse('数据初始化成功')
