from django.urls import include, path

from endereco.views import DetailEndereco, ListEndereco

urlpatterns = [
    path('', ListEndereco.as_view()),
    path('<str:cep>', DetailEndereco.as_view())
]