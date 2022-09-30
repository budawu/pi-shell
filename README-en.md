# PI Shell - Python based command line
>CAUTION:This readme is translated from Chinese by Google Translate.Report grammar mistakes in [Issues#documentation](https://github.com/budawu/pi-shell/labels/documentation).

Read this document in other languages: [简体中文](/README.md) | English

## Latest version: v0.2
  Now the source code is object oriented!
```
C:/pythondemo/pish π echo "hello,pi shell!"
```
## run Pi-shell
```shell
python pish.py
```
## syntax
### 1.`echo`
output command. Strings are supported.
```
echo 'hello'
```
### 2.`cd`
switch directory

3. `$` operator
Execute the default shell of the system, such as cmd on Windows and $SHELL on Linux.
```
$ python pish.py
```
### 4. `runpy`
Run Python code
```
runpy import sys
```
### 5. `exit`
quit.