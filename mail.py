#!/usr/bin/env python
#coding:utf-8
import smtplib
from email.mime.text import MIMEText

#注意构造MIMEText对象的第一个参数是邮件的正文部分，第二个参数是MIME的sbutye，传入plain，表示纯文本，最终MIME就是‘text/plain’,最后一定要用utf-8编码保证多语言兼容性，最后通过SMTP发出去。
#msg = MIMEText('send by python……','plain','utf-8')
#下面这个正文是以html格式+软连接发送的
msg = MIMEText('<html><body><h1>Hello</h1>'+'<p>send by <a href="http://www.baidu.com">python</a></p>'+'</body></html>','html','utf-8')
msg['From'] = "1030488223@qq.com"
msg['To'] = "1030488223@qq.com"
msg["Subject"] = "python teset"

server = smtplib.SMTP_SSL('smtp.qq.com',465) #设置smtp服务器，当前使用的是qq的SSMTP服务器，参数是服务器名，端口
server.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息
server.login("1030488223@qq.com","授权码")#登录进行转发的用户和授权码
server.sendmail("1030488223@qq.com",[
                                    "871909908@qq.com",
                                    "1030488223@qq.com"
                                    ],msg.as_string())#第一个参数是发件人，第二个参数是收件人，可以是多个，所以用一个列表，第三个参数是发送的内容。
server.quit()


#注意就是smtp.qq.com这个服务器只能发送给qq邮箱，要发送给126邮箱163邮箱就要改服务器名和端口。
