"""
Ejemplo de uso del servicio de email refactorizado según principios SOLID.
Este código demuestra cómo usar la nueva arquitectura modular y extensible.
"""
import logging
from providers import GmailProvider, OutlookProvider
from validators import BasicEmailValidator
from formatters import PlainTextFormatter, HTMLFormatter
from email_service import EmailService

# Configuración básica de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Intentar importar configuración
try:
    import config
    GMAIL_USER = config.GMAIL_USER
    GMAIL_APP_PASSWORD = config.GMAIL_APP_PASSWORD
    TEST_RECIPIENT = config.TEST_RECIPIENT
except ImportError:
    logging.warning("No se encontró config.py. Usando valores por defecto.")
    logging.warning("Crea un archivo config.py basado en config.example.py")
    GMAIL_USER = "tu_usuario@gmail.com"
    GMAIL_APP_PASSWORD = "tu_contraseña_de_aplicacion"
    TEST_RECIPIENT = "alumno_prueba@gmail.com"


def ejemplo_gmail():
    """
    Ejemplo de uso con Gmail.
    Demuestra cómo cambiar de proveedor es simple gracias a DIP.
    """
    print("\n" + "="*70)
    print("EJEMPLO 1: Envío de email usando Gmail con formato HTML")
    print("="*70)
    
    # 1. Crear el proveedor de Gmail (DIP: dependemos de la abstracción)
    gmail_provider = GmailProvider(
        user=GMAIL_USER,
        password=GMAIL_APP_PASSWORD
    )
    
    # 2. Crear el validador (SRP: responsabilidad única)
    validator = BasicEmailValidator()
    
    # 3. Crear el formateador HTML (OCP: extensible sin modificar código)
    html_formatter = HTMLFormatter(
        title="Notificación Google SMTP",
        color="#4285F4"
    )
    
    # 4. Crear el servicio de email (orquesta todo)
    email_service = EmailService(
        email_provider=gmail_provider,
        validator=validator,
        formatter=html_formatter
    )
    
    # 5. Enviar notificación
    body_mensaje = """Prueba de funcionamiento y entrega de actividad.

Datos del estudiante:
• Nombre: Jesús Ramiro González Rivas
• Matrícula: MRDX24001
• Cuatrimestre: Octavo
• Carrera: Ingeniería en Desarrollo de Software

Información de la actividad:
• Profesor: Cardona Contreras Miguel Ángel
• Materia: Patrones de Diseño
• Nombre de actividad: Refactorización SOLID - Email Service

Este correo es una prueba de funcionamiento del servicio de email refactorizado que cumple con los principios SOLID. Si recibes este mensaje, la conexión con Google SMTP funciona correctamente y el código ha sido refactorizado exitosamente."""
    
    resultado = email_service.send_notification(
        from_address=GMAIL_USER,
        to_address=TEST_RECIPIENT,
        subject="Refactorización SOLID - Email Service - Entrega de Actividad",
        body=body_mensaje,
        use_html=True
    )
    
    if resultado:
        print("✅ Correo enviado exitosamente")
    else:
        print("❌ Error al enviar correo")
    
    return resultado


def ejemplo_gmail_texto_plano():
    """
    Ejemplo de uso con Gmail y texto plano.
    Demuestra cómo cambiar de formato es simple gracias a OCP.
    """
    print("\n" + "="*70)
    print("EJEMPLO 2: Envío de email usando Gmail con texto plano")
    print("="*70)
    
    # Usar el mismo proveedor pero con formateador de texto plano
    gmail_provider = GmailProvider(
        user=GMAIL_USER,
        password=GMAIL_APP_PASSWORD
    )
    
    validator = BasicEmailValidator()
    plain_formatter = PlainTextFormatter()  # Cambio de formateador (OCP)
    
    email_service = EmailService(
        email_provider=gmail_provider,
        validator=validator,
        formatter=plain_formatter
    )
    
    body_mensaje = """Prueba de funcionamiento y entrega de actividad.

Datos del estudiante:
• Nombre: Jesús Ramiro González Rivas
• Matrícula: MRDX24001
• Cuatrimestre: Octavo
• Carrera: Ingeniería en Desarrollo de Software

Información de la actividad:
• Profesor: Cardona Contreras Miguel Ángel
• Materia: Patrones de Diseño
• Nombre de actividad: Refactorización SOLID - Email Service

Este correo es una prueba de funcionamiento del servicio de email refactorizado que cumple con los principios SOLID. Este mensaje utiliza formato de texto plano, demostrando la flexibilidad del sistema gracias al principio OCP (Open/Closed Principle)."""
    
    resultado = email_service.send_notification(
        from_address=GMAIL_USER,
        to_address=TEST_RECIPIENT,
        subject="Refactorización SOLID - Email Service - Prueba Texto Plano",
        body=body_mensaje,
        use_html=False
    )
    
    if resultado:
        print("✅ Correo enviado exitosamente")
    else:
        print("❌ Error al enviar correo")
    
    return resultado


