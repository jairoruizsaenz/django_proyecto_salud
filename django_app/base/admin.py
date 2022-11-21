from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Departamento

class MunicipioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Municipio

class DimensionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Dimension
    
class IndicadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Indicador

class RegistroIndiceMunicipalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = RegistroIndiceMunicipal

class RegistroIndiceDepartamentalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = RegistroIndiceDepartamental

class Punto_SaludAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Punto_Salud

# admin.site.register(Question, QuestionAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Dimension, DimensionAdmin)
admin.site.register(Indicador, IndicadorAdmin)
admin.site.register(RegistroIndiceMunicipal, RegistroIndiceMunicipalAdmin)
admin.site.register(RegistroIndiceDepartamental, RegistroIndiceDepartamentalAdmin)
admin.site.register(Punto_Salud, Punto_SaludAdmin)