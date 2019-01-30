# coding=utf-8
# !/usr/bin/env python

import sys
import time
import re

####################################################################################


class XTail:

    def __init__(self, args):
        # print args
        if len(args) < 2:
            print('缺少参数')
            sys.exit()
        self.args = args
        # 关键字
        self.kw = None
        # 多个关键字
        self.kwList = []
        # 忽略大小写
        self.mode_i = False
        # 支持正则
        self.mode_r = False
        # 行标记
        self.lineMarker = '['
        # 扩展行
        self.lineExt = False
        # 关键字关系 1:AND(&&) 2:OR(||)
        self.relation = 1

    def __analysis(self):
        try:
            # 文件路径
            self.file_name = self.args[1]

            # xtail cx.out -gx fdafds sdfdsfdsf -f [
            # xtail cx.out -gx fdafds -f [

            # if len(self.args) > 2:
            #    val = self.args[2]
            #    if '-' == val[0]:
            #        self.__analysisMode(val)
            #    else:
            #        self.__analysisKw(val)
            #
            #    if len(self.args) > 3:
            #        val = self.args[3]
            #        self.__analysisKw(val)

            # xtail cx.out -gx fdafds sdfdsfdsf -f [

            # 处理关键字标记和关键字
            idx = 2
            if idx < len(self.args):
                val = self.args[idx]
                if '-' == val[0]:
                    self.__analysisMode(val)
                else:
                    self.__analysisKw(val)

            # 处理关键字和日志行标记
            idx = 3
            while idx < len(self.args):
                val = self.args[idx]
                idx = idx + 1
                if '-f' == val:
                    break
                else:
                    self.__analysisKw(val)

            # 处理行标识
            if idx < len(self.args):
                self.__analysisMarker(val)

            if 0 == len(self.kwList):
                self.kwList = None
                return

            if 1 == len(self.kwList):
                self.kw = self.kwList[0]
                self.kwList = None

        except Exception, e:
            print '参数错误.'

    def __analysisMode(self, val):
        for i in val:
            if 'i' == i:
                self.mode_i = True
                self.mode_r = True
            if 'r' == i:
                self.mode_r = True
            if 'o' == i:
                self.relation = 2

    def __analysisKw(self, val):
        _val = val
        if '"' == val[0] or "'" == val[0]:
            _val = _val[1:-1]

        # if self.mode_r:
        #    self.kw = _val
        # else:
        #    self.kw = _val
        self.kwList.append(_val)

    def __analysisMarker(self, val):
        _val = val
        if '"' == val[0] or "'" == val[0]:
            _val = _val[1:-1]

        self.lineMarker = _val

    def follow(self):
        self.__analysis()
        try:
            with open(self.file_name) as f:
                f.seek(0, 2)
                while True:
                    # f.tell()
                    line = f.readline()
                    if line:
                        self.callback(line)
                    else:
                        time.sleep(1)
        except KeyboardInterrupt:
            pass
        except Exception, e:
            print '打开文件失败:' + self.file_name
            print e

    def callback(self, line):
        if (self.kw is None) and (self.kwList is None):
            sys.stdout.write(line)
            return

        isStandardLog = line.startswith(self.lineMarker)

        if isStandardLog:               # 标准日志
            _match = self.matchLine(line)
            if not _match:
                self.lineExt = False
                return
            self.lineExt = True
            sys.stdout.write(line)
        elif self.lineExt:              # 扩展日志
            sys.stdout.write(line)


    def matchLine(self, line):
        if self.kw is not None:
            if self.mode_r:
                return re.search(self.kw, line, re.IGNORECASE) is not None
            else:
                return line.find(self.kw) > -1

        if self.kwList is not None:
            _match = False
            if 1 == self.relation:          # AND
                for _kw in self.kwList:
                    if self.mode_r:
                        _match = re.search(_kw, line, re.IGNORECASE) is not None
                    else:
                        _match = line.find(_kw) > -1
                    if not _match:
                        return _match

            else:                           # OR
                for _kw in self.kwList:
                    if self.mode_r:
                        _match = re.search(_kw, line, re.IGNORECASE) is not None
                    else:
                        _match = line.find(_kw) > -1
                    if _match:
                        return _match

            return _match

####################################################################################


if __name__ == "__main__":

    _xtail = XTail(sys.argv)
    _xtail.follow()
