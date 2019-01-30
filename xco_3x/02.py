# coding=utf-8
# !/usr/bin/env python

from xco import XCO
from tangyuan import ServiceActuator

if __name__ == "__main__":

    # 服务地址
    # url = "http://api.ung.aixbx.com/analysis/aikang.xco"
    url = "http://aikang.mock.aixbx.service/mockReportService/getReportByCode"

    # 请求参数
    request = XCO()
    request.setStringValue("rp_code", "C160C37B97CE43BBBBD527D897A4C155")

    # 执行服务调用
    r = ServiceActuator.execute(url, request)

    # 结果输出r:XCO
    if 0 == r.getCode():
        # 服务的反馈成功, data为真实的返回对象(XCO类型)
        data = r.getData()
        print(data.toString())
    else:
        # 服务的反馈异常
        print("CODE[" + str(r.getCode()) + "], MESSAGE[" + r.getMessage() + "]")


