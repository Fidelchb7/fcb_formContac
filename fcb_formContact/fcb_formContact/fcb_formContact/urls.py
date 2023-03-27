from django.contrib import admin
from django.urls import path
from fcb_formContact.views import inicio, contacto
#from fcb_ContacFormApp.views import crearLibro

urlpatterns = [
   path('admin/', admin.site.urls),
    path('', inicio),
    path('contacto/', contacto),
  #  path('clibro/', crearLibro),
]
