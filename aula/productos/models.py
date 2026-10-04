# productos/models.py
"""
Modelo de datos para la entidad Producto.

DECISIÓN TÉCNICA:
Usamos el ORM de Django (en vez de SQL crudo) porque:
1. Nos protege automáticamente de inyección SQL (parametriza cada query).
2. Desacopla el código Python de un motor de base de datos específico
   (hoy SQLite en desarrollo, mañana PostgreSQL en producción sin
   reescribir nada de esta clase).
3. Genera y versiona el esquema de la BD mediante migraciones,
   lo cual es clave para trabajar en equipo sin pisarse cambios.
"""

from django.db import models
from django.core.validators import MinValueValidator


class Producto(models.Model):
    """
    Representa un producto del catálogo de SST Magnus.

    Cada campo declara explícitamente sus restricciones (max_length,
    validadores, valores por defecto) porque esas reglas de negocio
    deben vivir en el modelo, no dispersas en las vistas. Así, sin
    importar desde dónde se cree un Producto (vista, shell, script de
    carga masiva, API futura), la integridad de los datos está
    garantizada en un solo lugar.
    """

    nombre = models.CharField(
        max_length=150,
        help_text="Nombre comercial del producto, visible para el cliente."
    )
    descripcion = models.TextField(
        blank=True,
        help_text="Detalle técnico o comercial del producto (opcional)."
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Usamos DecimalField y no FloatField para evitar "
                   "errores de redondeo en operaciones de dinero."
    )
    stock = models.PositiveIntegerField(
        default=0,
        help_text="PositiveIntegerField impide guardar cantidades negativas "
                   "a nivel de base de datos, no solo de formulario."
    )
    activo = models.BooleanField(
        default=True,
        help_text="Borrado lógico: permite 'ocultar' un producto sin "
                   "perder su historial (ver nota en views.py)."
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-fecha_creacion"]  # Los más recientes primero
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        # __str__ define cómo se representa el objeto en el admin,
        # en el shell y en logs de error: siempre legible para humanos.
        return f"{self.nombre} (${self.precio})"


# NOTA PARA EL EQUIPO:
# El modelo "Servicio" se construye de forma análoga, cambiando
# 'stock' por algo como 'duracion_horas' o 'tipo_servicio'. La lógica
# de vistas, urls y templates que ven a continuación es 100% reutilizable
# cambiando "Producto" por "Servicio".
