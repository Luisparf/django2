from django.urls import path
from .views import contato, produto, index

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'), #rota na url, view, nome da view
    path('produto/', produto, name='produto'),
]
