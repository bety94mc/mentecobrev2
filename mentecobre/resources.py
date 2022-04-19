 #resources.py  from import_export import resources  
 from .models import Glosario
 class GlosarioResource(resources.ModelResource):  
   class Meta:  
     model = Glosario  