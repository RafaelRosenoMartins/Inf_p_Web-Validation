from django.urls import path
from .views import cadastrar_usuario
from .views import sucesso

urlpatterns =[
    path('', cadastrar_usuario, name='cadastrar_usuario'),
    path('sucesso/', sucesso, name='sucesso'), 
]