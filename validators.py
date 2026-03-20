"""
Validadores de email - Aplicando SRP (Single Responsibility Principle)
Cada clase tiene una única responsabilidad: validar direcciones de email.
"""
import re
from interfaces import EmailValidator


class BasicEmailValidator(EmailValidator):
    """
    Validador básico de email usando expresiones regulares.
    Cumple con SRP: su única responsabilidad es validar emails.
    """
    
    def __init__(self):
        # Patrón básico para validar formato de email
        self.email_pattern = re.compile(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        )
    
    def validate(self, email: str) -> bool:
        """
        Valida una dirección de email.
        
        Args:
            email: Dirección de email a validar
            
        Returns:
            True si la dirección es válida, False en caso contrario
        """
        if not email or not isinstance(email, str):
            return False
        return bool(self.email_pattern.match(email.strip()))
