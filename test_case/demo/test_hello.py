def test_login():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = 'http://dev.guoyasoft.com:8080/login'
    req = {
        "pwd": "dl4xw0Lm",
        "userName": "wUV647"
    }
    resp = request_tool.post_request(url,json=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['code'],2000)
    data =body['data']
    if data !='':
        token = data['token']
        assert_tool.assert_not_null(token)
