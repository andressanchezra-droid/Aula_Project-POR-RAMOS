from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """
    Registrar el modelo en el admin permite al equipo (y al cliente
    SST Magnus) inspeccionar y corregir datos sin escribir SQL,
    mientras el CRUD "de cara al usuario final" sigue siendo el
    construido a mano en productos/views.py.
    """
    list_display = ("nombre", "precio", "stock", "activo", "fecha_actualizacion")
    list_filter = ("activo",)
    search_fields = ("nombre",)
