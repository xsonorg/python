# coding=utf-8
# !/usr/bin/env python

import sys
import re

####################################################################################


class XCat:

    def __init__(self, args):
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
        # 默认显示的行数
        self.lineCount = 20
        # 当前读取的行数
        self.lineCurrent = 0

    def _analysis(self):
        try:
            # 文件路径
            self.file_name = self.args[1]

            # 处理关键字标记和关键字
            idx = 2
            self._analysisArgGroup(idx)

            if 0 == len(self.kwList):
                self.kwList = None
                return

            if 1 == len(self.kwList):
                self.kw = self.kwList[0]
                self.kwList = None

        except Exception as e:
            print('参数错误: ' + str(e))
            sys.exit()

    # 分析每一个参数组
    def _analysisArgGroup(self, idx):
        while idx < len(self.args):
            val = self.args[idx]
            if '-n' == val:
                idx = self._parseLineCount(idx)
            elif '-l' == val:
                idx = self._parseLineMarker(idx)
            elif '-' == val[0]:
                idx = self._parseMode(idx)
            else:
                idx = self._parseKw(idx)

    # 分析最大行数
    def _parseLineCount(self, idx):
        if idx + 1 >= len(self.args):
            raise Exception("-n 参数错误.")
        self.lineCount = int(self.args[idx + 1])
        return idx + 2

    # 分析行标记
    def _parseLineMarker(self, idx):
        if idx + 1 >= len(self.args):
            raise Exception("-l 参数错误.")
        val = self.args[idx + 1]
        if '"' == val[0] or "'" == val[0]:
            val = val[1:-1]
        self.lineMarker = val
        return idx + 2

    # 分析匹配模式
    def _parseMode(self, idx):
        val = self.args[idx]
        for i in val:
            if 'i' == i:
                self.mode_i = True
                self.mode_r = True
            if 'r' == i:
                self.mode_r = True
            if 'o' == i:
                self.relation = 2
        return idx + 1

    # 分析搜索的关键字
    def _parseKw(self, idx):
        val = self.args[idx]
        if '"' == val[0] or "'" == val[0]:
            val = val[1:-1]
        self.kwList.append(val)
        return idx + 1

    def follow(self):
        self._analysis()
        try:
            with open(self.file_name, encoding='utf-8') as f:
                f.seek(0, 0)
                while self.lineCurrent < self.lineCount:
                    line = f.readline()
                    if line:
                        self._callback(line)
                    else:
                        break
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print('打开文件失败:' + self.file_name)
            print(e)

    def _callback(self, line):
        if (self.kw is None) and (self.kwList is None):
            sys.stdout.write(line)
            self.lineCurrent = self.lineCurrent + 1
            return

        isStandardLog = line.startswith(self.lineMarker)

        if isStandardLog:               # 标准日志
            _match = self._matchLine(line)
            if not _match:
                self.lineExt = False
                return
            self.lineExt = True
            sys.stdout.write(line)
            self.lineCurrent = self.lineCurrent + 1
        elif self.lineExt:              # 扩展日志
            sys.stdout.write(line)

    def _matchLine(self, line):
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

    _xcat = XCat(sys.argv)
    _xcat.follow()
