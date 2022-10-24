# PI Shell-基于Python的命令行
  
Read this document in other languages:   简体中文 | [English](/README-en.md)
  
## 最新版本：v0.3.2
  * 改善了$操作符
  * 使用断言`-0`,据说可以提速

```shell
C:/pythondemo/pish π  echo "hello,pi shell!"
```

### 运行
```shell
python src/main.py
```
在powershell:
```poweershell
.\pish
```
  
## 语法
### 1.`echo`
输出指令。支持字符串。
```shell
echo 'hello'
```
### 2.`cd`
切换目录

### 3.`$`操作符
执行系统默认shell，如在Windows端为cmd，Linux端为$SHELL。
```shell
$ python pish.py
```
### 4.`runpy`
运行Python代码
```
runpy import sys
```
### 5.`exit`
退出。


   	




