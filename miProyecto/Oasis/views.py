from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.files.uploadedfile import SimpleUploadedFile


from rest_framework import viewsets

from .serializers import *




#Importar todos los modelos de la base de datos.
from .models import *

# Create your views here.

def index(request):
    logueo = request.session.get("logueo", False)
    if logueo == False:
        return render(request, "Oasis/index.html")
    else:
        return redirect("inicio")

def login(request):
	if request.method == "POST":
		user = request.POST.get("correo")
		passw = request.POST.get("clave")
		#Select * from Usuario where correo = "user" and clave = "passw"
		try:
			q = Usuario.objects.get(email = user, clave = passw)
			# Crear variable de sesión.
			request.session["logueo"] = {
				"id": q.id,
				"nombre": q.nombre,
				"rol": q.rol,
                "nombre_rol":q.get_rol_display()
			}
			messages.success(request, f"Bienvendido {q.nombre}!!")
			return redirect("inicio")
		except Exception as e:
			messages.error(request, f"Error: Usuario o contraseña incorrectos {e}")
			return redirect("index")
	else:
		messages.warning(request, "Error: No se enviaron datos.")
		return redirect("index")


def logout(request):
	try:
		del request.session["logueo"]
		messages.success(request, "Sesión cerrada correctamente")
		return redirect("index")
	except Exception as e:
		messages.warning(request, "No se pudo cerrar sesión")
		return redirect("inicio")
    
def inicio(request):
    logueo = request.session.get("logueo", False)
    if logueo:
        try:
            usuario_id = request.session['logueo']['id']
            usuario = Usuario.objects.get(id=usuario_id)
            contexto = {'data': usuario}
            return render(request, "Oasis/index.html", contexto)
        except Usuario.DoesNotExist:
            messages.error(request, "El usuario no existe")
    else:
        return redirect("index")
    


def registro(request):
    return render(request, 'Oasis/registro.html')


#PERFIL
def ver_perfil(request):
    logueo = request.session.get("logueo", False)
    #Consultamos en base de datos el ID del usuario logueado
    q = Usuario.objects.get(pk = logueo["id"])
    roles = Usuario.ROLES
    estado = Usuario.ESTADO
    contexto = {'data': q, 'roles': roles, 'estado':estado}
    return render(request, "Oasis/login/perfil.html", contexto)

