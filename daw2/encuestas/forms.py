from django import forms
from .models import Categoria, Pregunta


class CategoriaForm(forms.ModelForm):


    class Meta:
        model = Categoria

        fields = [
            'categoria_text',
        ]

        labels = {
            'categoria_text': 'Categoría',
        }
        
        widgets = {
            'categoria_text': forms.TextInput(attrs={'class':'form-control'}),
        }

class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta

        fields = [
            'pregunta_text',
            'categoria',
        ]
        labels = {
            'pregunta_text': 'Pregunta',
            'categoria': 'Categoría',
        }
        widgets = {
            'pregunta_text': forms.TextInput(attrs={'class':'form-control'}),
            # 'categoria': forms.CheckboxSelectMultiple(attrs={'class':''}),
            'categoria': forms.SelectMultiple(attrs={'size':'5','class':'formcontrol','required':'True'}),
        }