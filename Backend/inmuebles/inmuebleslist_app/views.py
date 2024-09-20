# from django.shortcuts import render # type: ignore
# from inmuebleslist_app.models import Inmueble
# from django.http import JsonResponse # type: ignore

# # Create your views here.

# def inmueble_list(request):
#     inmuebles = Inmueble.objects.all()
#     data = {
#         'inmuebles': list(inmuebles.values())
#     }
    
#     return JsonResponse(data)

# def inmueble_detalle(request, pk):
#     inmueble = Inmueble.objects.get(pk=pk)
#     data = {
#         'direccion':inmueble._direccion,
#         'pais':inmueble.pais,
#         'imagen':inmueble.imagen,
#         'activo':inmueble.active,
#         'description':inmueble.description
#     }
    
#     return JsonResponse(data)
    
    
