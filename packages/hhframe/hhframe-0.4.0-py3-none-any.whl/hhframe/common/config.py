
# -*- codeing = utf-8 -*-
# @Name：Config
# @Version：1.0.0
# @Author：立树
# @CreateTime：2025-04-02 13:50

import json

class Config():
    # 初始化
    def __init__(self):
        self.name = "hhframe"
        self.version = "0.4.0"
        self.author = "立树"
        self.mode = "run"
        # self.mode = "debug"

    # 打印结果
    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii = False, indent = 4)

config = Config()
