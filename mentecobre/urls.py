from django.urls import path, include
from . import views


urlpatterns = [ path ('glosario', views.glosario, name='glosario'),

                
]