def editar_perfil(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        fecha_nacimiento = request.POST.get('fechaNacimiento')
        email = request.POST.get('email')
        cedula = request.POST.get('cedula')
        rol = request.POST.get('rol')
        estado = request.POST.get('Estado')
        foto_nueva = request.FILES.get('foto_nueva')

        try:
            q = Usuario.objects.get(pk = id)
            q.nombre = nombre
            q.email = email
            q.fecha_nacimiento = fecha_nacimiento
            q.rol = rol
            q.cedula = cedula
            q.estado = estado
            
            if foto_nueva:
                q.foto = foto_nueva

            q.save()
            messages.success(request, "Usuario actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')

    return redirect('ver_perfil')


#CAMBIAR CONTRASEÑA
def cambio_clave_formulario(request):
    return render(request, "Oasis/login/cambio_clave.html")

def cambiar_clave(request):
    if request.method == "POST":
        logueo = request.session.get("logueo", False)
        q = Usuario.objects.get(pk=logueo["id"])

        c1 = request.POST.get("nueva1")
        c2 = request.POST.get("nueva2")

        if q.clave == request.POST.get("clave"):
            if c1 == c2:
                #Cambiar clave en DB
                q.clave = c1
                q.save()
                messages.success(request, "Contraseña guardada correctamente!")
                return redirect('ver_perfil')
            else:
               messages.info(request, "Las contraseñas nuevas no coinciden...")
        else:
            messages.error(request, "Contraseña no válida...")
    else:
        messages.warning(request, "Error: No se enviaron datos...")
    
    return redirect('cc_formulario')



#USUARIOS
def guInicio(request):
    logueo = request.session.get("logueo", False)
    user = Usuario.objects.get(pk = logueo["id"])
    q = Usuario.objects.all()
    contexto = {'data': q, 'user': user}
    return render(request, "Oasis/usuarios/guInicio.html", contexto)

def guInicioForm(request):
    roles = Usuario.ROLES
    estado = Usuario.ESTADO

    contexto = {'roles': roles, 'estado': estado}
    return render(request, "Oasis/usuarios/guInicioForm.html", contexto)

def guUsuariosBloqueados(request):
    return render(request, "Oasis/usuarios/guUsuariosBloqueados.html")

def guUsuariosCrear(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            fecha_nacimiento = request.POST.get('fechaNacimiento')
            email = request.POST.get('email')
            clave = request.POST.get('clave')
            cedula = request.POST.get('cedula')
            foto = request.FILES.get('foto')
            rol = int(request.POST.get('rol'))
            estado = int(request.POST.get('Estado'))

            if foto is None:
                foto = "Img_usuarios/default.png"
            
            q = Usuario(
                nombre=nombre,
                fecha_nacimiento=fecha_nacimiento,
                email=email,
                clave=clave,
                rol=rol,
                cedula=cedula,
                estado=estado,
                foto=foto,
            )

            q.save()
            messages.success(request, "Usuario creado correctamente")
        except Exception as e:
            messages.error(request, f'Error: {e}')
    else:
        messages.warning(request, 'No se enviaron datos')

    return redirect('guInicio')

def guUsuariosEliminados(request, id):
    try:
        q = Usuario.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Usuario eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('guInicio')

def guUsuariosFormEditar(request, id):
    q = Usuario.objects.get(pk = id)
    roles = Usuario.ROLES
    estado = Usuario.ESTADO
    contexto = {'data': q, 'roles': roles, 'estado':estado}

    return render(request, 'Oasis/usuarios/guInicioFormEditar.html', contexto)

def guUsuariosActualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        fecha_nacimiento = request.POST.get('fechaNacimiento')
        email = request.POST.get('email')
        clave = request.POST.get('clave')
        cedula = request.POST.get('cedula')
        rol = request.POST.get('rol')
        estado = request.POST.get('Estado')
        foto_nueva = request.FILES.get('foto_nueva')

        try:
            q = Usuario.objects.get(pk = id)
            q.nombre = nombre
            q.email = email
            q.clave = clave
            q.fecha_nacimiento = fecha_nacimiento
            q.rol = rol
            q.cedula = cedula
            q.estado = estado
            
            if foto_nueva:
                q.foto = foto_nueva

            q.save()
            messages.success(request, "Usuario actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')

    return redirect('guInicio')


#INVENTARIO
def invInicio(request):
    q = Inventario.objects.all()
    p = Producto.objects.all()
    contexto = {'data': q, 'producto': p}
    return render(request, "Oasis/inventario/invInicio.html", contexto)

def invForm(request):
    q = Producto.objects.all()
    contexto = {'data': q}
    return render(request, "Oasis/inventario/invInicioForm.html", contexto)

def crearInventario(request):
    if request.method == "POST":
        try:
            producto =Producto.objects.get(pk=request.POST.get('producto')) 
            cantidad = request.POST.get('cantidad')
            fecha_caducidad = request.POST.get('fecha_caducidad')
            # INSERT INTO Categoria VALUES (nom, desc)
            q = Inventario(
                producto = producto, 
                cantidad = cantidad,
                fecha_caducidad = fecha_caducidad)
            q.save()
            messages.success(request, "Producto de Inventario Registrado Correctamente!")
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('inventario')
    
    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        return redirect('inventario')
    
def eliminarInventario(request, id):
    try:
        q = Inventario.objects.get(pk = id)
        q.delete()
        messages.success(request, "Producto de Inventario Eliminado Correctamente!")
    except Exception as e:
        messages.error(request, f'Error: {e}')
    
    return redirect('inventario')
       
def invFormActualizar(request, id):
    q = Inventario.objects.get(pk = id)
    p = Producto.objects.all()
    contexto = {'data': q, 'producto': p}
    return render(request, 'Oasis/inventario/invFormActualizar.html', contexto)

def actualizarInventario(request):
    if request.method == "POST":
        id = request.POST.get('id')
        producto =Producto.objects.get(pk=request.POST.get('producto')) 
        cantidad = request.POST.get('cantidad')
        fecha_caducidad = request.POST.get('fecha_caducidad')
        try:
            q = Inventario.objects.get(pk=id)
            q.producto = producto
            q.cantidad = cantidad
            q.fecha_caducidad = fecha_caducidad
            q.save()
            messages.success(request, "Producto de Inventario Actualizado Correctamente!")

        except Exception as e:
            messages.error(request, f'Error: {e}')

    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        
    return redirect('inventario')


#PRODUCTOS

def invProductos(request):
#SELECT * FROM Productos
    q = Producto.objects.all()
    contexto = {'data' : q}
    return render(request, "Oasis/inventario/invProductos.html", contexto)

def invProductosForm(request):
    q = Categoria.objects.all()
    contexto = {'data': q}
    return render(request, 'Oasis/inventario/invProductosForm.html', contexto)

def crearProducto(request):
    if request.method == "POST":
        try:
            nom = request.POST.get('nombre')
            desc = request.POST.get('descripcion')
            cat_id = int(request.POST.get('categoria'))
            pre = request.POST.get('precio')
            foto = request.FILES.get('foto')

            cat = Categoria.objects.get(pk=cat_id)
            
            if foto == None:
                foto = "Img_productos/default.png"

            q = Producto(
                nombre=nom,
                descripcion=desc,
                categoria=cat,
                precio=pre,
                foto=foto,
            )
            q.save()
            messages.success(request, "Producto Agregado Correctamente!")
        except Exception as e:
            messages.error(request, f'Error: {e}')
    else:
        messages.warning(request, f'Error: No se enviaron datos...')

    return redirect('Productos')

def eliminarProducto(request, id):
    try:
        q = Producto.objects.get(pk = id)
        q.delete()
        messages.success(request, "Producto Eliminado Correctamente!")
    except Exception as e:
        messages.error(request, f'Error: {e}')
    
    return redirect('Productos')


def invFormProductosActualizar(request, id):
    q = Producto.objects.get(pk = id)
    c = Categoria.objects.all()
    print(type(q.precio), q.precio)
    contexto = {'data': q, 'categorias' : c}
    return render(request, 'Oasis/inventario/invProductosActualizar.html', contexto)

def actualizarProducto(request):
    if request.method == "POST":
        id = request.POST.get('id')
        cat = Categoria.objects.get(pk=request.POST.get('categoria'))
        nom = request.POST.get('nombre')
        desc = request.POST.get('descripcion')
        precio_str = request.POST.get('precio')
        precio_str = precio_str.replace(',', '.')
        pre = float(precio_str)
        foto_nueva = request.FILES.get('foto_nueva')

        try:
            q = Producto.objects.get(pk=id)
            q.nombre = nom
            q.categoria = cat
            q.descripcion = desc
            q.precio = pre

            if foto_nueva:
                q.foto = foto_nueva

            q.save()
            messages.success(request, "Producto Actualizado Correctamente!")

        except Exception as e:
            messages.error(request, f'Error: {e}')

    else:
        messages.warning(request, f'Error: No se enviaron datos...')

    return redirect('Productos')





def peInicio(request):
    return render (request, "Oasis/pedidos/peInicio.html")

def peHistorial(request):
    return render (request, "Oasis/pedidos/peHistorial.html")

def peGestionMesas(request):
    return render (request, "Oasis/pedidos/peGestionMesas.html")

def pedidoEmpleado(request):
    return render (request, "Oasis/pedidos/pedidoEmpleado.html")



#EVENTOS

def eveInicio(request):
#SELECT * FROM Eventos
    q = Evento.objects.all()
    contexto = {'data' : q}
    return render(request, "Oasis/eventos/eveInicio.html", contexto)

def eveForm(request):
    return render (request, 'Oasis/eventos/eveForm.html')

def crearEvento(request):
    if request.method == "POST":
        try:
            nom = request.POST.get('nombre')
            date = request.POST.get('fecha')
            time = request.POST.get('hora_incio')
            desc = request.POST.get('descripcion')
            foto = request.FILES.get('foto')

            if foto == None:
                foto = "Img_eventos/default.png"

            # INSERT INTO Evento VALUES (nom, date, time, desc, foto)
            q = Evento(
                nombre = nom,
                fecha = date,
                hora_incio = time,
                descripcion = desc,
                foto = foto,
            )
            q.save()
            messages.success(request, "Evento Creado Correctamente!")
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('Eventos')
    
    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        return redirect('Eventos')

def eliminarEvento(request, id):
    try:
        q = Evento.objects.get(pk = id)
        q.delete()
        messages.success(request, "Evento Eliminado Correctamente!")
    except Exception as e:
        messages.error(request, f'Error: {e}')
    
    return redirect('Eventos')

def eveFormActualizar(request, id):
    q = Evento.objects.get(pk = id)
    contexto = {'data': q}
    return render(request, 'Oasis/eventos/eveFormActualizar.html', contexto)

def actualizarEvento(request):
    if request.method == "POST":
        id = request.POST.get('id')
        nom = request.POST.get('nombre')
        date = request.POST.get('fecha')
        time = request.POST.get('hora_incio')
        desc = request.POST.get('descripcion')
        foto_nueva = request.FILES.get('foto_nueva')
        try:
            q = Evento.objects.get(pk=id)
            q.nombre = nom
            q.fecha = date
            q.hora_incio = time
            q.descripcion = desc

            if foto_nueva:
                q.foto = foto_nueva

            q.save()
            messages.success(request, "Evento Actualizado Correctamente!")

        except Exception as e:
            messages.error(request, f'Error: {e}')

    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        
    return redirect('Eventos')



def eveReserva(request):
    return render (request, 'Oasis/eventos/eveReserva.html')


# MENÚ (CATEGORÍAS)
def meInicio(request):
#SELECT * FROM Eventos
    q = Categoria.objects.all()
    contexto = {'data' : q}
    return render(request, "Oasis/menu/meInicio.html", contexto)

def meForm(request):
    return render (request, 'Oasis/menu/meForm.html')

def crearCategoria(request):
    if request.method == "POST":
        try:
            nom = request.POST.get('nombre')
            desc = request.POST.get('descripcion')
            foto = request.FILES.get('foto')

            if foto == None:
                foto = "Img_categorias/default.jpg"

            # INSERT INTO Categoria VALUES (nom, desc)
            q = Categoria(
                nombre = nom, 
                descripcion = desc,
                foto = foto,
                )
            q.save()
            messages.success(request, "Categoria Creada Correctamente!")
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('Menu')
    
    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        return redirect('Menu')

def eliminarCategoria(request, id):
    try:
        q = Categoria.objects.get(pk = id)
        q.delete()
        messages.success(request, "Categoria Eliminada Correctamente!")
    except Exception as e:
        messages.error(request, f'Error: {e}')
    
    return redirect('Menu')

def meFormActualizar(request, id):
    q = Categoria.objects.get(pk = id)
    contexto = {'data': q}
    return render(request, 'Oasis/menu/meFormActualizar.html', contexto)

def actualizarCategoria(request):
    if request.method == "POST":
        id = request.POST.get('id')
        nom = request.POST.get('nombre')
        desc = request.POST.get('descripcion')
        foto_nueva = request.FILES.get('foto_nueva')
        try:
            q = Categoria.objects.get(pk=id)
            q.nombre = nom
            q.descripcion = desc

            if foto_nueva:
                q.foto = foto_nueva

            q.save()
            messages.success(request, "Categoria Actualizada Correctamente!")

        except Exception as e:
            messages.error(request, f'Error: {e}')

    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        
    return redirect('Menu')

def meProductos(request):
    return render (request, 'Oasis/menu/meProductos.html')



def gaInicio(request):
#SELECT * FROM Galeria
    q = Galeria.objects.all()
    contexto = {'data' : q}
    return render(request, "Oasis/galeria/gaInicio.html", contexto)


def gaCarpetaForm(request):
    return render (request, 'Oasis/galeria/gaCarpetaForm.html')


def crearCarpeta(request):
    if request.method == "POST":
        try:
            nom = request.POST.get('nombre')
            date = request.POST.get('fecha')
            foto = request.FILES.get('foto')

            if foto == None:
                foto = "Img_carpeta/default.png"

            # INSERT INTO Evento VALUES (nom, date, time, desc, foto)
            q = Galeria(
                nombre = nom,
                fecha = date,
                foto = foto,
            )
            q.save()
            messages.success(request, "Carpeta Creada Correctamente!")
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('gaInicio')
    
    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        return redirect('gaInicio')

def eliminarCarpeta(request, id):
    try:
        q = Galeria.objects.get(pk = id)
        q.delete()
        messages.success(request, "Carpeta Eliminada Correctamente!")
    except Exception as e:
        messages.error(request, f'Error: {e}')
    
    return redirect('gaInicio')

def gaCarpetaFormActualizar(request, id):
    q = Galeria.objects.get(pk = id)
    contexto = {'data': q}
    return render(request, 'Oasis/galeria/gaCarpetaFormActualizar.html', contexto)


def actualizarCarpeta(request):
    if request.method == "POST":
        id = request.POST.get('id')
        nom = request.POST.get('nombre')
        date = request.POST.get('fecha')
        foto_nueva = request.FILES.get('foto_nueva')
        try:
            q = Galeria.objects.get(pk=id)
            q.nombre = nom
            q.fecha = date
            
            if foto_nueva:
                q.foto = foto_nueva

            q.save()
            messages.success(request, "Carpeta Actualizada Correctamente!")

        except Exception as e:
            messages.error(request, f'Error: {e}')

    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        
    return redirect('gaInicio')


def gaFotos(request):
    return render(request, 'Oasis/galeria/gaFotos.html')


# Vistas para el conjunto de datos de las API
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoMesaViewSet(viewsets.ModelViewSet):
    queryset = PedidoMesa.objects.all()
    serializer_class = PedidoMesaSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class GaleriaViewSet(viewsets.ModelViewSet):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer

class FotosViewSet(viewsets.ModelViewSet):
    queryset = Fotos.objects.all()
    serializer_class = FotosSerializer