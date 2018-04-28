#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))


# 第一行注释是为了告诉Linux/OS X 系统，这是一个Python 可执行程序，
# Windows 系统会忽略这个注释； 

# 第二行注释是为了告诉 Python 解释器，按照UTF-8 编码读取源代码
# 否则，你在源代码中写的中文输出可能会有乱码。 