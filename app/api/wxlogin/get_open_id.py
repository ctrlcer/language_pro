from flask import request
from runserver import app
from requests import get


def get_oid(CODE):
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code'
    appid = app.config['APPID']
    secret = app.config['SECRET']
    url = url.replace('APPID', str(appid))
    url = url.replace('SECRET', str(secret))
    url = url.replace('JSCODE', str(CODE))
    result = dict(get(url).json())
    dic = dict()
    dic["session_key"] = result["session_key"]
    dic["openid"] = result["openid"]
    return dic
