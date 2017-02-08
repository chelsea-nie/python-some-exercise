#!/usr/bin/env python
#coding:utf-8

fa = open('58sn.txt')
a = fa.readlines()
fa.close()
fb = open('13.txt')
b = fb.readlines()
fb.close()
c = [i for i in a if i in b]
fc = open('xia.txt', 'w')
fc.writelines(c)
fc.close()
