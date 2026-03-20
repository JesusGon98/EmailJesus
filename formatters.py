"""
Formateadores de mensajes - Aplicando OCP (Open/Closed Principle)
El sistema está abierto para extensión (nuevos formatos) pero cerrado para modificación.
"""
from interfaces import MessageFormatter


class PlainTextFormatter(MessageFormatter):
    """
    Formateador para mensajes de texto plano.
    Cumple con SRP: su única responsabilidad es formatear texto plano.
    """
    
    def format(self, body: str) -> str:
        """
        Retorna el cuerpo sin modificar (texto plano).
        
        Args:
            body: Contenido del mensaje
            
        Returns:
            El mismo contenido sin modificar
        """
        return body


class HTMLFormatter(MessageFormatter):
    """
    Formateador para mensajes HTML.
    Cumple con SRP: su única responsabilidad es formatear HTML.
    Extiende el sistema sin modificar código existente (OCP).
    """
    
    def __init__(self, title: str = "Notificación", color: str = "#4285F4"):
        """
        Args:
            title: Título del mensaje HTML
            color: Color del título (hexadecimal)
        """
        self.title = title
        self.color = color
    
    def format(self, body: str) -> str:
        """
        Formatea el cuerpo como HTML.
        
        Args:
            body: Contenido del mensaje en texto plano
            
        Returns:
            Contenido formateado como HTML
        """
        return f"""
        <html>
            <body>
                <h2 style='color: {self.color};'>{self.title}</h2>
                <p>{body}</p>
            </body>
        </html>
        """


class MarkdownFormatter(MessageFormatter):
    """
    Formateador para mensajes Markdown (ejemplo de extensión).
    Demuestra cómo el sistema puede extenderse sin modificar código existente (OCP).
    """
    
    def format(self, body: str) -> str:
        """
        Convierte Markdown básico a HTML.
        
        Args:
            body: Contenido en Markdown
            
        Returns:
            Contenido convertido a HTML
        """
        # Conversión básica de Markdown a HTML
        html = body.replace('**', '<strong>').replace('**', '</strong>')
        html = html.replace('*', '<em>').replace('*', '</em>')
        return f"<html><body>{html}</body></html>"
