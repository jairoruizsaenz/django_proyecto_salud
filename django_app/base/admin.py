from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Departamento

class MunicipioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Municipio

class ManzanaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Manzana

class DimensionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Dimension
    
class IndicadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Indicador

class RegistroIndiceDepartamentalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = RegistroIndiceDepartamental

class RegistroIndiceMunicipalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = RegistroIndiceMunicipal

class RegistroIndiceManzanaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = RegistroIndiceManzana

class Punto_SaludAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Punto_Salud

# admin.site.register(Question, QuestionAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Manzana, ManzanaAdmin)
admin.site.register(Dimension, DimensionAdmin)
admin.site.register(Indicador, IndicadorAdmin)
admin.site.register(RegistroIndiceDepartamental, RegistroIndiceDepartamentalAdmin)
admin.site.register(RegistroIndiceMunicipal, RegistroIndiceMunicipalAdmin)
admin.site.register(RegistroIndiceManzana, RegistroIndiceManzanaAdmin)
admin.site.register(Punto_Salud, Punto_SaludAdmin)