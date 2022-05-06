from django.contrib import admin
from django.urls import include, path

from endereco.views import ListEndereco


urlpatterns = [
    path('admin/', admin.site.urls),
    path('endereco/', ListEndereco.as_view())
]
