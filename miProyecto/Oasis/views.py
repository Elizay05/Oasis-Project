from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

#Importar todos los modelos de la base de datos.
from .models import *

# Create your views here.

def index(request):
    logueo = request.session.get("logueo", False)
    if logueo == False:
        return render(request, "Oasis/login/login.html")
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
				"rol": q.rol
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
		return render(request, "Oasis/index.html")
	else:
		return redirect("index")


def registro(request):
    return render(request, 'Oasis/registro.html')


#USUARIOS
def guInicio(request):
    q = Usuario.objects.all()
    contexto = {'data': q}
    return render(request, "Oasis/usuarios/guInicio.html", contexto)

def guInicioForm(request):
    return render(request, "Oasis/usuarios/guInicioForm.html")

def guUsuariosBloqueados(request):
    return render(request, "Oasis/usuarios/guUsuariosBloqueados.html")

def guUsuariosCrear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        fecha_nacimiento = request.POST.get('fechaNacimiento')
        email = request.POST.get('email')
        clave = request.POST.get('clave')
        cedula = request.POST.get('cedula')
        rol = request.POST.get('rol')
        estado = request.POST.get('Estado')
        foto = request.POST.get('foto')
        try:
            q = Usuario(
                nombre = nombre,
                fecha_nacimiento = fecha_nacimiento,
                email = email,
                clave = clave,
                rol = rol,
                cedula = cedula,
                estado = estado,
                foto = foto
            )

            q.save()
            messages.success(request, "Usuario creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')

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
    contexto = {'data': q}

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
        foto = request.POST.get('foto')
        try:
            q = Usuario.objects.get(pk = id)
            q.nombre = nombre
            q.email = email
            q.clave = clave
            q.fecha_nacimiento = fecha_nacimiento
            q.rol = rol
            q.cedula = cedula
            q.estado = estado
            q.foto = foto

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
            messages.success(request, "Producto de Inventario Creado Correctamente!")
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


#CATEGORÍAS

def invCategorias(request):
#SELECT * FROM Categorias
    q = Categoria.objects.all()
    contexto = {'data' : q}
    return render(request, "Oasis/inventario/invCategorias.html", contexto)

def invCategoriasForm(request):
    return render(request, 'Oasis/inventario/invCategoriasForm.html')



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
            # INSERT INTO Evento VALUES (nom, date, time, desc, foto)
            q = Evento(
                nombre = nom,
                fecha = date,
                hora_incio = time,
                descripcion = desc,
                foto = f"fotos/{foto}",
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
        foto = request.POST.get('foto')
        try:
            q = Evento.objects.get(pk=id)
            q.nombre = nom
            q.fecha = date
            q.hora_incio = time
            q.descripcion = desc
            q.foto = f'fotos/{foto}'

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
            foto = request.POST.get('foto')
            # INSERT INTO Categoria VALUES (nom, desc)
            q = Categoria(
                nombre = nom, 
                descripcion = desc,
                foto = foto)
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
        foto = request.POST.get('foto')
        try:
            q = Categoria.objects.get(pk=id)
            q.nombre = nom
            q.descripcion = desc
            q.foto = f'fotos/{foto}'

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
            # INSERT INTO Evento VALUES (nom, date, time, desc, foto)
            q = Galeria(
                nombre = nom,
                fecha = date,
                foto = f"fotos/{foto}",
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
        foto = request.POST.get('foto')
        try:
            q = Galeria.objects.get(pk=id)
            q.nombre = nom
            q.fecha = date
            q.foto = f'fotos/{foto}'

            q.save()
            messages.success(request, "Carpeta Actualizada Correctamente!")

        except Exception as e:
            messages.error(request, f'Error: {e}')

    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        
    return redirect('gaInicio')


def gaFotos(request):
    return render(request, 'Oasis/galeria/gaFotos.html')



def saludar(request):
    return HttpResponse("Hola, <strong style='color:red'>A todos!!</strong>")

def saludar_param(request, nombre, apellido):
    return HttpResponse(f"Hola, <strong style='color:red'>{nombre} {apellido}</strong>")


#Construir una miniCalculadora, que haga operaciones con dos números

def calculadora(request, num1, num2, operador):
    if operador == "suma":
        return HttpResponse(f"La suma de {num1} + {num2} es: <strong style='color:red'>{num1 + num2}</strong>")
    elif operador == "resta":
        return HttpResponse(f"La resta de {num1} - {num2} es: <strong style='color:red'>{num1 - num2}</strong>")
    elif operador == "multiplicacion":
        return HttpResponse(f"La multiplicación de {num1} * {num2} es: <strong style='color:red'>{num1 * num2}</strong>")
    elif operador == "division":
        return HttpResponse(f"La division de {num1} / {num2} es: <strong style='color:red'>{num1 / num2}</strong>")
    else:
        return HttpResponse("Operador no valido")