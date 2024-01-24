#지메일 계정 파일 - my_gmail_account.py
#지메일 전송 파일 - send_gmail.py

import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail #지메일 계정 모듈
import send_gmail 

html = """



"""

msg = send_gmail.make_mime_text(
    mail_to = gmail.account,
    subject = "HTML로 만든 이메일 입니다",
    body = html)

send_gmail.send_gmail(msg)
print("HTML로 작성한 이메일 보냈습니다.")