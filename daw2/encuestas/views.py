from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Pregunta, Opcion, Categoria
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone

from .forms import CategoriaForm, PreguntaForm

@login_required
def categoria_create_read(request):
    if not request.user.is_superuser: # Control de acceso unicamente para superuser
        raise PermissionDenied

    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('encuestas:categoria')
    else:
        form = CategoriaForm()
        categorias = Categoria.objects.all()
        print(categorias)
        contexto = {'form':form,'categorias':categorias}
        return render(request,'encuestas/categorias.html',contexto)


@login_required
def categoria_update(request, categoria_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    categoria = Categoria.objects.get(id=categoria_id)
    if request.method == 'GET':
        form = CategoriaForm(instance=categoria)
    else:
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
        return redirect('encuestas:categoria')
    categorias = Categoria.objects.all()
    contexto = {'form':form,'categorias':categorias,'categoria':categoria}
    return render(request,'encuestas/categorias.html',contexto)


@login_required
def categoria_delete(request, categoria_id):
    if not request.user.is_superuser:
        raise PermissionDenied


    categoria = Categoria.objects.get(id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('encuestas:categoria')
    contexto = {'categoria':categoria}
    return render(request,'encuestas/categoria_delete.html',contexto)

@login_required
def index(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            preguntaAGuardar = form.save(commit=False)
            preguntaAGuardar.creador = request.user.usuario
            preguntaAGuardar.fecha_pub = timezone.now()
            preguntaAGuardar.save()
            preguntaAGuardar.categoria.set(form.cleaned_data['categoria'])
        return redirect('encuestas:index')
    else:
        form = PreguntaForm()
        # lista_ultimas_preguntas = Pregunta.objects.order_by('-fecha_pub')[:5]
        lista_ultimas_preguntas = Pregunta.objects.all()
        contexto = {'form':form,'lista_ultimas_preguntas':lista_ultimas_preguntas}
        return render(request,'encuestas/index.html',contexto)

@login_required
def pregunta_update(request,pregunta_id):
    pregunta = Pregunta.objects.get(id=pregunta_id)
    if request.method == 'GET':
        form = PreguntaForm(instance=pregunta)
    else:
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
        return redirect('encuestas:index')
    lista_ultimas_preguntas = Pregunta.objects.all()
    contexto = {'form':form,'lista_ultimas_preguntas':lista_ultimas_preguntas,'pregunta':pregunta}
    return render(request,'encuestas/index.html',contexto)

@login_required
def pregunta_delete(request,pregunta_id):
    pregunta = Pregunta.objects.get(id=pregunta_id)
    if request.method == 'POST':
        pregunta.delete()
        return redirect('encuestas:index')
    contexto = {'pregunta':pregunta}
    return render(request,'encuestas/pregunta_delete.html',contexto)

@login_required
def opcion_delete(request,opcion_id):
    opcion = get_object_or_404(Opcion, pk=opcion_id)
    if request.method == 'POST':
        opcion.delete()
        return redirect('encuestas:detalle',opcion.pregunta.id)
    else:
        return render(request,'encuestas/detalle_delete.html',{'opcion':opcion})

@login_required
def detalle(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    if request.method == 'POST':
        nueva_opcion = Opcion(opcion_text=request.POST['opcion_text'],pregunta=pregunta)
        nueva_opcion.save()
        return redirect('encuestas:detalle',pregunta_id)
    else:
        return render(request,'encuestas/detalle.html',{'pregunta':pregunta})

@login_required
def resultados(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request,'encuestas/resultados.html',{'pregunta':pregunta})

@login_required
def votar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        opcion_seleccionada = pregunta.opcion_set.get(pk=request.POST['opcion'])
    except(KeyError, Opcion.DoesNotExist):
        return render(request,'encuestas/detalle.html', {
            'pregunta':pregunta,
            'mensaje_error':"No has seleccionado ninguna opción"
        })
    else:
        opcion_seleccionada.votos += 1
        opcion_seleccionada.save()
        return HttpResponseRedirect(reverse('encuestas:resultados',args=(pregunta_id,)))