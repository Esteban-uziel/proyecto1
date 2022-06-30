from django.urls import path
from .views import index,busqueda_demanda,buscar,creardemanda,listado,modificar_dem

urlpatterns = [
    path('', index, name="home"),
    path('busqueda_demanda.html/',busqueda_demanda, name="busqueda_demanda"),
    path('buscar/', buscar, name="buscar"),
    path('creardemanda.html/',creardemanda, name="creardemanda"),
    path('list.html',listado ,name="list" ),
    path('modificar/<id>/',modificar_dem  ,name="modific"),
  
    
]