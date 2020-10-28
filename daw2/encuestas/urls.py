from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'encuestas'
urlpatterns = [
	path('', views.index, name='index'),
    path('<int:pregunta_id>/',views.detalle,name="detalle"),
    path('<int:pregunta_id>/resultados/',views.resultados,name="resultados"),
    path('<int:pregunta_id>/votar/',views.votar,name="votar"),
    
    path('accounts/login/',
    auth_views.LoginView.as_view(template_name='encuestas/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('categoria/',views.categoria_create_read,name='categoria'),
    path('updateCategoria/<int:categoria_id>',views.categoria_update,name='updateCategoria'),
    path('deleteCategoria/<int:categoria_id>',views.categoria_delete,name='deleteCategoria'),

    path('updatePregunta/<int:pregunta_id>', views.pregunta_update, name='updatePregunta'),
    path('deletePregunta/<int:pregunta_id>', views.pregunta_delete, name='deletePregunta'),
    path('deleteOpcion/<int:opcion_id>', views.opcion_delete, name='deleteOpcion'),

    path('usuario/',views.usuarios,name='usuarios'),
    path('updateUsuarioAjax/',views.usuario_form_ajax,name='UsuarioFormAjax'),
]

