# vulfocus-py

[![GitHub (pre-)release](https://img.shields.io/github/release/fofapro/vulfocus-py/all.svg)](https://github.com/fofapro/vulfocus-py/releases) [![stars](https://img.shields.io/github/stars/fofapro/vulfocus-py.svg)](https://github.com/fofapro/vulfocus-py/stargazers) [![license](https://img.shields.io/github/license/fofapro/vulfocus-py.svg)](https://github.com/fofapro/vulfocus-py/blob/master/LICENSE)

[Chinese document](https://github.com/fofapro/vulfocus-py/blob/master/README_zh.md)

## Vulfocus API

[`Vulfocus API`](https://fofapro.github.io/vulfocus/#/VULFOCUSAPI) is the `RESUFul API` interface provided by [`Vulfocus`](http://vulfocus.io/) for development, allowing Developers integrate [`Vulfocus`](http://vulfocus.io) in their own projects.

## Vulfocus SDK

The `Python` version of `SDK` written based on the [`Vulfocus API`](https://fofapro.github.io/vulfocus/#/VULFOCUSAPI) makes it easy for `Python` developers to quickly integrate [`Vulfocus`](http://vulfocus.io/)  into their projects.

## Install

pip install VulfocusSdk

## USE

|field|description|
| ---- | ---- |
|`username`|User login [`Vulfocus`](http://vulfocus.io/) userbox `username`|
|licence|Please go to the [`personal center`](http://vulfocus.fofa.so/#/profile/index) to view `API licence`|

### Pull Images

```python
from vulfocus_client_api.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxxx",licence="xxxxxx")
images = clinet.get_images()
print(images)
```

#### Response

[<vulfocus_client_api.imageEntity.ImageEntity object at 0x000002978B35DC48>, <vulfocus_client_api.imageEntity.ImageEntity object at 0x000002978B35DD08>, <vulfocus_client_api.imageEntity.ImageEntity object at 0x000002978B35DAC8>]

### Start

```python
from vulfocus_client_api.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxxxx",licence="xxxxxxx")
images = clinet.get_images()
print(clinet.start_container(images[0].get_image_name()))
```

#### Response

HostEntity(host=118.193.36.37:57581,port={'10000': '57581'})

### Stop

```python
from vulfocus_client_api.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxx",licence="xxxxx")
images = clinet.get_images()
print(clinet.stop_container(images[0].get_image_name()))
```

#### Response

停止成功

### Delete

```python
from vulfocus_client_api.vulfocusClient import VulfocusClient
clinet = VulfocusClient(username="xxx",licence="xxxxx")
images = clinet.get_images()
print(clinet.delete_container(images[0].get_image_name()))
```
#### Response

删除成功

## Update Log

2021-11-28

```
Release
```

