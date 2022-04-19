from django.shortcuts import render

# Create your views here.
from .models import Glosario
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
