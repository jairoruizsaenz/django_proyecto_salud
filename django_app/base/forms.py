from django import forms
from .models import Punto_Salud

class Punto_Salud_Create_Form(forms.ModelForm):
    class Meta:
        model = Punto_Salud
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Punto_Salud_Create_Form, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control form-control-sm'})