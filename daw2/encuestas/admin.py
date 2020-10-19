from django.contrib import admin
from .models import Pregunta
from .models import Categoria
from .models import Usuario
from .models import Opcion

# Register your models here.
admin.site.register(Pregunta)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Opcion)