import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import sendGmail
import myGmailAccount as gmail #지메일 계정 모듈

msg = MIMEMultipart()
msg["Subject"] = "[첨부] 사진"
msg["To"] = gmail.account
msg["From"] = gmail.account
msg["Cc"] = gmail.account

txt = MIMEText("zip 파일 첨부")
msg.attach(txt)

zip_part = MIMEBase("application", "zip")

with open("aladin.zip", "rb") as fp:
    zip_part.set_payload(fp.read())

encoders.encode_base64(zip_part)
zip_part.add_header("Content-Disposition", "attachment", filename="aladin.zip")
msg.attach(zip_part)

sendGmail.send_gmail(msg)
print("사진 첨부 한 이메일 전송 완료")