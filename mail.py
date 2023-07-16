import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from essencials import ct, get_path
from mail_info import email, senha

ct()

path = get_path()

# SMTP server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = f'{email}'
SENDER_PASSWORD = f'{senha}'

receiver_email = str(input('Type the receiver email adress:    '))
subject = 'Gerenciador Financeiro'

# Create the email message
msg = MIMEMultipart()
msg['From'] = SENDER_EMAIL
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach files to the email
file_names = [f'{path}/infos.xlsx', f'{path}/relatorio.docx']
for file_name in file_names:
    attachment = open(file_name, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=file_name)
    msg.attach(part)

# Send the email
def send_mail():
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        print('Email enviado com sucesso!')
    except Exception as e:
        print('Erro ao enviar email:', str(e))
    finally:
        server.quit()

send_mail()