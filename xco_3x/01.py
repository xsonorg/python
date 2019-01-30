# coding=utf-8
# !/usr/bin/env python
from xco import XCO

import datetime

if __name__ == "__main__":

    xco = XCO()

    xco.setIntegerValue("i1", 12)
    xco.setStringValue("s2", u"中'\"><<><>dfsj\kafdsjk,?$%")
    # xco.setStringValue("s2", u"中'")

    xco.setFloatValue("f3", 3.9)
    xco.setDoubleValue("d4", -0.0007)
    xco.setLongValue("l5", 234324)

    xco.setIntegerArrayValue("ia", [1, 2, 3])
    xco.setLongArrayValue("la", [1, 23])
    xco.setFloatArrayValue("fa", [1, 0.23])
    xco.setDoubleArrayValue("da", [1.00, 23])
    xco.setStringArrayValue("sa", ["a", "b", u"你好"])

    xco1 = XCO()
    xco1.setIntegerValue("a", 23)
    xco1.setIntegerValue("david", 2345435)

    xco.setXCOValue("xco1", xco1)
    xco.setXCOArrayValue("xa", [xco1, xco1])
    xco.setStringListValue("sl", ["a", "b", u"你好"])
    xco.setXCOListValue("xl", [xco1, xco1])

    xco.setDateTimeValue("DT1", datetime.datetime.now())
    xco.setDateValue("DT2", datetime.datetime.now())
    xco.setTimeValue("DT3", datetime.datetime.now())

    xco.setBigIntegerValue("B1", 12121212)
    xco.setBigDecimalValue("B2", 12121212.234324324324)

    # print(xco.get("s2"))
    # print ["a", "b", u"你好"]
    # print(xco.get("sa")[2])

    xml = xco.toString()
    print(xml)

    print("")

    nXCO = XCO.fromXML(xml)
    print(nXCO.toString())

    print(nXCO.toJSON())
