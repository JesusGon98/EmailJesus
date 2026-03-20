"""
Proveedores de email - Aplicando DIP (Dependency Inversion Principle)
Las implementaciones dependen de la abstracción (EmailProvider), no de implementaciones concretas.
"""
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from interfaces import EmailProvider


class GmailProvider(EmailProvider):
    """
    Proveedor de email para Gmail.
    Cumple con SRP: su única responsabilidad es enviar emails a través de Gmail SMTP.
    Cumple con DIP: implementa la interfaz EmailProvider.
    """
    
    def __init__(self, user: str, password: str, smtp_host: str = "smtp.gmail.com", smtp_port: int = 587):
        """
        Args:
            user: Usuario de Gmail
            password: Contraseña de aplicación de Gmail
            smtp_host: Host del servidor SMTP de Gmail
            smtp_port: Puerto del servidor SMTP de Gmail
        """
        self.user = user
        self.password = password
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
    
    def send_email(self, from_address: str, to_address: str, subject: str, body: str, is_html: bool = False) -> bool:
        """
        Envía un email usando Gmail SMTP.
        
        Args:
            from_address: Dirección del remitente
            to_address: Dirección del destinatario
            subject: Asunto del correo
            body: Cuerpo del correo
            is_html: Si es True, el cuerpo es HTML; si es False, es texto plano
            
        Returns:
            True si el envío fue exitoso, False en caso contrario
        """
        try:
            # Construcción del mensaje
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            # Codificar el asunto con UTF-8 para soportar caracteres especiales
            msg['Subject'] = Header(subject, 'utf-8')
            
            # Adjuntar el cuerpo según el tipo con encoding UTF-8
            content_type = 'html' if is_html else 'plain'
            msg.attach(MIMEText(body, content_type, 'utf-8'))
            
            # Conexión y envío
            server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            server.starttls()  # Requerido por Gmail
            server.login(self.user, self.password)  # Autenticación
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()
            
            logging.info(f"Correo enviado exitosamente a {to_address}")
            return True
            
        except Exception as e:
            logging.error(f"Error al enviar correo: {e}")
            return False


class OutlookProvider(EmailProvider):
    """
    Proveedor de email para Outlook/Hotmail.
    Demuestra cómo el sistema puede soportar múltiples proveedores (DIP).
    """
    
    def __init__(self, user: str, password: str, smtp_host: str = "smtp-mail.outlook.com", smtp_port: int = 587):
        """
        Args:
            user: Usuario de Outlook
            password: Contraseña de Outlook
            smtp_host: Host del servidor SMTP de Outlook
            smtp_port: Puerto del servidor SMTP de Outlook
        """
        self.user = user
        self.password = password
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
    
    def send_email(self, from_address: str, to_address: str, subject: str, body: str, is_html: bool = False) -> bool:
        """
        Envía un email usando Outlook SMTP.
        
        Args:
            from_address: Dirección del remitente
            to_address: Dirección del destinatario
            subject: Asunto del correo
            body: Cuerpo del correo
            is_html: Si es True, el cuerpo es HTML; si es False, es texto plano
            
        Returns:
            True si el envío fue exitoso, False en caso contrario
        """
        try:
            # Construcción del mensaje
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            # Codificar el asunto con UTF-8 para soportar caracteres especiales
            msg['Subject'] = Header(subject, 'utf-8')
            
            # Adjuntar el cuerpo según el tipo con encoding UTF-8
            content_type = 'html' if is_html else 'plain'
            msg.attach(MIMEText(body, content_type, 'utf-8'))
            
            # Conexión y envío
            server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            server.starttls()
            server.login(self.user, self.password)  # Autenticación
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()
            
            logging.info(f"Correo enviado exitosamente a {to_address}")
            return True
            
        except Exception as e:
            logging.error(f"Error al enviar correo: {e}")
            return False
