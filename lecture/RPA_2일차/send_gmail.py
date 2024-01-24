#지메일 계정 파일 - my_gmail_account.py
#지메일 전송 파일 - send_gmail.py

import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail #지메일 계정 모듈


def send_test_email():
    msg = make_mime_text(
        mail_to=gmail.account,
        subject="메일 송신 테스트입니다.1",
        body="안녕하세요 테스트 이메일 보냅니다."
        )
    send_gmail(msg) #메일 보내기

#메일 데이터
def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = gmail.account
    return msg

#Gmail 보내기
def send_gmail(msg):
    # Gmail 서버에 접속
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # 로그 출력(에러 파악을 위해서는 0->1)
    server.set_debuglevel(0)
    # 로그인하여 메일 발송
    server.login(gmail.account, gmail.password)
    server.send_message(msg)


if __name__ == "__main__":
    send_test_email()
    print("이메일을 전송했습니다.")