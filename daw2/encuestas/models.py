from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime 
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.SmallIntegerField(null=True)
    def __str__(self):
        return '{} {} años'.format(self.user,self.edad)

@receiver(post_save, sender=User)
def create_user_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_usuario(sender, instance, **kwargs):
    instance.usuario.save()

class Categoria(models.Model):
    categoria_text = models.CharField(max_length=200)
    class Meta:
        ordering = ['categoria_text']
    def __str__(self):
        return '{}'.format(self.categoria_text)

class Pregunta(models.Model):
    pregunta_text = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('Fecha de Publicación')
    categoria = models.ManyToManyField(Categoria, related_name='pregunta',blank=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    class Meta:
        ordering = ['fecha_pub','pregunta_text']
    def __str__(self):
        return '{}      (Fecha de publicación: {})'.format(self.pregunta_text,self.fecha_pub)
    def fue_publicado_recientemente(self):
        return self.fecha_pub >= timezone.now() - datetime.timedelta(days=1)

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    class Meta:
        ordering = ['opcion_text']
    def __str__(self):
        return '{}'.format(self.opcion_text)