import os
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders'''
import imaplib
import email

'''smtp_server = "smtp.gmail.com"
smtp_port = 587
email_usuario = os.environ["SMTP_EMAIL"]
email_password = os.environ["SMTP_PASSWORD"]

#Escritura en archivos con uso de correo


cuerpo_html ="""
<html>
    <body>
        <h1>Hola, desde Python</h1>
    </body>
</html>
"""

#mensaje = MIMEText("Este es un correo enviado desde Python")
#mensaje = MIMEMultipart()
#mensaje.attach(MIMEText(cuerpo_html,'html'))
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email_usuario, email_password)
mensaje = MIMEMultipart()
archivo = 'reporte.pdf'
adjunto = MIMEBase('application', 'octet-stream')
with open(archivo, 'wb') as f:
    adjunto.set_payload(f.read())
encoders.encode_base64(adjunto)
adjunto.add_header('Content-Disposition', f'attachment; filedname={archivo}')
mensaje.attach(adjunto)
mensaje["From"] = email_usuario
mensaje["To"] = "SMTP_EMAIL"
mensaje["Subject"] = "Correo automático con Python"

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(email_usuario, email_password)
    server.send_message(mensaje)
server.sendmail(email_usuario, 'xplain1819@gmail.com', mensaje.as_string())

print("Correo enviado con éxito")'''

#Leectura de archivos con uso de correos electronicos
imap_server = 'smtp.gmail.com'
imap_usuario = 'SMTP_EMAIL' #Esto es para agregar el correo a utilizar y su PW
imap_password = 'SMTP_PASSWORD'

mail = imaplib.IMAP4_SSL(imap_server)
mail.login(imap_usuario, imap_password)
print(mail.list())
mail.select('inbox')
status, correos = mail.search(None, 'UNSEEN')
print(correos[0].split())

correo_id = correos[0].split()[0]
status, datos = mail.fetch(correo_id, '(RFC63037)')
mensaje = email.message_from_bytes(datos[0][1])
print(mensaje['Subject'])
print(mensaje['From'])

if mensaje.is_multipart():
    for parte in mensaje.walk():
        if parte.get_content_type() == 'text/plain':
            print(parte.get_payload(decode=True).decode())

for parte in mensaje.walk():
    if parte.get_content_maintype() == 'multipart':
        continue
    if parte.get('Content-Disposition') is None:
        continue
    nombre_archivo = parte.get_filename()
    if nombre_archivo:
        ruta = os.path.join('descargas', nombre_archivo)
        with open(ruta, 'wb') as f:
            f.write(parte.get_payload(decode=True))
        print(f"Archivo guardado_{ruta}")