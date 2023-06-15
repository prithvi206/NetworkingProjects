import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',25)

server.ehlo()

server.login("YOUR EMAIL","PASSWORD GOES HERE")

msg = MIMEMultipart()
msg['From'] = 'Prithvi'
msg['To'] = "testmails@spam1.de"
msg["Subject"] = "Just A Test"

with open('message.text','r') as f:
    message = f.read()

msg.attach(MIMEText(message,"plain"))

filename = 'working.png'
attachment = open(filename,'rb')
p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={filename}')
msg.attach(p)
text = msg.as_string
server.send('mailtesting@gmail.com','testmail@spam1.de',text)