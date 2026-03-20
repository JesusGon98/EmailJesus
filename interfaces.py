"""
Interfaces para aplicar el principio de Inversión de Dependencias (DIP).
Define contratos que las implementaciones deben cumplir.
"""
from abc import ABC, abstractmethod


class EmailProvider(ABC):
    """
    Interfaz para proveedores de email (Gmail, Outlook, etc.)
    Permite cambiar de proveedor sin modificar el código que lo usa.
    """
    
    @abstractmethod
    def send_email(self, from_address: str, to_address: str, subject: str, body: str, is_html: bool = False) -> bool:
        """
        Envía un email usando el proveedor configurado.
        
        Args:
            from_address: Dirección del remitente
            to_address: Dirección del destinatario
            subject: Asunto del correo
            body: Cuerpo del correo
            is_html: Si es True, el cuerpo es HTML; si es False, es texto plano
            
        Returns:
            True si el envío fue exitoso, False en caso contrario
        """
        pass


class MessageFormatter(ABC):
    """
    Interfaz para formateadores de mensajes.
    Permite extender el sistema con nuevos formatos sin modificar código existente (OCP).
    """
    
    @abstractmethod
    def format(self, body: str) -> str:
        """
        Formatea el cuerpo del mensaje.
        
        Args:
            body: Contenido del mensaje en texto plano
            
        Returns:
            Mensaje formateado según el tipo de formateador
        """
        pass


class EmailValidator(ABC):
    """
    Interfaz para validadores de email.
    Permite diferentes estrategias de validación.
    """
    
    @abstractmethod
    def validate(self, email: str) -> bool:
        """
        Valida una dirección de email.
        
        Args:
            email: Dirección de email a validar
            
        Returns:
            True si la dirección es válida, False en caso contrario
        """
        pass
