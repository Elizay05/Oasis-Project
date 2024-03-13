from django.urls import path, include
from rest_framework import routers


from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'evento', views.EventoViewSet)
router.register(r'mesa', views.MesaViewSet)
router.register(r'reserva', views.ReservaViewSet)
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'producto', views.ProductoViewSet)
router.register(r'pedido', views.PedidoViewSet)
router.register(r'pedido_mesa', views.PedidoMesaViewSet)
#router.register(r'inventario', views.InventarioViewSet)
router.register(r'galeria', views.GaleriaViewSet)
router.register(r'fotos', views.FotosViewSet)
router.register(r'venta', views.VentaViewSet)
router.register(r'detalle_venta', views.DetalleVentaViewSet)


urlpatterns = [
    path('api/1.0/', include(router.urls)),


    path('', views.index, name="index"),
	path('inicio/', views.inicio, name="inicio"),


    #Autenticación de usuarios del sistema
    path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),


    path('registro/', views.registro, name='registro'),

    #PERFIL
    path('Perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),


    #CAMBIAR CONTRASEÑA
    path('cc_formulario/', views.cambio_clave_formulario, name="cc_formulario"),
    path('cambiar_clave/', views.cambiar_clave, name="cambiar_clave"),


    #USUARIOS
    path('Gestion_Usuarios/', views.guInicio, name='guInicio'),
    path('Agregar_Usuario/', views.guInicioForm, name='guInicioForm'),
    path('Usuarios_Bloqueados/', views.guUsuariosBloqueados, name='guUsuariosBloqueados'),

    path('Usuarios_Eliminados/<int:id>', views.guUsuariosEliminados, name='guUsuariosEliminados'),
    path('Usuarios_Form_Editar/<int:id>', views.guUsuariosFormEditar, name='guUsuariosFormEditar'),
    path('Usuarios_Actualizar/', views.guUsuariosActualizar, name='guUsuariosActualizar'),
    path('guUsuariosCrear/', views.guUsuariosCrear, name='guUsuariosCrear'),


    #CRUD INVENTARIO
    #path('Gestion_Inventario/', views.invInicio, name='inventario'),
    #path('Agregar_Producto/', views.invForm, name='invForm'),
    #path('Crear_Inventario/', views.crearInventario, name='crearInventario'),
    #path('Eliminar_Inventario/<int:id>', views.eliminarInventario, name='eliminarInventario'),
    #path('Inventario_Actualizar/<int:id>', views.invFormActualizar, name='invFormActualizar'),
    #path('Actualizar_Inventario/', views.actualizarInventario, name='actualizarInventario'),


    #CRUD PRODUCTOS
    path('Gestion_Categorias/', views.invProductos, name='Productos'),
    path('Categorias_Form/', views.invProductosForm, name='invProductosForm'),
    path('Crear_Producto/', views.crearProducto, name='crearProducto'),
    path('Eliminar_Producto/<int:id>', views.eliminarProducto, name='eliminarProducto'),
    path('Actualizar_Producto_Form/<int:id>', views.invFormProductosActualizar, name='invFormProductosActualizar'),
    path('Actualizar_Producto/', views.actualizarProducto, name='actualizarProducto'),


    path('Gestion_Pedidos/', views.peInicio, name='peInicio'),
    path('Historial_Pedidos/', views.peHistorial, name='peHistorial'),
    path('Gestion_Mesas/', views.peGestionMesas, name='peGestionMesas'),
    path('Agregar_Pedido/', views.pedidoEmpleado, name='pedidoEmpleado'),


#   CRUD EVENTOS
    path('Gestion_Eventos/', views.eveInicio, name='Eventos'),
    path('Evento_Form/', views.eveForm, name='eveForm'),
    path('Agregar_Evento/', views.crearEvento, name='crearEvento'),
    path('Eliminar_Evento/<int:id>', views.eliminarEvento, name='eliminarEvento'),
    path('Actualizar_Evento_Form/<int:id>', views.eveFormActualizar, name='eveFormActualizar'),
    path('Actualizar_Evento/', views.actualizarEvento, name='actualizarEvento'),
    path('Reservas/', views.eveReserva, name='eveReserva'),

#   CRUD MENÚ (CATEGORÍAS)
    path('Gestion_Menu/', views.meInicio, name='Menu'),
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



#   FRONT PRODUCTOS
    path('front_productos/', views.front_productos, name='front_productos'),


# CARRITO DE COMPRA
	path("carrito_add/", views.carrito_add, name="carrito_add"),
	path("carrito_ver/", views.carrito_ver, name="carrito_ver"),
    path("carrito_eliminar/<int:id>/", views.carrito_eliminar, name="carrito_eliminar"),
	path("vaciar_carrito/", views.vaciar_carrito, name="vaciar_carrito"),
	path("actualizar_totales_carrito/<int:id_producto>/", views.actualizar_totales_carrito, name="actualizar_totales_carrito"),

#VENTAS
	path("crear_venta/", views.crear_venta, name="crear_venta"),
	path("ver_ventas/", views.ver_ventas, name="ver_ventas"),
	path("ver_detalles/<int:id>/", views.ver_detalles, name="ver_detalles"),




]   