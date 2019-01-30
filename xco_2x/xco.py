#!/usr/bin/env python
# coding=utf-8

import sys
import datetime
import xml.etree.ElementTree as ET

reload(sys)
sys.setdefaultencoding('utf8')

####################################################################################
class DataType:

    INT_TYPE = 3                    #
    LONG_TYPE = 4                   #
    FLOAT_TYPE = 5                  #
    DOUBLE_TYPE = 6                 #
    STRING_TYPE = 9                 #
    XCO_TYPE = 10                   #
    DATE_TYPE = 11                  #
    SQLDATE_TYPE = 12               #
    SQLTIME_TYPE = 13               #

    BIGINTEGER_TYPE = 15            #
    BIGDICIMAL_TYPE = 16            #

    INT_ARRAY_TYPE = 23             #
    LONG_ARRAY_TYPE = 24            #
    FLOAT_ARRAY_TYPE = 25           #
    DOUBLE_ARRAY_TYPE = 26          #
    STRING_ARRAY_TYPE = 29          #
    XCO_ARRAY_TYPE = 30             #

    STRING_LIST_TYPE = 49           #
    XCO_LIST_TYPE = 50              #

    PROPERTY_K = "K"
    PROPERTY_V = "V"

    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"


####################################################################################
class StringBuilder:

    def __init__(self):
        self.value = ""

    def append(self, _str):
        self.value = ''.join((self.value, _str))

    def toString(self):
        return self.value


class XCOUtil:

    @staticmethod
    def encodeTextForXML(_str):
        if 0 == len(_str):
            return _str

        builder = StringBuilder()
        for i in _str:
            if "&" == i:
                builder.append(u"&amp;")
            elif ">" == i:
                builder.append(u"&gt;")
            elif "<" == i:
                builder.append(u"&lt;")
            elif "'" == i:
                builder.append(u"&apos;")
            elif "\"" == i:
                builder.append(u"&quot;")
            elif "\r" == i:
                pass
            elif "\n" == i:
                builder.append(u"&#xa;")
            else:
                builder.append(i)

        return builder.toString()

    @staticmethod
    def encodeTextForJSON(_str):
        if 0 == len(_str):
            return _str
        _str = _str.replace("\\", "\\\\")
        _str = _str.replace("\"", "\\\"")
        return _str

    @staticmethod
    def getDateTimeString(val):
        return val.strftime(DataType.DATETIME_FORMAT)

    @staticmethod
    def getDateString(val):
        return val.strftime(DataType.DATE_FORMAT)

    @staticmethod
    def getTimeString(val):
        return val.strftime(DataType.TIME_FORMAT)

    @staticmethod
    def parseDateTime(val):
        return datetime.datetime.strptime(val, DataType.DATETIME_FORMAT)

    @staticmethod
    def parseDate(val):
        return datetime.datetime.strptime(val, DataType.DATE_FORMAT)

    @staticmethod
    def parseTime(val):
        return datetime.datetime.strptime(val, DataType.TIME_FORMAT)


####################################################################################
class IField:

    def getValue(self):
        pass

    # builder:StringBuilder
    def toXMLString(self, builder):
        pass

    def toJSONString(self, builder):
        pass

    def arrayToString(self, arr):
        b = StringBuilder()
        for i in range(len(arr)):
            if i > 0:
                b.append(",")
            b.append("{}".format(arr[i]))
        return b.toString()


