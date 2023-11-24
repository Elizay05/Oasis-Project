from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('registro/', views.registro, name='registro'),

    #USUARIOS
    path('Gestion_Usuarios/', views.guInicio, name='guInicio'),
    path('Agregar_Usuario/', views.guInicioForm, name='guInicioForm'),
    path('Usuarios_Bloqueados/', views.guUsuariosBloqueados, name='guUsuariosBloqueados'),

    path('Usuarios_Eliminados/<int:id>', views.guUsuariosEliminados, name='guUsuariosEliminados'),
    path('Usuarios_Form_Editar/<int:id>', views.guUsuariosFormEditar, name='guUsuariosFormEditar'),
    path('Usuarios_Actualizar/', views.guUsuariosActualizar, name='guUsuariosActualizar'),
    path('guUsuariosCrear/', views.guUsuariosCrear, name='guUsuariosCrear'),


    #CRUD INVENTARIO
    path('Gestion_Inventario/', views.inventario, name='inventario'),
    path('Agregar_Producto/', views.invForm, name='invForm'),
    path('Crear_Inventario/', views.crearInventario, name='crearInventario'),
    path('Eliminar_Inventario/<int:id>', views.eliminarInventario, name='eliminarInventario'),
    path('Inventario_Actualizar/<int:id>', views.invFormActualizar, name='invFormActualizar'),
    path('Actualizar_Inventario/', views.actualizarInventario, name='actualizarInventario'),


    #CRUD CATEGORIAS
    path('Gestion_Categorias/', views.invCategorias, name='invCategorias'),
    path('Categorias_Form/', views.invCategoriasForm, name='invCategoriasForm'),


    path('Gestion_Pedidos/', views.peInicio, name='peInicio'),
    path('Historial_Pedidos/', views.peHistorial, name='peHistorial'),
    path('Gestion_Mesas/', views.peGestionMesas, name='peGestionMesas'),
    path('Agregar_Pedido/', views.pedidoEmpleado, name='pedidoEmpleado'),


#   CRUD EVENTOS
    path('Gestion_Eventos/', views.Eventos, name='Eventos'),
    path('Evento_Form/', views.eveForm, name='eveForm'),
    path('Agregar_Evento/', views.crearEvento, name='crearEvento'),
    path('Eliminar_Evento/<int:id>', views.eliminarEvento, name='eliminarEvento'),
    path('Actualizar_Evento_Form/<int:id>', views.eveFormActualizar, name='eveFormActualizar'),
    path('Actualizar_Evento/', views.actualizarEvento, name='actualizarEvento'),
    path('Reservas/', views.eveReserva, name='eveReserva'),

#   CRUD MENÚ (CATEGORÍAS)
    path('Gestion_Menu/', views.Menu, name='Menu'),
    path('Menu_Form/', views.meForm, name='meForm'),
    path('Crear_Categoria/', views.crearCategoria, name='crearCategoria'),
    path('Eliminar_Categoria/<int:id>', views.eliminarCategoria, name='eliminarCategoria'),
    path('Actualizar_Categoria_Form/<int:id>', views.meFormActualizar, name='meFormActualizar'),
    path('Actualizar_Categoria/', views.actualizarCategoria, name='actualizarCategoria'),
    path('Productos/', views.meProductos, name='meProductos'),


#   CRUD GALERÍA
    path('Gestion_Galeria/', views.gaInicio, name='gaInicio'),
    path('Galeria_Form/', views.gaCarpetaForm, name='gaCarpetaForm'),
    path('Agregar_Carpeta/', views.crearCarpeta, name='crearCarpeta'),
    path('Galeria_Fotos/', views.gaFotos, name='gaFotos'),
    path('Eliminar_Carpeta/<int:id>', views.eliminarCarpeta, name='eliminarCarpeta'),
    path('Actualizar_Carpeta_Form/<int:id>', views.gaCarpetaFormActualizar, name='gaCarpetaFormActualizar'),
    path('Actualizar_Carpeta/', views.actualizarCarpeta, name='actualizarCarpeta'),




    path('saludar/', views.saludar, name='saludar'),
    path('saludar_param/<str:nombre>/<str:apellido>', views.saludar_param, name='saludar_param'),
    path('calculadora/<int:num1>/<int:num2>/<str:operador>', views.calculadora, name='calculadora'),
]   