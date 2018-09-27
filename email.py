# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class EmailSender(object):
    def __init__(self):
        self.mail_host = "smtp.example.com"
        self.mail_user = "example"  # 用户名
        self.mail_pass = "example"  # 口令
        self.sender = 'example@example.com'
        self.smtp_server = smtplib.SMTP()
        self.smtp_server.connect(self.mail_host, 25) 
        self.smtp_server.login(self.mail_user, self.mail_pass)

    def message(self, subject, content, receivers):
        message = MIMEMultipart()
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = self.sender
        message['To'] = receivers
        message.attach(MIMEText(content, 'plain', 'utf-8'))

        att1 = MIMEText(open('/example/example.txt', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="example.txt"'
        message.attach(att1)
        return message

    def send_message(self, subject, content, receivers):
        message = self.message(subject, content, receivers)
        try:
            self.smtp_server.sendmail(self.sender, receivers, message.as_string())
            self.smtp_server.quit()
            return True
        except Exception as e:
            return e


if __name__ == '__main__':
    e = EmailSender()
    e.send_message(u"a", u"b", "example@example.com.cn")
