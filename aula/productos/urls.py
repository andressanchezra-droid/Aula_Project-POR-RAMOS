# productos/urls.py
"""
DECISIÓN TÉCNICA:
Cada endpoint tiene un 'name=' explícito. En vez de escribir rutas
como '/productos/editar' directamente en los templates, usamos
{% url 'producto_update' pk %}. Esto desacopla el HTML de la URL real:
si mañana cambian '/productos/' por '/catalogo/productos/', no hay que
tocar ni un solo template, solo este archivo.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("productos/", views.producto_list, name="producto_list"),
    path("productos/nuevo/", views.producto_create, name="producto_create"),
    path("productos/<int:pk>/editar/", views.producto_update, name="producto_update"),
    path("productos/<int:pk>/eliminar/", views.producto_delete, name="producto_delete"),
]

# En el urls.py del proyecto (sst_magnus/urls.py) se incluye así:
#
# from django.urls import path, include
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", include("productos.urls")),
# ]
