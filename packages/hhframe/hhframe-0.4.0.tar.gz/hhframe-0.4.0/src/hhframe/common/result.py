
# -*- codeing = utf-8 -*-
# @Name：Result
# @Version：1.0.0
# @Author：立树
# @CreateTime：2025-03-30 01:41

import os
import sys
import json
import types
from .config import config
# from .decorator import once

# 结果数据
class Result():
    # 初始化
    def __init__(self, state = True, data = None, msg = "", code = 200, depth = 1):
        # self.state = state
        # self.data = data
        # self.msg = msg
        # self.code = code
        # self.depth = depth
        pass
    
    # 打印结果
    def __str__(self):
        ClassInstanceDict = {}
        for key, value in self.__dict__.items():
            if type(value) == types.MethodType:
                # ClassInstanceDict[key] = value.__name__
                # ClassInstanceDict[key] = str(type(value))
                # ClassInstanceDict[key] = str(value)
                pass
            else:
                ClassInstanceDict[key] = value
        return json.dumps(ClassInstanceDict, ensure_ascii = False, indent = 4)
    
    # 打印结果
    # type: info - 普通信息, error - 错误信息, force - 强制信息
    # @once
    def print(self, type = "force"):
        # 报错信息，始终打印
        if type == "error" or type == "force":
            print(self)
        # 普通信息，根据配置打印
        if type == "info" and config.mode == "debug":
            print(self)
        return self

    # 查看数据
    def view(self, key = "data"):
        ClassInstanceDict = self.__dict__
        method = ClassInstanceDict["method"]
        if key in ClassInstanceDict:
            value = ClassInstanceDict[key]
            print(f"[ {method} ] - 返回值中 {key} 数据如下：", )
            if type(value) == dict or type(value) == list or type(value) == tuple:
                print(json.dumps(value, ensure_ascii = False, indent = 4))
            else:
                print(value)
        else:
            print(f"[ {method} ] - 返回值中不存在 {key} 数据")
        return self
    
    # 初始化方法名信息
    def initMethod(self, depth = 1):
        module = os.path.split(sys._getframe(depth).f_code.co_filename)[-1].replace(".py", "")
        method = sys._getframe(depth).f_code.co_name
        self.method = "hhframe.{}.{}()".format(module, method)
        return self

    # 设置状态
    def setState(self, state = True):
        self.state = state
        return self
    
    # 设置数据
    def setData(self, data = None):
        self.data = data
        return self
    
    # 设置提示信息
    def setMsg(self, msg = ""):
        self.msg = msg
        return self
    
    # 设置状态码
    def setCode(self, code = 200):
        self.code = code
        return self