def ejemplo_outlook():
    """
    Ejemplo de uso con Outlook.
    Demuestra cómo cambiar de Gmail a Outlook es simple gracias a DIP.
    """
    print("\n" + "="*70)
    print("EJEMPLO 3: Cambio de proveedor a Outlook (DIP en acción)")
    print("="*70)
    print("💡 Tip de Mike: Si para cambiar de Gmail a Outlook tienes que")
    print("   borrar y reescribir media clase, entonces no estás aplicando SOLID.")
    print("   ¡Haz que tu código sea intercambiable!")
    print("="*70)
    
    # Solo cambiamos el proveedor, el resto del código permanece igual (DIP)
    outlook_provider = OutlookProvider(
        user=GMAIL_USER,  # En producción, usar credenciales de Outlook
        password=GMAIL_APP_PASSWORD
    )
    
    validator = BasicEmailValidator()
    html_formatter = HTMLFormatter(title="Notificación Outlook", color="#0078D4")
    
    email_service = EmailService(
        email_provider=outlook_provider,  # Cambio de proveedor (DIP)
        validator=validator,
        formatter=html_formatter
    )
    
    body_mensaje = """Prueba de funcionamiento y entrega de actividad.

Datos del estudiante:
• Nombre: Jesús Ramiro González Rivas
• Matrícula: MRDX24001
• Cuatrimestre: Octavo
• Carrera: Ingeniería en Desarrollo de Software

Información de la actividad:
• Profesor: Cardona Contreras Miguel Ángel
• Materia: Patrones de Diseño
• Nombre de actividad: Refactorización SOLID - Email Service

Este correo fue enviado usando Outlook, demostrando el principio DIP (Dependency Inversion Principle). El código es completamente intercambiable entre proveedores de email sin necesidad de modificar la lógica de negocio."""
    
    resultado = email_service.send_notification(
        from_address=GMAIL_USER,
        to_address=TEST_RECIPIENT,
        subject="Refactorización SOLID - Email Service - Prueba Outlook (DIP)",
        body=body_mensaje,
        use_html=True
    )
    
    if resultado:
        print("✅ Correo enviado exitosamente")
    else:
        print("❌ Error al enviar correo (puede ser porque las credenciales son de Gmail)")
    
    return resultado


if __name__ == "__main__":
    print("\n" + "="*70)
    print("🐍 REFACTORIZACIÓN SOLID - Email Service")
    print("="*70)
    print("\nEste código demuestra la aplicación de los 5 principios SOLID:")
    print("  • SRP: Cada clase tiene una única responsabilidad")
    print("  • OCP: El sistema es extensible sin modificar código existente")
    print("  • LSP: Las implementaciones son intercambiables")
    print("  • ISP: Interfaces específicas y cohesivas")
    print("  • DIP: Dependemos de abstracciones, no de implementaciones")
    print("="*70)
    
    # Ejecutar ejemplos
    try:
        ejemplo_gmail()
        ejemplo_gmail_texto_plano()
        # ejemplo_outlook()  # Descomentar si tienes credenciales de Outlook
    except Exception as e:
        logging.error(f"Error en la ejecución: {e}")
        print("\n⚠️  Asegúrate de haber configurado config.py con tus credenciales")
        print("   Copia config.example.py a config.py y completa los datos")
    
    print("\n" + "="*70)
    print("📚 Para más información sobre SOLID, consulta el documento PDF")
    print("="*70)
