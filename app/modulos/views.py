from django.shortcuts import render,redirect
from .models import Empleado

# Create your views here.


def first_view(request):
    return render(request, 'login.html')

def second_view(request):
    return render(request, 'index.html')


def third_view(request):
    return render(request, 'rec_tono_piel.html')


def four_view(request):
    return render(request, 'rec_tip_ceja.html')


def five_view(request):
    return render(request, 'rec_tono_cabello.html')

def six_view(request):
    return render(request, 'cal_sug.html')


def guardar_registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        identificacion = request.POST.get('identificacion')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        foto = request.FILES.get('foto')  # Asegúrate de tener enctype="multipart/form-data" en tu formulario HTML

        # Crear un nuevo empleado con los datos recibidos
        nuevo_empleado = Empleado(nombre=nombre, apellido=apellido, identificacion=identificacion,
                                  email=email, telefono=telefono, direccion=direccion, foto=foto)
        nuevo_empleado.save()

        # Redirigir a alguna página de confirmación o a la página de inicio
        return redirect('login')  # Cambiar 'pagina_inicio' por la URL de tu página de inicio

    # En caso de que la solicitud no sea POST, simplemente renderiza la plantilla nuevamente
    return render(request, 'login.html')




