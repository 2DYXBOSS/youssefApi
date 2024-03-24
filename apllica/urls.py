from django.contrib import admin
from django.urls import path, include
from apllica.views import Meth


urlpatterns = [
    
    path('Meth/', Meth.as_view(), name='Meth'),  # Corrected view reference
]
