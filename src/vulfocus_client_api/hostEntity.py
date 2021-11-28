#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 10:51
# @Author : x98zy


class HostEntity:

    def __init__(self):
        self.host = None
        self.port = None

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def set_host(self, host):
        self.host = host

    def set_port(self, port):
        self.port = port

    def __str__(self):
        return "HostEntity(host={host},port={port})".format(
            host=self.host,
            port=self.port
        )