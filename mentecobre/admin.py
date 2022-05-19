from django.contrib import admin

from .models import Glosario, Usuario, Articulos
from .forms import UsuarioActualizarForm, RegistroForm

from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter, SimpleDropdownFilter
)
from django.urls import path

import csv
from django.http import HttpResponse
from import_export import resources
from import_export.signals import post_export

from django.contrib.auth.admin import UserAdmin, UserAdmin


class GlosarioResource(resources.ModelResource):  
    class Meta:  
        model = Glosario  


# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(ImportExportModelAdmin, UserAdmin):
    form = UsuarioActualizarForm
    add_form = RegistroForm
    list_display =('id','username','rango','universo')
    fieldsets = ( (None, {'fields':('username','password','email','first_name','last_name')}),
                  ('Extra Info',{'fields':('rango','universo')}),
                  ('Permisos',{'fields':('groups','is_superuser','is_staff','is_active')}),
    )
    add_fieldsets = (
        (None, {
                'classes':('wide',),
                'fields':('username','password1','password2')}
                ),
   ) 



@admin.register(Glosario)
class GlosarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =('id','wordEn','wordEs','universo')
    list_filter = ['universo']
    search_fields = ('wordEn','wordEs')
    
    resource_class=GlosarioResource
    
@admin.register(Articulos)
class ArticulosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =('id','tituloEn','tituloEs','traductor', 'traducido','revisor','universo')
    search_fields = ('tituloEn','tituloEs','universo')
    list_filter = (('traductor', RelatedDropdownFilter),('traducido',ChoiceDropdownFilter),('revisor',RelatedDropdownFilter), ('universo',ChoiceDropdownFilter),)

admin.site.site_header= "Nave Nodriza"
admin.site.site_title= "Mandos Nave Nodriza"