# 📧 Ejercicio de Refactorización: Principios SOLID con SMTP

Este repositorio contiene un **script de Python** diseñado para enviar **notificaciones por correo electrónico utilizando el servidor SMTP de Gmail**.

El código base ha sido escrito **intencionalmente rompiendo los principios SOLID**. El objetivo de este ejercicio es que el alumno **identifique estas violaciones y refactorice el código hacia una arquitectura limpia, mantenible y escalable**.

---

# 🚀 Objetivos de Aprendizaje

El alumno deberá **refactorizar la clase `EmailManager`** aplicando los **5 pilares de la programación orientada a objetos**.

## S — Responsabilidad Única (SRP)

Separar las responsabilidades del sistema.

**Problema típico:**
Una sola clase hace demasiadas cosas.

**Separar en:**

- Validación de datos
- Construcción del mensaje
- Transporte del mensaje (SMTP)

**Ejemplo conceptual**

```python
class EmailValidator:
    def validate(self, email: str) -> bool:
        pass


class EmailBuilder:
    def build(self, to, subject, body):
        pass


class EmailSender:
    def send(self, message):
        pass
