import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from essencials import ct, get_path
import sys

ct()

path = get_path()

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'email adress'
SENDER_PASSWORD = 'password'

receiver_email = sys.argv[1]
subject = 'Gestor Financeiro'

msg = MIMEMultipart()
msg['From'] = SENDER_EMAIL
msg['To'] = receiver_email
msg['Subject'] = subject

file_names = [f'{path}/infos.xlsx', f'{path}/relatorio.docx']
for file_name in file_names:
    attachment = open(file_name, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=file_name)
    msg.attach(part)

def send_mal():
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('Erro ao enviar o e-mail:', str(e))
    finally:
        server.quit()

send_mal()