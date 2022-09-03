# PI Shell - Python based command line
CAUTION:This readme is translated from Chinese by Goggle Translate.Report grammar mistakes in issue.

read this file in other languages: [简体中文](/README.md) | English

## Latest version: 0.0.4
  * Fixed pressing enter or '\' to exit
```
C:/pythondemo/pish π echo "hello,pi shell!"
```
## run Pi-shell
```shell
python pish.py
```
## syntax
### 1.echo
output command. Strings are supported.
```
echo 'hello'
```
### 2.cd
switch directory

3. $ operator
Execute the default shell of the system, such as cmd on Windows and $SHELL on Linux.
```
$ python pish.py
```
### 4. runpy
Run Python code
```
runpy import sys
```
### 5. exit
quit.