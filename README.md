# python some exercise
### file.py
keepalived-lvs01.conf,test.txt
其中keepalive*此文件为原有文件
test.txt文件为需要touch的文件\\
当keepalived-lvs01.conf文件里面有东西有东西更改后，keepalived-lvs02.conf文件也需要同步lvs01的文件，file.py文件就可以保存一份为keepalived-lvs02.conf的文件（在此时为test.txt），然后用rsync就可以传到lvs02机器上，备份之前的文件，吧test.txt文件更名就可以了，这样可以更方便的更改文件内容，因为文件更改不是有序的改动，所以这样更快捷.

### the same word extract----extract.py
__要求__
---
有两个文本文档，想把两个里面相同的部分提取出来写进另一个文档，这该怎么实现？！比如：
文档A：
aaa
bbb
文档B：
aaa
ccc
bbb
怎样写算法才能把“aaa”和“bbb”提取出来写进文档C中？！

---
__写法__
```fa = open('A.txt')
a = fa.readlines()
fa.close()
fb = open('B.txt')
b = fb.readlines()
fb.close()
c = [i for i in a if i in b]
fc = open('C.txt', 'w')
fc.writelines(c)
fc.close()```
其中
```c = [i for i in a if i in b] ```  等价于
```c = []
for i in a:
    if i in b:
        c.append(i)```
