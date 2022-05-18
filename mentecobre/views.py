from django.shortcuts import render

# Create your views here.
from .models import Glosario, Articulos
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import date


@require_http_methods(["GET", "POST"])   
def glosario(request):
    search = request.GET.get("q", None)
    if search is not None:
        query = search
        object_list = Glosario.objects.filter(
            Q(wordEn__icontains=query) | Q(wordEs__icontains=query)
        )
        
        ser_instance = serializers.serialize('json', object_list)
    else:
        object_list=None
    
    print(object_list)
    return render(
        request,
        'mentecobre/glosario.html',
        context={"object_list":object_list}
    )

def portada(request):
    """
    Función vista para la página inicio del sitio.
    """

    # Renderiza la plantilla HTML portada.html con los datos en la variable contexto
    return render(
        request,
        'portada.html',
        context={},
    )

@login_required
def traducciones(request):
    usuarioid=request.user.id
    usuario=request.user.username
    
    universo = request.user.universo
    
    articulo_asignado=Articulos.objects.filter(traducido__isnull=True).filter(traductor=usuarioid)
    
    articulo_noasignado = []
    for universo_item in universo:

        articulo = Articulos.objects.filter(universo=universo_item).filter(traducido__isnull=True).filter(traductor__isnull=True).exclude(tipo='RD').order_by('prioridad').values().first()

        if articulo != None:
            articulo_noasignado.append(articulo)
    

    return render(
        request,
        'traducciones.html',
        context={"usuario":usuario, "articulo":articulo_asignado, "siguiente_articulo":articulo_noasignado},
    )


@login_required
def asignartraducciones(request):
    if request.method == "POST":
        userid=request.user.id
        idarticulo=request.POST.get("id",None)
        fecha=date.today()
        Articulos.objects.filter(pk=idarticulo).update(traductor=userid,fechaasignado=fecha)
        
        return JsonResponse({"instance": "Éxito"}, status=200)
    else:
            # some form errors occured.
        print("Vayase señor cuesta")
        return JsonResponse({"error": ""}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
    
@login_required
def marcartraducido(request):
    if request.method == "POST":
        traducidoup=request.POST.get("traducido",None)
        idarticulo=request.POST.get("id",None)
        notas=request.POST.get("notas",None)
        fecha=date.today()
        Articulos.objects.filter(pk=idarticulo).update(traducido=traducidoup,fechatraducido=fecha,notas=notas)
        return JsonResponse({"instance": "Éxito"}, status=200)

    else:
            # some form errors occured.
        return JsonResponse({"error": ""}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
    
@login_required
def revisiones(request):
    usuario=request.user.username
    usuarioid=request.user.id
    universo = request.user.universo
    
    articulo_asignado=Articulos.objects.exclude(revisado='Y').filter(revisor=usuarioid)
    
    articulo_noasignado = []
    for universo_item in universo:

        articulo = Articulos.objects.filter(universo=universo_item).filter(traducido__isnull=False).filter(revisado__isnull=True).filter(revisor__isnull=True).order_by('prioridad').values().first()

        if articulo != None:
            articulo_noasignado.append(articulo)
    

    return render(
        request,
        'revisiones.html',
        context={"usuario":usuario, "articulo":articulo_asignado, "siguiente_articulo":articulo_noasignado},
    )
    
@login_required
def asignarrevisiones(request):
    if request.method == "POST":
        userid=request.user.id
        idarticulo=request.POST.get("id",None)
        fecha=date.today()
        Articulos.objects.filter(pk=idarticulo).update(revisor=userid,fechaasignadorevisor=fecha)
        
        return JsonResponse({"instance": "Éxito"}, status=200)
    else:
            # some form errors occured.
        return JsonResponse({"error": ""}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

@login_required
def marcarrevisado(request):
    if request.method == "POST":
        revisadoup=request.POST.get("revisado",None)
        idarticulo=request.POST.get("id",None)
        notas=request.POST.get("notas",None)
        fecha=date.today()
        Articulos.objects.filter(pk=idarticulo).update(revisado=revisadoup,fecharevisado=fecha,notas=notas)
        return JsonResponse({"instance": "Éxito"}, status=200)

    else:
            # some form errors occured.
        return JsonResponse({"error": ""}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)