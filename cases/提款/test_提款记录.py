# coding=utf-8 

from ddt import ddt, data
import unittest
import json
from common.check import Check
from common.readConfig import confParam
from common.operToken import read_token
from common.readYaml import operYaml
from getRootPath import root_dir
from common.writeLog import writeLog
import os
from common.send import sendRequest


@ddt
class test_提款记录(unittest.TestCase):
    yamlPath = ['提款', '提款记录.yaml']
    yaml_path = os.path.join(root_dir, "yamlCase")
    for dir in yamlPath:
        yaml_path = os.path.join(yaml_path, dir)
    oper_yaml = operYaml(yaml_path)
    case_list,method,uri = oper_yaml.caseList()



    # 跳过说明
    reason = confParam("skip_reason")

    @classmethod
    def setUpClass(cls):

        # 拼接接口地址
        cls.url = confParam("hostName") + cls.uri
        cls.client = sendRequest()

        # 请求信息头
        #cls.headers = {"Cookie": read_token()["cookie"], "Content-Type": "application/json;charset=UTF-8"}

    # case_list传进去做数据驱动
    @data(*case_list)
    def test_提款记录(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            data = caseInfo["data"]
            check = caseInfo["check"]
            self.__dict__['_testMethodDoc'] = caseName

        # 发送请求
        response = self.client.sendRequest(self.method, self.url, data)

        # 接口返回文本信息
        text = response.text

        # 把文本信息转化为字典格式
        text_dict = json.loads(text)

        # 写日志
        writeLog(caseName, self.url, data, check, text_dict)

        # 断言
        Check().check(check, text_dict)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
