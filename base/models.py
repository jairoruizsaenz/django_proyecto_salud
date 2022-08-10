from django.db import models

class Punto_Salud(models.Model):
    
    departamento = models.CharField(null=False, default='', max_length=255)
    municipio = models.CharField(null=False, default='', max_length=255)
    direccion = models.CharField(verbose_name='Dirección',null=False, default='', max_length=255)
    longitud = models.CharField(null=False, default='', max_length=255)
    latitud = models.CharField(null=False, default='', max_length=255)
    
    SI_NO_CHOICES =(('Sí', 'Sí'), ('No', 'No'))
    es_IPS = models.CharField(verbose_name='¿Esta sede pertenecerá o será una IPS?', choices=SI_NO_CHOICES, max_length=2, default='-')
    
    NATURALEZA_JURIDICA_CHOICES =(('Pública', 'Pública'), ('Privada', 'Privada'), ('Mixta', 'Mixta'))
    naturaleza_juridica = models.CharField(verbose_name='Naturaleza jurídica de la IPS', choices=NATURALEZA_JURIDICA_CHOICES, max_length=7, default='-')
    
    NIVEL_ATENCION_CHOICES =(('Primer nivel', 'Primer nivel'), ('Segundo nivel', 'Segundo nivel'), ('Tercer nivel', 'Tercer nivel'))
    nivel_atencion = models.CharField(verbose_name='Nivel de atención (Si es pública)', choices=NIVEL_ATENCION_CHOICES, max_length=13, default='-')

    ENTIDAD_TERRITORIAL_CHOICES =(('Municipal', 'Municipal'), ('Departamental', 'Departamental'))
    entidad_territorial = models.CharField(verbose_name='Entidad territorial a la que pertenece', choices=ENTIDAD_TERRITORIAL_CHOICES, max_length=13, default='-')

    TIPO_SERVICIOS_CHOICES =(('Primario', 'Primario'), ('Complementario', 'Complementario'))
    tipo_servicios = models.CharField(verbose_name='Tipo de servicios', choices=TIPO_SERVICIOS_CHOICES, max_length=14, default='-')

    # def save(self, *args, **kwargs):
    #     try:
    #         this = Doc_Template.objects.get(id=self.id)
    #         if this.template != self.template:
    #             this.template.delete(save=False)
    #     except: pass
    #     super(Doc_Template, self).save(*args, **kwargs)

    # def __str__(self):
    #     return str(self.pk)


class Departamento(models.Model):    
    divipola = models.CharField(max_length=2, unique=True)
    nombre = models.CharField(null=False, default='', max_length=255)
    
    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    divipola = models.CharField(max_length=5, unique=True)
    nombre = models.CharField(null=False, default='', max_length=255)
    
    def __str__(self):
        return f"{self.nombre} ({self.departamento.nombre})"