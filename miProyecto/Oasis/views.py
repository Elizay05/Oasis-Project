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

def guInicio(request):
    return render(request, "Oasis/usuarios/guInicio.html")

def guInicioForm(request):
    return render(request, "Oasis/usuarios/guInicioForm.html")

def guUsuariosBloqueados(request):
    return render(request, "Oasis/usuarios/guUsuariosBloqueados.html")



def invInicio(request):
    return render(request, "Oasis/inventario/invInicio.html")

def invInicioForm(request):
    return render(request, "Oasis/inventario/invInicioForm.html")


#CATEGORÍAS

def invCategorias(request):
#SELECT * FROM Categorias
    q = Categoria.objects.all()
    contexto = {'data' : q}
    return render(request, "Oasis/inventario/invCategorias.html", contexto)

def invCategoriasForm(request):
    return render(request, 'Oasis/inventario/invCategoriasForm.html')

def crearCategoria(request):
    if request.method == "POST":
        try:
            nom = request.POST.get('nombre')
            desc = request.POST.get('descripcion')
            # INSERT INTO Categoria VALUES (nom, desc)
            q = Categoria(
                nombre = nom, 
                descripcion = desc)
            q.save()
            messages.success(request, "Categoria Creada Correctamente!")
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('invCategorias')
    
    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        return redirect('invCategorias')


def eliminarCategoria(request, id):
    try:
        q = Categoria.objects.get(pk = id)
        q.delete()
        messages.success(request, "Categoria Eliminada Correctamente!")
    except Exception as e:
        messages.error(request, f'Error: {e}')
    
    return redirect('invCategorias')


def invCategoriaFormActualizar(request, id):
    q = Categoria.objects.get(pk = id)
    contexto = {'data': q}
    return render(request, 'Oasis/inventario/invCategoriasActualizar.html', contexto)

def actualizarCategoria(request):
    if request.method == "POST":
        id = request.POST.get('id')
        nom = request.POST.get('nombre')
        desc = request.POST.get('descripcion')
        try:
            q = Categoria.objects.get(pk=id)
            q.nombre = nom
            q.descripcion = desc

            q.save()
            messages.success(request, "Categoria Actualizada Correctamente!")

        except Exception as e:
            messages.error(request, f'Error: {e}')

    else:
        messages.warning (request, f'Error: No se enviaron datos...')
        
    return redirect('invCategorias')



def peInicio(request):
    return render (request, "Oasis/pedidos/peInicio.html")

def peHistorial(request):
    return render (request, "Oasis/pedidos/peHistorial.html")

def peGestionMesas(request):
    return render (request, "Oasis/pedidos/peGestionMesas.html")

def pedidoEmpleado(request):
    return render (request, "Oasis/pedidos/pedidoEmpleado.html")



def eveInicio(request):
    return render (request, 'Oasis/eventos/eveInicio.html')

def eveForm(request):
    return render (request, 'Oasis/eventos/eveForm.html')

def eveReserva(request):
    return render (request, 'Oasis/eventos/eveReserva.html')



def meInicio(request):
    return render (request, 'Oasis/menu/meInicio.html')

def meProductos(request):
    return render (request, 'Oasis/menu/meProductos.html')



def gaInicio(request):
    return render (request, 'Oasis/galeria/gaInicio.html')

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