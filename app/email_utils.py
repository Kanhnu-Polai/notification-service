import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_CONFIG

def send_email(to_email,subject,message):
    from_email = EMAIL_CONFIG['EMAIL']
    from_password = EMAIL_CONFIG['PASSWORD']
    smtp_server = EMAIL_CONFIG['SMTP_SERVER']
    smtp_port = EMAIL_CONFIG['SMTP_PORT']


    msg = MIMEMultipart()
    msg['From']=from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message,'plain'))

    try:
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(from_email,from_password)
        server.sendmail(from_email,to_email,msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
        return False


