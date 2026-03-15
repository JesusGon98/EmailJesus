import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)

class EmailManager:
    """
    Esta clase viola múltiples principios SOLID (SRP, OCP, DIP).
    Configurada para usar el servidor SMTP de Google.
    """

    def __init__(self, user, app_password):
        # Configuración fija para Gmail
        self.host = "smtp.gmail.com"
        self.port = 587
        self.user = user
        self.password = app_password

    def send_notification(self, recipient, subject, body, format_type="text"):
        # VIOLACIÓN DE SRP: Valida, formatea, envía y registra logs en un solo método.
        
        # 1. Validación
        if "@" not in recipient:
            logging.error(f"Dirección de correo inválida: {recipient}")
            return False

        # 2. Formateo del mensaje (Lógica de presentación mezclada)
        msg = MIMEMultipart()
        msg['From'] = self.user
        msg['To'] = recipient
        msg['Subject'] = subject

        if format_type == "text":
            msg.attach(MIMEText(body, 'plain'))
        elif format_type == "html":
            # VIOLACIÓN DE OCP: Difícil de extender a otros formatos sin modificar la clase.
            html_body = f"<html><body><h2 style='color: #4285F4;'>Notificación Google SMTP</h2><p>{body}</p></body></html>"
            msg.attach(MIMEText(html_body, 'html'))
        else:
            logging.error("Formato no soportado")
            return False

        # 3. Envío SMTP (Dependencia directa de la implementación smtplib)
        try:
            # Conexión al servidor de Google
            server = smtplib.SMTP(self.host, self.port)
            server.starttls()  # Requerido por Google
            server.login(self.user, self.password)
            server.sendmail(self.user, recipient, msg.as_string())
            server.quit()
            
            # 4. Registro (Logging acoplado)
            logging.info(f"Correo enviado exitosamente a {recipient}")
            return True
        except Exception as e:
            logging.error(f"Error al enviar correo: {e}")
            return False

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # RECUERDA: No uses tu contraseña normal de Gmail aquí.
    # Usa la 'Contraseña de Aplicación' generada en tu cuenta de Google.
    MI_CORREO = "tu_usuario@gmail.com"
    MI_APP_PASSWORD = "abcd efgh ijkl mnop" 

    notifier = EmailManager(MI_CORREO, MI_APP_PASSWORD)
    
    # Intento de envío de prueba
    notifier.send_notification(
        recipient="alumno_prueba@gmail.com",
        subject="Ejercicio de Programación SOLID",
        body="Si recibes esto, la conexión con Google SMTP funciona. Ahora refactoriza este código.",
        format_type="html"
    )

"""
================================================================================
GUÍA PARA OBTENER LA CONTRASEÑA DE APLICACIÓN DE GOOGLE:
================================================================================
Google ya no permite el uso de 'Aplicaciones menos seguras' con la contraseña 
normal de tu cuenta. Debes seguir estos pasos:

1. Entra a tu cuenta de Google (https://myaccount.google.com/).
2. Ve a la pestaña de 'Seguridad' en el menú de la izquierda.
3. Asegúrate de tener activada la 'Verificación en dos pasos'. Es obligatoria.
4. En el buscador de la parte superior de la cuenta, escribe 'Contraseñas de aplicaciones' 
   o búscala en la sección de 'Cómo inicias sesión en Google'.
5. Ponle un nombre a la aplicación (ejemplo: 'Python SMTP Script').
6. Haz clic en 'Crear'. Google te mostrará un código de 16 caracteres en un cuadro amarillo.
7. Copia ese código (sin espacios) y úsalo como valor en la variable 'MI_APP_PASSWORD'.
================================================================================
"""
