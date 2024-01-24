#지메일 계정 파일 - my_gmail_account.py
#지메일 전송 파일(송신) - send_gmail.py
#지메일 이미지첨부 전송 파일 - gmail_send_file.py

import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import send_gmail
import my_gmail_account as gmail #지메일 계정 모듈

msg = MIMEMultipart()
msg["Subject"] = "[첨부]구입할 책 사진 첨부합니다"
msg["To"] = gmail.account
msg["From"] = gmail.account
msg["Cc"] = "abc@abc.com"

#본문 작성
txt = MIMEText("구입해야할 책 이미지를 첨부하였습니다. 확인해 주세요")
msg.attach(txt)

#이미지 첨부
with open("aladin_img_1.jpg", "rb") as fp:
    img = MIMEImage(fp.read())
    msg.attach(img)

#메일 송신
send_gmail.send_gmail(msg)
print("사진 첨부한 이메일이 전송 되었습니다.")