####################################################################################
class IntegerField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<I " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append("{}".format(self.value))
        builder.append(u"\"/>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append("{}".format(self.value))


class LongField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<L " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append("{}".format(self.value))
        builder.append(u"\"/>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append("{}".format(self.value))


class FloatField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<F " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append("{}".format(self.value))
        builder.append(u"\"/>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append("{}".format(self.value))


class DoubleField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<D " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append("{}".format(self.value))
        builder.append(u"\"/>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append("{}".format(self.value))


class BigIntegerField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<K " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append("{}".format(self.value))
        builder.append(u"\"/>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append("{}".format(self.value))


class BigDecimalField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<M " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append("{}".format(self.value))
        builder.append(u"\"/>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append("{}".format(self.value))


class StringField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<S " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        # builder.append(XCOUtil.encodeTextForXML(self.value))
        # 2.x
        builder.append(unicode(XCOUtil.encodeTextForXML(self.value)))
        builder.append(u"\"/>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"\"")
        builder.append(unicode(XCOUtil.encodeTextForJSON(self.value)))
        # builder.append(XCOUtil.encodeTextForJSON(self.value))
        builder.append(u"\"")


class DateTimeField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<A " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append(XCOUtil.getDateTimeString(self.value))
        builder.append(u"\"/>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"\"")
        builder.append(XCOUtil.getDateTimeString(self.value))
        builder.append(u"\"")


class SqlDateField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<E " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append(XCOUtil.getDateString(self.value))
        builder.append(u"\"/>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"\"")
        builder.append(XCOUtil.getDateString(self.value))
        builder.append(u"\"")


class SqlTimeField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<G " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append(XCOUtil.getTimeString(self.value))
        builder.append(u"\"/>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"\"")
        builder.append(XCOUtil.getTimeString(self.value))
        builder.append(u"\"")


class XCOField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        self.value._toXMLString(self.name, builder)

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(self.value.toJSON())


class IntegerArrayField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<IA " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append(IField.arrayToString(self, self.value))
        builder.append(u"\"/>")

    def setValue(self, str):
        self.value = []
        if 0 == len(str):
            return
        arr = str.split(",")
        for i in range(len(arr)):
            self.value.append(int(arr[i]))

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"[")
        builder.append(IField.arrayToString(self, self.value))
        builder.append(u"]")


class LongArrayField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<LA " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append(IField.arrayToString(self, self.value))
        builder.append(u"\"/>")

    def setValue(self, _str):
        self.value = []
        if 0 == len(_str):
            return
        arr = _str.split(",")
        for i in range(len(arr)):
            self.value.append(long(arr[i]))

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"[")
        builder.append(IField.arrayToString(self, self.value))
        builder.append(u"]")


class FloatArrayField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<FA " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append(IField.arrayToString(self, self.value))
        builder.append(u"\"/>")

    def setValue(self, _str):
        self.value = []
        if 0 == len(_str):
            return
        arr = _str.split(",")
        for i in range(len(arr)):
            self.value.append(float(arr[i]))

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"[")
        builder.append(IField.arrayToString(self, self.value))
        builder.append(u"]")


class DoubleArrayField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<DA " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\" " + DataType.PROPERTY_V + "=\"")
        builder.append(IField.arrayToString(self, self.value))
        builder.append(u"\"/>")

    def setValue(self, _str):
        self.value = []
        if 0 == len(_str):
            return
        arr = _str.split(",")
        for i in range(len(arr)):
            self.value.append(float(arr[i]))

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"[")
        builder.append(IField.arrayToString(self, self.value))
        builder.append(u"]")


class StringArrayField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<SA " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\">")
        for i in range(len(self.value)):
            builder.append(u"<S " + DataType.PROPERTY_V + "=\"")
            # builder.append(XCOUtil.encodeTextForXML(self.value[i]))
            builder.append(unicode(XCOUtil.encodeTextForXML(self.value[i])))
            builder.append(u"\"/>")
        builder.append(u"</SA>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"[")
        for i in range(len(self.value)):
            if i > 0:
                builder.append(u",")
            builder.append(u"\"")
            builder.append(unicode(XCOUtil.encodeTextForJSON(self.value[i])))
            builder.append(u"\"")
        builder.append(u"]")


class XCOArrayField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<XA " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\">")
        for i in range(len(self.value)):
            self.value[i]._toXMLString(None, builder)
        builder.append(u"</XA>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"[")
        for i in range(len(self.value)):
            if i > 0:
                builder.append(u",")
            builder.append(self.value[i].toJSON())
        builder.append(u"]")


class StringListField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<SL " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\">")
        for i in range(len(self.value)):
            builder.append(u"<S " + DataType.PROPERTY_V + "=\"")
            # builder.append(XCOUtil.encodeTextForXML(self.value[i]))
            builder.append(unicode(XCOUtil.encodeTextForXML(self.value[i])))
            builder.append(u"\"/>")
        builder.append(u"</SL>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"[")
        for i in range(len(self.value)):
            if i > 0:
                builder.append(u",")
            builder.append(u"\"")
            builder.append(unicode(XCOUtil.encodeTextForJSON(self.value[i])))
            builder.append(u"\"")
        builder.append(u"]")


class XCOListField(IField):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getValue(self):
        return self.value

    def toXMLString(self, builder):
        builder.append(u"<XL " + DataType.PROPERTY_K + "=\"")
        builder.append(self.name)
        builder.append(u"\">")
        for i in range(len(self.value)):
            self.value[i]._toXMLString(None, builder)
        builder.append(u"</XL>")

    def toJSONString(self, builder):
        builder.append(u"\"")
        builder.append(self.name)
        builder.append(u"\"")
        builder.append(u":")
        builder.append(u"[")
        for i in range(len(self.value)):
            if i > 0:
                builder.append(u",")
            builder.append(self.value[i].toJSON())
        builder.append(u"]")

####################################################################################
class XCO:

    def __init__(self):
        self.dateMap = {}
        self.fieldList = []
        self.fieldValueList = []

    # __del__

    # ==================== common ====================#

    def __putItem(self, field, fieldValue):
        if field in self.dateMap:
            self.dateMap[field] = fieldValue
            index = self.fieldList.index(field)
            self.fieldValueList[index] = fieldValue
        else:
            self.dateMap[field] = fieldValue
            self.fieldList.append(field)
            self.fieldValueList.append(fieldValue)

    def __setField(self, field, fieldValue):
        self.__putItem(field, fieldValue)

    def getCode(self):
        return self.__getValue("$$CODE")

    def getMessage(self):
        return self.__getValue("$$MESSAGE")

    def getData(self):
        return self.__getValue("$$DATA")

    def __getValue(self, field):
        if field in self.dateMap:
            return self.dateMap[field].getValue()
        else:
            return None

    def get(self, field):
        return self.__getValue(field)

    def remove(self, field):
        if self.exists(field):
            index = self.fieldList.index(field)
            del self.fieldList[index]
            del self.fieldValueList[index]
            del self.dateMap[field]

    def exists(self, field):
        if field in self.dateMap:
            return True
        else:
            return False

    def isEmpty(self):
        if 0 == len(self.dateMap):
            return True
        else:
            return False

    # ==================== set ====================#

    def setIntegerValue(self, field, var):
        self.__setField(field, IntegerField(field, var))

    def setLongValue(self, field, var):
        self.__setField(field, LongField(field, var))

    def setFloatValue(self, field, var):
        self.__setField(field, FloatField(field, var))

    def setDoubleValue(self, field, var):
        self.__setField(field, DoubleField(field, var))

    def setStringValue(self, field, var):
        # if None == var:
        if var is None:
            self.remove(field)
            return
        self.__setField(field, StringField(field, var))

    def setDateTimeValue(self, field, var):
        if var is None:
            self.remove(field)
            return
        self.__setField(field, DateTimeField(field, var))

    def setDateValue(self, field, var):
        if var is None:
            self.remove(field)
            return
        self.__setField(field, SqlDateField(field, var))

    def setTimeValue(self, field, var):
        if var is None:
            self.remove(field)
            return
        self.__setField(field, SqlTimeField(field, var))

    def setBigIntegerValue(self, field, var):
        if var is None:
            self.remove(field)
            return
        self.__setField(field, BigIntegerField(field, var))

    def setBigDecimalValue(self, field, var):
        if var is None:
            self.remove(field)
            return
        self.__setField(field, BigDecimalField(field, var))

    def setXCOValue(self, field, var):
        if var is None:
            self.remove(field)
        else:
            self.__setField(field, XCOField(field, var))

    def setIntegerArrayValue(self, field, var):
        if var is None:
            self.remove(field)
        else:
            self.__setField(field, IntegerArrayField(field, var))

    def setLongArrayValue(self, field, var):
        if var is None:
            self.remove(field)
        else:
            self.__setField(field, LongArrayField(field, var))

    def setFloatArrayValue(self, field, var):
        if var is None:
            self.remove(field)
        else:
            self.__setField(field, FloatArrayField(field, var))

    def setDoubleArrayValue(self, field, var):
        if var is None:
            self.remove(field)
        else:
            self.__setField(field, DoubleArrayField(field, var))

    def setStringArrayValue(self, field, var):
        if var is None:
            self.remove(field)
        else:
            self.__setField(field, StringArrayField(field, var))

    def setXCOArrayValue(self, field, var):
        if var is None:
            self.remove(field)
        else:
            self.__setField(field, XCOArrayField(field, var))

    def setStringListValue(self, field, var):
        if var is None:
            self.remove(field)
        else:
            self.__setField(field, StringListField(field, var))

    def setXCOListValue(self, field, var):
        if var is None:
            self.remove(field)
        else:
            self.__setField(field, XCOListField(field, var))

    # ==================== get ====================#

    # ==================== Serialization and deserialization ====================#

    def _fromXML0(self, element):
        # print type(element)
        for child in element:
            # print type(child)
            # print(child.tag)
            tag = child.tag
            if "I" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                self.__putItem(k, IntegerField(k, int(v)))
            elif "L" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                self.__putItem(k, LongField(k, long(v)))
            elif "F" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                self.__putItem(k, FloatField(k, float(v)))
            elif "D" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                self.__putItem(k, DoubleField(k, float(v)))
            elif "S" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                self.__putItem(k, StringField(k, v))
            elif "X" == tag:
                k = child.get(DataType.PROPERTY_K)
                xco = XCO()
                xco._fromXML0(child)
                self.__putItem(k, XCOField(k, xco))
            elif "A" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                self.__putItem(k, DateTimeField(k, XCOUtil.parseDateTime(v)))
            elif "E" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                self.__putItem(k, SqlDateField(k, XCOUtil.parseDate(v)))
            elif "G" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                self.__putItem(k, SqlTimeField(k, XCOUtil.parseTime(v)))

            elif "K" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                self.__putItem(k, BigIntegerField(k, long(v)))
            elif "M" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                self.__putItem(k, BigDecimalField(k, float(v)))

            elif "IA" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                fieldValue = IntegerArrayField(k, None)
                fieldValue.setValue(v)
                self.__putItem(k, fieldValue)
            elif "LA" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                fieldValue = LongArrayField(k, None)
                fieldValue.setValue(v)
                self.__putItem(k, fieldValue)
            elif "FA" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                fieldValue = FloatArrayField(k, None)
                fieldValue.setValue(v)
                self.__putItem(k, fieldValue)
            elif "DA" == tag:
                k = child.get(DataType.PROPERTY_K)
                v = child.get(DataType.PROPERTY_V)
                fieldValue = DoubleArrayField(k, None)
                fieldValue.setValue(v)
                self.__putItem(k, fieldValue)
            elif "SA" == tag:
                k = child.get(DataType.PROPERTY_K)
                arr = []
                for item in child:
                    arr.append(item.get(DataType.PROPERTY_V))
                fieldValue = StringArrayField(k, arr)
                self.__putItem(k, fieldValue)
            elif "XA" == tag:
                k = child.get(DataType.PROPERTY_K)
                arr = []
                for item in child:
                    xco = XCO()
                    xco._fromXML0(item)
                    arr.append(xco)
                fieldValue = XCOArrayField(k, arr)
                self.__putItem(k, fieldValue)

            elif "SL" == tag:
                k = child.get(DataType.PROPERTY_K)
                arr = []
                for item in child:
                    arr.append(item.get(DataType.PROPERTY_V))
                fieldValue = StringListField(k, arr)
                self.__putItem(k, fieldValue)
            elif "XL" == tag:
                k = child.get(DataType.PROPERTY_K)
                arr = []
                for item in child:
                    xco = XCO()
                    xco._fromXML0(item)
                    arr.append(xco)
                fieldValue = XCOListField(k, arr)
                self.__putItem(k, fieldValue)
            else:
                print("ERR:" + child.tag)

    @staticmethod
    def fromXML(_xml):
        xco = XCO()
        root = ET.fromstring(_xml)
        xco._fromXML0(root)
        return xco

    def _toXMLString(self, key, builder):
        if None == key:
            builder.append(u"<X>")
        else:
            builder.append(u"<X " + DataType.PROPERTY_K + u"=\"" + key + u"\">")

        for i in range(len(self.fieldValueList)):
            self.fieldValueList[i].toXMLString(builder)

        builder.append(u"</X>")

    def toXMLString(self):
        builder = StringBuilder()
        builder.append(u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        self._toXMLString(None, builder)
        return builder.toString()

    def toJSON(self):
        builder = StringBuilder()
        builder.append(u"{")
        for i in range(len(self.fieldValueList)):
            if i > 0:
                builder.append(u",")
            self.fieldValueList[i].toJSONString(builder)
        builder.append(u"}")
        return builder.toString()

    def toString(self):
        return self.toXMLString()

####################################################################################
