#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 10:52
# @Author : x98zy


import requests
import json
from vulfocus_client_api.vulfocusException import VulfocusException
from vulfocus_client_api.operationConstants import OperationConstants
from vulfocus_client_api.imageEntity import ImageEntity
from vulfocus_client_api.hostEntity import HostEntity

class VulfocusClient(object):
    def __init__(self, username, licence):
        self.username = username
        self.licence = licence
        self.url = "http://vulfocus.fofa.so/api/imgs/operation"
        self.operation = OperationConstants()

    def get_images(self):
        url = self.url
        data = {"username": self.username, "licence": self.licence}
        ret_info = requests.get(url=url, params=data)
        response_info = json.loads(ret_info.text)
        self.check_response_msg(response_info)
        image_list = []
        ret_image_list = response_info["data"]
        if ret_image_list:
            for image in ret_image_list:
                image_instance = ImageEntity()
                if "image_name" in image:
                    image_instance.set_image_name(image["image_name"])
                if "image_vul_name" in image:
                    image_instance.set_image_vul_name(image["image_vul_name"])
                if "image_desc" in image:
                    image_instance.set_image_desc(image["image_desc"])
                image_list.append(image_instance)
        return image_list


    def start_container(self, image_name):
        if not image_name:
            raise VulfocusException("镜像名称不能为空")
        url = self.url
        data = {"username": self.username, "licence": self.licence, "image_name": image_name,
                "requisition": self.operation.START}
        ret_info = requests.post(url=url, data=data)
        response_info = json.loads(ret_info.text)
        self.check_response_msg(response_info)
        hostentity = HostEntity()
        hostentity.set_host(response_info["data"]["host"])
        hostentity.set_port(json.loads(response_info["data"]["port"]))
        return hostentity


    def stop_container(self, image_name):
        if not image_name:
            raise VulfocusException("镜像名称不能为空")
        url = self.url
        data = {"username": self.username, "licence": self.licence,
                "image_name": image_name, "requisition": self.operation.STOP}
        ret_info = requests.post(url=url, data=data)
        response_info = json.loads(ret_info.text)
        self.check_response_msg(response_info)
        return response_info["msg"]

    def delete_container(self, image_name):
        if not image_name:
            raise VulfocusException("镜像名称不能为空")
        url = self.url
        data = {"username": self.username, "licence": self.licence,
                "image_name": image_name, "requisition": self.operation.DELETE}
        ret_info = requests.post(url=url, data=data)
        response_info = json.loads(ret_info.text)
        self.check_response_msg(response_info)
        return response_info["msg"]

    def check_response_msg(self, response_info):
        if "status" in response_info and response_info["status"] == 500:
            raise VulfocusException(response_info["msg"])


