# vulfocus-py

[![GitHub (pre-)release](https://img.shields.io/github/release/fofapro/vulfocus-py/all.svg)](https://github.com/fofapro/vulfocus-py/releases) [![stars](https://img.shields.io/github/stars/fofapro/vulfocus-py.svg)](https://github.com/fofapro/vulfocus-py/stargazers) [![license](https://img.shields.io/github/license/fofapro/vulfocus-py.svg)](https://github.com/fofapro/vulfocus-py/blob/master/LICENSE)

[Chinese document](https://github.com/fofapro/vulfocus-py/blob/master/README_zh.md)

## Vulfocus API

[`Vulfocus API`](https://fofapro.github.io/vulfocus/#/VULFOCUSAPI) is the `RESUFul API` interface provided by [`Vulfocus`](http://vulfocus.io/) for development, allowing Developers integrate [`Vulfocus`](http://vulfocus.io) in their own projects.

## Vulfocus SDK

The `Python` version of `SDK` written based on the [`Vulfocus API`](https://fofapro.github.io/vulfocus/#/VULFOCUSAPI) makes it easy for `Python` developers to quickly integrate [`Vulfocus`](http://vulfocus.io/)  into their projects.

## Install

pip install vulfocus

## USE

|field|description|
| ---- | ---- |
|`username`|User login [`Vulfocus`](http://vulfocus.io/) userbox `username`|
|licence|Please go to the [`personal center`](http://vulfocus.fofa.so/#/profile/index) to view `API licence`|

### Pull Images

```python
from vulfocus.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxxx",licence="xxxxxx")
images = clinet.get_images()
print(images)
```

#### Response

ImageEntity(image_name='vulfocus/webmin-cve_2020_35606:latest', image_vul_name='Webmin 命令执行漏洞 （CVE-2020-35606）', image_desc='Webmin是Webmin社区的一套基于Web的用于类Unix操作系统中的系统管理工具。\nWebmin 1.962版本及之前版本存在安全漏洞，该漏洞允许执行任意命令。任何被授权使用Package Updates模块的用户都可以使用根权限通过包含和的向量执行任意命令。\n账户密码：root:password')

### Start

```python
from vulfocus.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxxx",licence="xxxxx")
images = clinet.get_images()
print(clinet.start_container(images[0].image_name))
```

#### Response

HostEntity(host=x.x.x.x:57581,port={'10000': '57581'})

### Stop

```python
from vulfocus.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxxx",licence="xxxxx")
images = clinet.get_images()
print(clinet.stop_container(images[0].image_name))
```

#### Response

停止成功

### Delete

```python
from vulfocus.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxxx",licence="xxxxx")
images = clinet.get_images()
print(clinet.delete_container(images[0].image_name))
```
#### Response

删除成功

## Update Log

2021-11-29

```
Release
```

