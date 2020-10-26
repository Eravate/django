from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Pregunta, Opcion
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    lista_ultimas_preguntas = Pregunta.objects.order_by('-fecha_pub')[:5]
    #output = ','.join([q.pregunta_text for q in lista_ultimas_preguntas])
    #return HttpResponse(output)

    #plantilla = loader.get_template('encuestas/index.html')
    #contexto = {
    #    'lista_ultimas_preguntas':lista_ultimas_preguntas,
    #}
    #return HttpResponse(plantilla.render(contexto,request))
    
    contexto = {'lista_ultimas_preguntas':lista_ultimas_preguntas}
    return render(request,'encuestas/index.html',contexto)

@login_required
def detalle(request, pregunta_id):
    #return HttpResponse("Te encuentras en la pregunta %s" % pregunta_id)
    
    #try:
    #    pregunta = Pregunta.objects.get(pk=pregunta_id)
    #except:
    #    raise Http404("La pregunta no existe")
    #return render(request,'encuestas/detalle.html',{'pregunta':pregunta})
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
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