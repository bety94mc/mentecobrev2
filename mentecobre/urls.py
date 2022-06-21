from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [ path('', views.portada, name='portada'),
                path ('glosario', views.glosario, name='glosario'),
                
                path('traducciones', views.traducciones, name='traducciones'),
                path('asignartraducciones', views.asignartraducciones, name='asignartraducciones'),
                path('marcartraducido', views.marcartraducido, name='marcartraducido'),

                path('revisiones', views.revisiones, name='revisiones'),
                path('asignarrevisiones', views.asignarrevisiones, name='asignarrevisiones'),
                path('marcarrevisado', views.marcarrevisado, name='marcarrevisado'),
                
                path('gregorio', views.gregorio, name='gregorio'),
                path('perfil', views.perfil, name='perfil'),
                path('updateuser', views.updateuser,name='updateuser'),
                
                path('categorizanator', login_required(views.CategoriaListView.as_view()),name='categorizanator')
                
]