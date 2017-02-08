#!/usr/bin/env python
#coding:utf-8

import sys

t=open("13.xls","w+")
file="1486524222.xls"
f = open(file, 'rb')
lines = f.readlines()
for line in lines:
    line = line.decode('gb2312').encode('utf8')
    print >> t,line
