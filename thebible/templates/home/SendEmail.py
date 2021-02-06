import smtplib #pip 필요없음
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 메일 보내기 펑션
def SendMail(sendEmail, pswd, recvEmail, text, Subject):
    smtpName = "smtp.gmail.com" # 구글 smtp
    smtpPort = 587 # 포트

    # 여러 mime 넣기
    msg = MIMEMultipart()

    # 메일 내용
    contentPart = MIMEText(text, 'html')
    msg.attach(contentPart)

    msg['Subject'] = Subject # 메일 제목
    msg['From'] = sendEmail # 발신자
    msg['To'] = recvEmail # 수신자

    s = smtplib.SMTP(smtpName, smtpPort) # 메일 서버 연결
    s.starttls() # 보안처리
    s.login(sendEmail, pswd) # 로그인
    s.sendmail(sendEmail, recvEmail, msg.as_string()) # 메일 전송, 문자열로 변환
    s.close() # 메일 서버 연결 종료


sendEmail = 'moons@featuring.in' # 발신자
pswd = 'admin1999' # 발신자 메일 비번
recvEmail = 'jacob@featuring.in' # 수신자
# recvEmail = 'wxq9102@naver.com' # 수신자

Subject = '[이그몬]메일을 인증해 주세요! - (일단 대충 만들었어요 이거 내부처리가 따로 필요한데 어떻게 할가요)'

text = '''
        <h1>이그몬 이메일 인증 안내 드립니다.</h1>
        <h5>
            이그몬의 회원이 되신 것을 진심으로 환영합니다. <br>
            본 메일은 본인 확인을 위하여 발송되는 메일입니다.<br>
            <br>
            이메일 인증을 하지 않을 경우 사이트 이용에 제한이 있을 수 있습니다.<br>
            보다 원활한 서비스 이용을 위하여 아래 이메일 인증하기 버튼을 통해<br>
            인증을 완료해주시기 바랍니다.<br>
            <br>
            감사합니다.
        </h5>
        <a href="https://featuring.co/">
            <div style="width: 200px; height: 40px; line-height: 40px; background-color: black; color: white; text-align: center; font-size: 20px; margin: 20px auto;">이메일 인증하기</div>
        </a>
    '''

# 메일 보내기(발신자, 비번, 수신자, 내용)
SendMail(sendEmail, pswd, recvEmail, text, Subject)