import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Información del remitente y destinatarios
remitente = 'iniconavarro@gmail.com'
destinatarios = ['juanbarbosa@foodology.com.co', 'juandavidgomez@foodology.com.co']
contrasena = 'mi contraseña va acá'

# Crear el objeto de mensaje
mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['To'] = ', '.join(destinatarios)
mensaje['Subject'] = 'Tarea completada'

# Cuerpo del mensaje
cuerpo_mensaje = '¡Hola! He completado la tarea. Aquí está el enlace al repositorio:https://github.com/iNicoNavarro/PruebaFoodology.git'
mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

# Configuración del servidor SMTP
servidor_smtp = 'smtp.gmail.com'
puerto_smtp = 587

# Iniciar sesión en el servidor SMTP
conexion_smtp = smtplib.SMTP(servidor_smtp, puerto_smtp)
conexion_smtp.starttls()
conexion_smtp.login(remitente, contrasena)

# Enviar el mensaje a los destinatarios
conexion_smtp.send_message(mensaje)
print('Correo electrónico enviado exitosamente a los destinatarios.')

# Cerrar la conexión SMTP
conexion_smtp.quit()
