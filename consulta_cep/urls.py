from django.contrib import admin
from django.urls import include, path

import endereco.urls as endereco


urlpatterns = [
    path('admin/', admin.site.urls),
    path('endereco/', include(endereco))
]
