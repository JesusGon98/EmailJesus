# 📧 Refactorización SOLID - Email Service

Este repositorio contiene un **servicio de email refactorizado** que cumple con los **5 principios SOLID**, transformando un código monolítico en una arquitectura modular, extensible y mantenible.

---

## ✅ Estado del Proyecto

**Refactorización completada** - El código ahora cumple con todos los principios SOLID.

---

## 📁 Estructura del Proyecto

```
EmailJesus/
├── .gitignore              # Ignora config.py y archivos sensibles
├── config.py               # Credenciales (⚠️ NO se sube a git)
├── config.example.py       # Plantilla de configuración
├── main.py                 # Punto de entrada con ejemplos
├── interfaces.py          # Definición de interfaces (DIP)
├── validators.py          # Validadores de email (SRP)
├── formatters.py          # Formateadores de mensajes (OCP)
├── providers.py           # Proveedores de email (DIP)
├── email_service.py       # Servicio principal (orquestador)
├── SOLID_REFACTORING.md   # Documentación detallada de la refactorización
└── README.md              # Este archivo
```

---

## 🚀 Inicio Rápido

### 1. Configurar credenciales

Copia `config.example.py` a `config.py` y completa tus credenciales:

```python
GMAIL_USER = "tu_usuario@gmail.com"
GMAIL_APP_PASSWORD = "tu_contraseña_de_aplicacion"  # Contraseña de aplicación de Google
TEST_RECIPIENT = "destinatario@gmail.com"
```

**⚠️ Importante:** El archivo `config.py` está en `.gitignore` para proteger tus credenciales.

### 2. Ejecutar el ejemplo

```bash
python main.py
```

---

## 🎯 Principios SOLID Aplicados

### S — Single Responsibility Principle (SRP)

**Separación de responsabilidades:**
- `BasicEmailValidator`: Solo valida emails
- `PlainTextFormatter`, `HTMLFormatter`: Solo formatean mensajes
- `GmailProvider`, `OutlookProvider`: Solo envían emails
- `EmailService`: Solo orquesta el proceso

### O — Open/Closed Principle (OCP)

**Extensible sin modificar código existente:**
- Nuevos formatos: Crea una clase que implemente `MessageFormatter`
- Nuevos validadores: Crea una clase que implemente `EmailValidator`

### L — Liskov Substitution Principle (LSP)

**Implementaciones intercambiables:**
- Cualquier `EmailProvider` puede usarse en `EmailService`
- Cualquier `MessageFormatter` puede usarse en `EmailService`

### I — Interface Segregation Principle (ISP)

**Interfaces específicas:**
- `EmailProvider`: Solo métodos de envío
- `MessageFormatter`: Solo métodos de formateo
- `EmailValidator`: Solo métodos de validación

### D — Dependency Inversion Principle (DIP)

**Dependencia de abstracciones:**
```python
# EmailService depende de EmailProvider (interfaz), no de GmailProvider (implementación)
class EmailService:
    def __init__(self, email_provider: EmailProvider, ...):
        self.email_provider = email_provider
```

**Cambiar de proveedor es simple:**
```python
# Gmail
provider = GmailProvider(user, password)

# Outlook (solo cambias esta línea)
provider = OutlookProvider(user, password)
```

---

## 💻 Ejemplo de Uso

```python
from providers import GmailProvider
from validators import BasicEmailValidator
from formatters import HTMLFormatter
from email_service import EmailService

# Configurar componentes
provider = GmailProvider(user="tu_email@gmail.com", password="tu_app_password")
validator = BasicEmailValidator()
formatter = HTMLFormatter(title="Notificación", color="#4285F4")

# Crear servicio
service = EmailService(provider, validator, formatter)

# Enviar email
service.send_notification(
    from_address="tu_email@gmail.com",
    to_address="destinatario@gmail.com",
    subject="Asunto del correo",
    body="Cuerpo del mensaje",
    use_html=True
)
```

---

## 🔄 Cambiar de Proveedor (DIP en Acción)

**Antes (violando SOLID):** Tenías que reescribir media clase para cambiar de Gmail a Outlook.

**Ahora (cumpliendo SOLID):** Solo cambias una línea:

```python
# De Gmail a Outlook
provider = OutlookProvider(user, password)  # Solo esta línea cambia
```

---

## 📚 Documentación

Para más detalles sobre la refactorización, consulta:
- `SOLID_REFACTORING.md` - Documentación completa de los principios SOLID aplicados

---

## 🔐 Seguridad

- ✅ `config.py` está en `.gitignore`
- ✅ Las credenciales no se suben al repositorio
- ✅ Usa `config.example.py` como plantilla

---

## 📝 Obtener Contraseña de Aplicación de Google

1. Entra a tu cuenta de Google (https://myaccount.google.com/)
2. Ve a la pestaña de 'Seguridad'
3. Asegúrate de tener activada la 'Verificación en dos pasos'
4. Busca 'Contraseñas de aplicaciones'
5. Crea una nueva contraseña de aplicación
6. Copia el código de 16 caracteres y úsalo en `config.py`

---

## 💡 Tip de Mike

> "Recuerden que si para cambiar de Gmail a Outlook tienen que borrar y reescribir media clase, entonces no están aplicando SOLID. ¡Hagan que su código sea intercambiable!"

**✅ Con esta refactorización:** Cambiar de Gmail a Outlook es cambiar una línea de código.

---

## 📊 Beneficios de la Refactorización

1. ✅ **Testabilidad:** Cada componente puede probarse de forma aislada
2. ✅ **Mantenibilidad:** Cambios localizados no afectan otras partes
3. ✅ **Extensibilidad:** Nuevas funcionalidades sin modificar código existente
4. ✅ **Flexibilidad:** Intercambio de componentes sin reescribir código
5. ✅ **Legibilidad:** Código más claro y fácil de entender

---

## 🧪 Pruebas

Ejecuta `main.py` para ver ejemplos de uso:

```bash
python main.py
```

El script incluye:
- Ejemplo con Gmail y formato HTML
- Ejemplo con Gmail y texto plano
- Ejemplo de cambio a Outlook (comentado)

---

## 📄 Licencia

Este proyecto es parte de un ejercicio educativo sobre principios SOLID.
