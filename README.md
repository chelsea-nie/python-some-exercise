# python some exercise

keepalived-lvs01.conf,test.txt
其中keepalive*此文件为原有文件
test.txt文件为需要touch的文件

当keepalived-lvs01.conf文件里面有东西有东西更改后，keepalived-lvs02.conf文件也需要同步lvs01的文件，file.py文件就可以保存一份为keepalived-lvs02.conf的文件（在此时为test.txt），然后用rsync就可以传到lvs02机器上，备份之前的文件，吧test.txt文件更名就可以了，这样可以更方便的更改文件内容，因为文件更改不是有序的改动，所以这样更快捷.
