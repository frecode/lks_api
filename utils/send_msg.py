import time
import requests
from lks_api.settings import WECHAT_CONFIG, USER_ID


def get_access_token():
    """
    获取微信全局接口的凭证(默认有效期俩个小时)
    如果不每天请求次数过多, 通过设置缓存即可
    """
    result = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": WECHAT_CONFIG['app_id'],
            "secret": WECHAT_CONFIG['appsecret'],
        }
    ).json()
    if result.get("access_token"):
        access_token = result.get('access_token')
    else:
        access_token = None
    return access_token


def send_template_msg(data):
    """
    发送微信模版消息
    :param data:
    :return:
    """
    name_ = "标题："
    content_ = "详细描述："
    access_token = get_access_token()
    res = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/template/send",
        params={
            'access_token': access_token
        },
        json={
            "touser": USER_ID,
            "template_id": WECHAT_CONFIG['template_id'],
            "data": {
                "name_": {
                    "value": name_,
                    "color": "#666"
                },
                "content_": {
                    "value": content_,
                    "color": "#666"
                },
                "ip_": {
                    "value": name_,
                    "color": "#666"
                },
                "time_": {
                    "value": "时间：",
                    "color": "#666"
                },
                "name": {
                    "value": data["title"],
                    "color": "#173177"
                },
                "content": {
                    "value": data["content"],
                },
                "time": {
                    "value": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                    "color": "#173177"
                },
                "ip": {
                    "value": 'null',
                    "color": "#666"
                },
            }
        }
    )
    if res.json().get('errcode') == 0:
        print('微信推送成功')
    else:
        print('微信推送失败')