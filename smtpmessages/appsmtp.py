# Asegúrate de haber instalado la biblioteca python-dotenv usando el siguiente comando:
# pip install python-dotenv

# Importar las bibliotecas necesarias
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la contraseña del correo electrónico desde las variables de entorno
password = os.getenv("PASSWORD")

# Definir la dirección de correo electrónico del remitente y del destinatario
email_sender = "Chikiboon2015@gmail.com"
email_receiver = "mr.sansan777@gmail.com"

# Definir el asunto y el cuerpo del correo electrónico
subject = "test1"
body = "este es el test2"

# Crear un objeto EmailMessage para representar el correo electrónico
em = EmailMessage()
em["From"] = email_sender
em["to"] = email_receiver
em["Subject"] = subject

# Establecer el contenido del cuerpo del correo electrónico
em.set_content(body)

# Crear un contexto SSL seguro para la conexión SMTP
context = ssl.create_default_context()

# Establecer la conexión con el servidor SMTP de Gmail utilizando SSL
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    # Iniciar sesión en la cuenta de correo electrónico del remitente
    smtp.login(email_sender, password)
    
    # Enviar el correo electrónico
    smtp.sendmail(email_sender, email_receiver, em.as_string())

