
# pip install python-dotenv
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# llamar la contrasena desde el .env
password = os.getenv("PASSWORD")

email_sender = "Chikiboon2015@gmail.com"
email_receiver = "mr.sansan777@gmail.com"

# asunto y texto que enviare
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

try:
    # Establecer la conexión con el servidor SMTP de Gmail utilizando SSL
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:   
        # Iniciar sesión en la cuenta de correo electrónico del remitente
        smtp.login(email_sender, password)
        
        # Enviar el correo 
        smtp.sendmail(email_sender, email_receiver, em.as_string())
except Exception as e:
    print(f"hay un problema en {e}")

else:
    print("Se ha enviado con exito el correo.")            

