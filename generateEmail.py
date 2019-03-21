import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import re

def sendmail(to, head, attachList, context):
    smtp_server = 'smtp.qq.com'
    pwd = 'rkfazvbncpsebfbi'
    port = 465
    sender = 'a19970417b@qq.com'
    msg = ''
    # receivers = ['royal_skye@outlook.com']

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("a19970417b@qq.com", 'utf-8')
    message['To'] = Header("a19970417b@qq.com", 'utf-8')
    subject = head
    message['Subject'] = Header(subject, 'utf-8')
    # 邮件正文内容
    message.attach(MIMEText(context, 'plain', 'utf-8'))

    # 处理attachment
    for i in range(0, len(attachList)):
        # print(attachList[i])
        # filename = re.findall(r'[^\\/:*?"<>|\r\n]+$', attachList[i])
        filetype = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', attachList[i])
        # print(filename[0])
        # print(filetype[0])
        # print(tmp)

        import time
        t = time.time()
        timestamp = int(t)
        newfilename = str(timestamp) + str(i) + filetype[0]

        att1 = MIMEText(open(attachList[i], 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename=%s' % newfilename
        message.attach(att1)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(smtp_server)
        smtpObj.login(sender, pwd)
        smtpObj.sendmail(sender, to, message.as_string())
        print("邮件发送成功")
        msg = "邮件发送成功"
    except:
        try:
            # for QQ 邮箱 SSL
            smtpObj = smtplib.SMTP_SSL(smtp_server, port)
            smtpObj.login(sender, pwd)
            smtpObj.sendmail(sender, to, message.as_string())
            print("邮件发送成功")
            msg = "邮件发送成功"
        except smtplib.SMTPException:
            print("Error: 邮件发送失败，请更改设置")
            msg = "Error: 邮件发送失败，请更改设置"

    return msg