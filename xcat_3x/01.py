# coding=utf-8
# !/usr/bin/env python

from xcat import XCat

if __name__ == "__main__":

    # cat xxx.out -ir err -n 30 -l [
    print("################################################################################################")
    # _xcat = XCat(['xcat', 'C:/Users/Lenovo/Desktop/temp/catalina_all.log'])
    # _xcat = XCat(['xcat', 'C:/Users/Lenovo/Desktop/temp/catalina_all.log', '-n', '50', '-l', '['])
    # _xcat = XCat(['xcat', 'C:/Users/Lenovo/Desktop/temp/catalina_all.2018-11-28.log', '-n', '10', '-l', '[', '-i', 'reponse result'])
    _xcat = XCat(['xcat', 'C:/Users/Lenovo/Desktop/temp/catalina_all.2018-11-28.log', '-i', 'TangYuanServlet'])
    _xcat.follow()
