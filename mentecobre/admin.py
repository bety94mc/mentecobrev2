from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.utils.safestring import mark_safe

from .models import Glosario, Usuario, Articulos
from .forms import UsuarioActualizarForm, RegistroForm

from import_export.admin import ImportExportModelAdmin, ExportActionMixin, ExportMixin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter, SimpleDropdownFilter
)
from django.urls import path, reverse

import csv
from django.http import HttpResponse
from import_export import resources
from import_export.signals import post_export

from django.contrib.auth.admin import UserAdmin, UserAdmin


class GlosarioResource(resources.ModelResource):  
    class Meta:  
        model = Glosario  


# Register your models here.

@admin.register(LogEntry)
class LogEntryAdmin(ExportMixin, admin.ModelAdmin):
    date_hierarchy = 'action_time'
    readonly_fields = [ 'user','content_type','object_id','object_repr','action_flag','change_message']
    list_filter = ['user', 'content_type']
    search_fields = ['object_repr', 'change_message']
    list_display = ['__str__', 'content_type', 'action_time', 'user', 'object_link']

    # keep only view permission
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = obj.object_repr
        else:
            ct = obj.content_type
            try:
                link = mark_safe('<a href="%s">%s</a>' % (
                                 reverse('admin:%s_%s_change' % (ct.app_label, ct.model),
                                         args=[obj.object_id]),
                                 escape(obj.object_repr),
                ))
            except NoReverseMatch:
                link = obj.object_repr
        return link
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = 'object'

    def queryset(self, request):
        return super(LogEntryAdmin, self).queryset(request) \
            .prefetch_related('content_type')




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
    list_display =('id','tituloEn','tituloEs','traductor', 'traducido','revisor','universo','prioridad','enlacecopperen')
    search_fields = ('tituloEn','tituloEs','universo')
    list_filter = (('traductor', RelatedDropdownFilter),('traducido',ChoiceDropdownFilter),('revisor',RelatedDropdownFilter), ('traducido',ChoiceDropdownFilter),('revisado',ChoiceDropdownFilter),('universo',ChoiceDropdownFilter),('prioridad',ChoiceDropdownFilter),'enlacecopperen', )

admin.site.site_header= "Nave Nodriza"
admin.site.site_title= "Mandos Nave Nodriza"