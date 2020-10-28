from django import forms
from .models import Categoria, Pregunta, User, Usuario


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

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password','first_name', 'last_name', 'email')

        widgets = {
            'username':
                forms.TextInput(attrs={'class':'form-control','autocomplete':'new-text'}),
            'password':
                forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
            'edad',
        ]

        widgets = {
            'edad': forms.NumberInput(attrs={'class':'form-control'}),
        }