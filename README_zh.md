# vulfocus-java



[![GitHub (pre-)release](https://img.shields.io/github/release/fofapro/vulfocus-py/all.svg)](https://github.com/fofapro/vulfocus-py/releases) [![stars](https://img.shields.io/github/stars/fofapro/vulfocus-py.svg)](https://github.com/fofapro/vulfocus-py/stargazers) [![license](https://img.shields.io/github/license/fofapro/vulfocus-py.svg)](https://github.com/fofapro/vulfocus-py/blob/master/LICENSE)

[English document](https://github.com/fofapro/vulfocus-py/blob/master/README.md)

## Vulfocus API

[`Vulfocus API`](https://fofapro.github.io/vulfocus/#/VULFOCUSAPI) 是  [`Vulfocus`](http://vulfocus.io/) 为开发提供的 `RESUFul API`接口，允许开发者在自己的项目中集成 [`Vulfocus`](http://vulfocus.io)。


## Vulfocus SDK

基于 [`Vulfocus API`](https://fofapro.github.io/vulfocus/#/VULFOCUSAPI) 编写的 `Python 版 `SDK`，方便`Python开发者快速将[Vulfocus](http://vulfocus.io/) 集成到自己的项目中。


## 安装

pip install vulfocus

使用

|字段名称|描述|
| ---- | ---- |
|`username`|用户登陆 [`Vulfocus`](http://vulfocus.io/) 使用的用户名|
|`licence`|前往 [`个人中心`](http://vulfocus.fofa.so/#/profile/index) 查看 `API Key`|

### 获取镜像

#### Code

```python
from vulfocus.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxxx",licence="xxxxxx")
images = clinet.get_images()
print(images)
```

#### Response

```python
ImageEntity(image_name='vulfocus/webmin-cve_2020_35606:latest', image_vul_name='Webmin 命令执行漏洞 （CVE-2020-35606）', image_desc='Webmin是Webmin社区的一套基于Web的用于类Unix操作系统中的系统管理工具。\nWebmin 1.962版本及之前版本存在安全漏洞，该漏洞允许执行任意命令。任何被授权使用Package Updates模块的用户都可以使用根权限通过包含和的向量执行任意命令。\n账户密码：root:password')
```

### 启动

#### Code

```python
from vulfocus.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxxx",licence="xxxxx")
images = clinet.get_images()
print(clinet.start_container(images[0].image_name))
```

#### Response

```python
HostEntity(host=x.x.x.x:57581,port={'10000': '57581'})
```

### 停止

#### Code

```python
from vulfocus.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxxx",licence="xxxxx")
images = clinet.get_images()
print(clinet.stop_container(images[0].image_name))
```

#### Response

```
停止成功
```

### 删除

#### Code

```python
from vulfocus.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxxx",licence="xxxxx")
images = clinet.get_images()
print(clinet.delete_container(images[0].image_name))
```

#### Response

```
删除成功
```

## 更新日志

2021-11-29

```
Release
```