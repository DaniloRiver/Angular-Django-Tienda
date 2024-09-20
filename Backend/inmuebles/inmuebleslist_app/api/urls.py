from django.urls import path # type: ignore
# from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from inmuebleslist_app.api.views import InmuebleListAV, InmuebleDetalleAV

urlpatterns = [
    # path('list/', inmueble_list, name='inmueble-list'), con funciones
    # path('<int:pk>', inmueble_detalle, name='inmueble-detalle'),
    path('list/', InmuebleListAV.as_view(), name='inmueble-list'), #con clases
    path('<int:pk>', InmuebleDetalleAV.as_view(), name='inmueble-detalle'),
]