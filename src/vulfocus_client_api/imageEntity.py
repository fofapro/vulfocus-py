#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 10:51
# @Author : x98zy


class ImageEntity:
    def __init__(self):
        self.imageName = None
        self.imageVulName = None
        self.imageDesc = None

    def get_image_name(self):
        return self.imageName

    def get_image_vul_name(self):
        return self.imageVulName

    def get_image_desc(self):
        return self.imageDesc

    def set_image_name(self, image_name):
        self.imageName = image_name

    def set_image_vul_name(self, image_vul_name):
        self.imageVulName = image_vul_name

    def set_image_desc(self, image_desc):
        self.imageDesc = image_desc

    def __str__(self):
        return "ImageEntity(image_name={name},image_vul_name={vul_name}," "image_desc={image_desc})".format(
            name=self.imageName,vul_name=self.imageVulName,image_desc=self.imageDesc)