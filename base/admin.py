from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
    
    
class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Departamento

class MunicipioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Municipio

# admin.site.register(Question, QuestionAdmin)
admin.site.register(Punto_Salud)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)