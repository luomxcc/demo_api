from tools.api import request_tool
from tools.report import assert_tool


def test_lock(driver_data):
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = 'http://dev.guoyasoft.com:8080/user/lock'
    req = {'userName': driver_data['user_name']}
    headers = {
        'token': driver_data['token'],
        'charset': 'UTF-8',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    resp = request_tool.post_request(url, data=req, headers=headers)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)
