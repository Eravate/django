# Generated by Django 3.1.1 on 2020-10-05 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_text', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['categoria_text'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.SmallIntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_text', models.CharField(max_length=200)),
                ('fecha_pub', models.DateTimeField(verbose_name='Fecha de Publicación')),
                ('categoria', models.ManyToManyField(blank=True, related_name='pregunta', to='encuestas.Categoria')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.usuario')),
            ],
            options={
                'ordering': ['fecha_pub', 'pregunta_text'],
            },
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion_text', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.pregunta')),
            ],
            options={
                'ordering': ['opcion_text'],
            },
        ),
    ]
