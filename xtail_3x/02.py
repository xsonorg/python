# coding=utf-8
# !/usr/bin/env python

from xtail import XTail

if __name__ == "__main__":
    # s = "a123456c"
    # print s[1:-1]
    # _xtail = XTail(['xtail', 'C:/Users/Lenovo/Desktop/temp/x.log', "-ir", 'ERROR'])
    # _xtail = XTail(['xtail', 'C:/Users/Lenovo/Desktop/temp/x.log', "-ir", 'ung', 'alone', 'medanalysis'])
    # _xtail = XTail(['xtail', 'C:/Users/Lenovo/Desktop/temp/x.log', "-ir", 'ung'])
    _xtail = XTail(['xtail', 'C:/Users/Lenovo/Desktop/temp/catalina_all.log'])
    _xtail.follow()


