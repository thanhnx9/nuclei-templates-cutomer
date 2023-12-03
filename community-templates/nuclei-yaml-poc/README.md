# nuclei-yaml-poc

## 一、简介
本仓库是本人平时编写的一些基于nuclei的自定义POC。

nuclei-yaml-poc所上传的POC是nuclei模板之外的，也是日常渗透中自己收集编写的，实用性还是比较强的。

目前仓库内容比较少，我也会不定时更新POC。也欢迎大家共同完善这个仓库的内容，且行且珍惜。🚀

编写不易，顺手点个⭐️


## 二、简单使用
这里简单介绍一下nuclei的debug模式使用。这里只用了-t、-u参数进行单一的漏洞校验。更多的用法请参考nuclei官方文档。
```
nuclei -t xxx-xxx-xxx-xxx-xxx.yaml -u https://111.111.111.111:8080 --debug
```
![image](https://cdn.jsdelivr.net/gh/hututu-tech/IMG-gongfeng@main/2022/02/09/62037a10d4bed.png)

