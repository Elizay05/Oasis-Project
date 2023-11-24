from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

#Importar todos los modelos de la base de datos.
from .models import *

# Create your views here.

def index(request):
    return render(request, "Oasis/index.html")


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
        cedula = request.POST.get('cedula')
        rol = request.POST.get('rol')
        telefono = request.POST.get('Telefono')
        estado = request.POST.get('Estado')
        try:
            q = Usuario(
                nombre = nombre,
                fecha_nacimiento = fecha_nacimiento,
                email = email,
                rol = rol,
                cedula = cedula,
                telefono = telefono,
                estado = estado,
            )

            q.save()
            messages.success(request, "Fue creado correctamente")
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
        cedula = request.POST.get('cedula')
        rol = request.POST.get('rol')
        telefono = request.POST.get('Telefono')
        estado = request.POST.get('Estado')
        try:
            q = Usuario.objects.get(pk = id)
            q.nombre = nombre
            q.email = email
            q.fecha_nacimiento = fecha_nacimiento
            q.rol = rol
            q.cedula = cedula
            q.telefono = telefono
            q.estado = estado

            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')

    return redirect('guInicio')


#INVENTARIO
def inventario(request):
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

def Eventos(request):
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
def Menu(request):
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