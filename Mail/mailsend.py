"""
Mail Send Module : Python 3.6(Simple 해짐)

gmail    smtp.gmail.com, 587(TLS는 보통 포트 587을, SSL은 465를 사용한다)
Live     smtp.live.com, 587

를 이용하여 Mail을 보낸다.

To Do...
1. 파라미터로 받을 것.
2. 다중전송을 위해 To ~를 Set로 받는 방법도 고민.
3. 환경설정 파일에서 메일정보를 읽는다.
"""
import smtplib
from email.message import EmailMessage

fromaddr = "parkhg@gmail.com"
toaddr   = "phg4u@naver.com"

msg = EmailMessage()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "[Python]메일보내기 모듈 테스트"

body = "메일 본문 "
msg.set_content(body)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "ixsrgetgjzxqgonqlmh")  # 2단계 인증인 경우 16자리 앱비밀번호 사용함
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
