"""
Servicio de Email - Aplicando todos los principios SOLID
Esta clase coordina las diferentes responsabilidades sin violar SRP, DIP, OCP, LSP, ISP.
"""
import logging
from interfaces import EmailProvider, MessageFormatter, EmailValidator


class EmailService:
    """
    Servicio de email que coordina validación, formateo y envío.
    Cumple con SRP: su única responsabilidad es orquestar el proceso de envío.
    Cumple con DIP: depende de abstracciones (interfaces), no de implementaciones concretas.
    """
    
    def __init__(
        self,
        email_provider: EmailProvider,
        validator: EmailValidator,
        formatter: MessageFormatter
    ):
        """
        Args:
            email_provider: Proveedor de email (Gmail, Outlook, etc.) - DIP
            validator: Validador de emails - SRP
            formatter: Formateador de mensajes - OCP
        """
        self.email_provider = email_provider
        self.validator = validator
        self.formatter = formatter
    
    def send_notification(
        self,
        from_address: str,
        to_address: str,
        subject: str,
        body: str,
        use_html: bool = False
    ) -> bool:
        """
        Envía una notificación por email.
        
        Args:
            from_address: Dirección del remitente
            to_address: Dirección del destinatario
            subject: Asunto del correo
            body: Cuerpo del correo (texto plano)
            use_html: Si es True, usa el formateador HTML; si es False, texto plano
            
        Returns:
            True si el envío fue exitoso, False en caso contrario
        """
        # 1. Validación (SRP: responsabilidad separada)
        if not self.validator.validate(to_address):
            logging.error(f"Dirección de correo inválida: {to_address}")
            return False
        
        if not self.validator.validate(from_address):
            logging.error(f"Dirección de correo del remitente inválida: {from_address}")
            return False
        
        # 2. Formateo (OCP: extensible sin modificar)
        formatted_body = self.formatter.format(body)
        
        # 3. Envío (DIP: usa la abstracción, no la implementación)
        return self.email_provider.send_email(
            from_address=from_address,
            to_address=to_address,
            subject=subject,
            body=formatted_body,
            is_html=use_html
        )
