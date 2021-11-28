#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 10:51
# @Author : x98zy


class VulfocusException(Exception):

    def __init__(self, err):
        super().__init__(err)