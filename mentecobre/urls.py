from django.urls import path, include
from . import views


urlpatterns = [ path('', views.portada, name='portada'),
                path ('glosario', views.glosario, name='glosario'),
                
                path('traducciones', views.traducciones, name='traducciones'),
                path('asignartraducciones', views.asignartraducciones, name='asignartraducciones'),
                path('marcartraducido', views.marcartraducido, name='marcartraducido'),

                path('revisiones', views.revisiones, name='revisiones'),
                path('asignarrevisiones', views.asignarrevisiones, name='asignarrevisiones'),
                path('marcarrevisado', views.marcarrevisado, name='marcarrevisado'),
                
]