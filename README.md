# crontab-manager
[![GitHub stars](https://img.shields.io/github/stars/LeonQiuM/crontab-manager.svg?style=social&label=Stars&style=plastic)](https://github.com/LeonQiuM/crontab-manager/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/LeonQiuM/crontab-manager.svg?style=social&label=Fork&style=plastic)](https://github.com/LeonQiuM/crontab-manager/fork)
[![AUR](https://img.shields.io/aur/license/yaourt.svg?style=plastic)](https://github.com/LeonQiuM/crontab-manager/blob/master/LICENSE)


*新项目正在开发当中，喜欢的大佬可以提供建议和意见，我一定会很努力的~*

## 前言
1. linux crontab统一调度管理平台
2. 在页面上点击既可以实现整个集群的定时任务的统一调度，我在`Rundeck`中看到有这样的一个模块，想自己用Django实现，只实现一个这样的功能
3. 将定时任务管理平台化、简单化、集群化


## 实现方式
1. 在linux主机上利用`crontab -u user <file>`来向某个主机的某个用户添加定时任务
2. 任务存储在数据库里面，与主机建立一定的关系

## Environment
1. Python : ![](https://img.shields.io/badge/Python-3.6.2-green.svg)
2. Django : ![](https://img.shields.io/badge/Django-1.11.5-blue.svg)
2. 其他组件请查看 : `requirements.txt`

## 安装


## API文档
[API文档地址]()
