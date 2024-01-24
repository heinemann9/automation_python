import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import sendGmail
import myGmailAccount as gmail #지메일 계정 모듈

msg = MIMEMultipart()
msg["Subject"] = "[첨부] 사진"
msg["To"] = gmail.account
msg["From"] = gmail.account
msg["Cc"] = gmail.account

txt = MIMEText("책 이미지 첨부")
msg.attach(txt)

with open("aladin_img_1.jpg", "rb") as fp:
    img = MIMEImage(fp.read())
    img.add_header("Content-Disposition", "attachment", filename="aladin_img_1.jpg")
    msg.attach(img)
    
sendGmail.send_gmail(msg)
print("사진 첨부 한 이메일 전송 완료")