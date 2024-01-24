#지메일 계정 파일 - my_gmail_account.py
#지메일 전송 파일(송신) - send_gmail.py
#지메일 이미지첨부 전송 파일 - gmail_send_file.py

import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import send_gmail
import my_gmail_account as gmail #지메일 계정 모듈

msg = MIMEMultipart()
msg["Subject"] = "[첨부]필요한 파일 압축해서 전달드려요"
msg["To"] = gmail.account
msg["From"] = gmail.account
msg["Cc"] = "abc@abc.com"

#본문 작성
txt = MIMEText("압축 파일에 구입해야할 책 이미지를 첨부하였습니다. 확인해 주세요")
msg.attach(txt)

#파일 첨부
zip_part = MIMEBase("application", "zip")
with open("file_img.zip", "rb") as fp:
    zip_part.set_payload(fp.read())

encoders.encode_base64(zip_part)
zip_part.add_header("Content-Disposition", "attachment", filename="imagezip.zip")
msg.attach(zip_part)

#메일 송신
send_gmail.send_gmail(msg)
print("zip파일을 첨부한 이메일이 전송 되었습니다.")


