import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv
load_dotenv()



email_password = os.getenv("PASSWORD")
email_enviador = "Chikiboon2015@gmail.com"
email_recividor = "SantoGmz2015@gmail.com"

asunto = "prueba 3"
cuerpo = "este es el detalle"


em = EmailMessage()

em["from"] = email_enviador
em["to"] = email_recividor
em["Subject"] = asunto

em.set_content(cuerpo)

context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com',465,context) as smtp:
    smtp.login(email_enviador,email_password)
    smtp.sendmail(email_enviador, email_recividor, em.as_string())

    
    