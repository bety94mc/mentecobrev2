from django.shortcuts import render

# Create your views here.
from .models import Glosario, Articulos, Usuario, Categoria
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from datetime import date

import pandas as pd

@xframe_options_exempt
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
    
@xframe_options_exempt
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
    prioridadexcluida=[4,5]
    tipoexcluida=['RD','DIS']
    for universo_item in universo:
        

        articulo = Articulos.objects.filter(universo=universo_item).filter(traducido__isnull=True).filter(traductor__isnull=True).exclude(prioridad__in=prioridadexcluida).exclude(tipo__in=tipoexcluida).order_by('prioridad','tituloEn').first()

        if articulo != None:
            print(articulo)
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
    prioridadexcluida=[4,5]
    tipoexcluida=['RD']
    for universo_item in universo:

        articulo = Articulos.objects.filter(universo=universo_item).filter(traducido__isnull=False).filter(revisado__isnull=True).filter(revisor__isnull=True).exclude(prioridad__in=prioridadexcluida).exclude(tipo__in=tipoexcluida).order_by('prioridad','tituloEn').first()

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
        enlacecopperencheck=request.POST.get("checked")
        if enlacecopperencheck == 'true':
            enlacecopperencheck = True
        else:
            enlacecopperencheck = False
        fecha=date.today()
        Articulos.objects.filter(pk=idarticulo).update(revisado=revisadoup,fecharevisado=fecha,notas=notas,enlacecopperen=enlacecopperencheck)
        return JsonResponse({"instance": "Éxito"}, status=200)

    else:
            # some form errors occured.
        return JsonResponse({"error": ""}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

@login_required
def gregorio(request):
    if request.user.is_superuser:
        lista_usuarios = Usuario.objects.exclude(is_active=False)
        hoy=date.today()
        usuario_saa=[]
        articulosinfechaasignado=[]
        traducido=['F','Y']
        tabla=pd.DataFrame(columns=['userid','user','universo','artiasignado','artitraducido','fechaasignado','fechatraducido','diaspasados','estado'])
        for user in lista_usuarios:
            #Fecha último artículo asignado
            
            ultimoarticuloasignado=Articulos.objects.filter(traductor=user.id).order_by('-fechaasignado').first()
            ultimoarticulotraducido=Articulos.objects.filter(traductor=user.id,traducido__in=traducido).order_by('-fechatraducido').first()
            numeroarticuloasignado=Articulos.objects.filter(traductor=user.id).count()
            numeroarticulotraducido=Articulos.objects.filter(traductor=user.id,traducido__in=traducido).count()
            articuloasginadosinfechas=Articulos.objects.filter(traductor=user.id,fechaasignado__isnull=True)
            if articuloasginadosinfechas !=None:
                for articulosinfecha in articuloasginadosinfechas:
                    articulosinfechaasignado.append(articulosinfecha.tituloEs)
            if ultimoarticuloasignado != None:
                if ultimoarticuloasignado.fechaasignado != None:
                    diaspasados=(hoy-ultimoarticuloasignado.fechaasignado).days
                else:
                    diaspasados='¡Falta fecha!'
                    
                print(diaspasados)
                if diaspasados == '¡Falta fecha!':
                    estado = '\U0001F926'                    
                elif diaspasados >= 21 and diaspasados < 45:
                    estado='\U0001F917'
                elif diaspasados >= 45 and  diaspasados < 60:
                    estado='\U0001F641'
                elif diaspasados >=60 and  diaspasados < 70:
                    estado='\U0001F92C'
                elif diaspasados < 21:
                    estado='\U0001F970'
                else:
                    estado='\U0001F480'
                
                if ultimoarticulotraducido == None:
                    tabla_dict=pd.DataFrame([{'userid':user.id,'user':user.username,'universo':user.universo,'artiasignado':numeroarticuloasignado,'artitraducido':numeroarticulotraducido,'fechaasignado':ultimoarticuloasignado.fechaasignado,'fechatraducido':None,'diaspasados':diaspasados,'estado':estado}])
                else:
                    tabla_dict=pd.DataFrame([{'userid':user.id,'user':user.username,'universo':user.universo,'artiasignado':numeroarticuloasignado,'artitraducido':numeroarticulotraducido,'fechaasignado':ultimoarticuloasignado.fechaasignado,'fechatraducido':ultimoarticulotraducido.fechatraducido,'diaspasados':diaspasados,'estado':estado}])
                tabla=pd.concat([tabla,tabla_dict],ignore_index = True, axis = 0)
            else:
                
                usuario_saa.append(user)
                
            print (articulosinfechaasignado)
            # if len(articulosinfechaasignado) > 0 :
                # messages.add_message(request, messages.INFO, 'Parece que alguien se ha olvidado de algo... No sé... En ciertos artículos...')
                

        return render(
            request,
            'gregorio.html',
            context={'resumenusuarios':tabla, 'usuarios_saa':usuario_saa, 'articulosinfechaasignado':articulosinfechaasignado},
        )



@require_http_methods(["GET", "POST"])
def perfil(request):
    # request should be ajax and method should be POST.
    if request.method == "POST":
        userid=request.POST.get("id",None)
        user=Usuario.objects.filter(id=userid)
        print(user)
        ser_user = serializers.serialize('json', user)
        print(ser_user) 
        
        articulos_asignados=Articulos.objects.filter(traductor=userid).order_by('-fechaasignado')
        ser_articulos = serializers.serialize('json', articulos_asignados)
        print(articulos_asignados)
        print(ser_articulos)
        return JsonResponse({"usuario": ser_user, "articulos":ser_articulos}, status=200)
        
    if request.method == "GET":
        userid = request.user.id
        user=Usuario.objects.filter(id=userid)
        print(user)
        articulos_asignados=Articulos.objects.filter(traductor=userid).order_by('-fechaasignado')
        
        return render(
            request,
            'perfil.html',
            context={"usuario": user, "articulos":articulos_asignados},
        )
        

    return JsonResponse({"error": ""}, status=400)


@login_required
def updateuser(request):
    if request.method == "POST":
        username=request.POST.get("username",None)
        notas=request.POST.get("notas",None)
        print(notas)
        Usuario.objects.filter(username=username).update(notas=notas)
        return JsonResponse({"instance": "Éxito"}, status=200)

    else:
            # some form errors occured.
        return JsonResponse({"error": ""}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
    

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'mentecobre/categoria.html'
    context_object_name = 'categoria_list'