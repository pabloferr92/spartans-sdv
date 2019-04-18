"""sistemadevendas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from descritivo.views import ler_parceiro,alterar_parceiro,criar_parceiro,remover_parceiro
from descritivo.views import ler_banco,alterar_banco,criar_banco,remover_banco

urlpatterns = [
    path('criarpaceiro/', criar_parceiro,name='criarpaceiro'),
    path('parceiros/', ler_parceiro, name='parceiros'),
    path('alterarparceiro/<int:id>', alterar_parceiro, name='alterarparceiro'),
    path('removerparceiro/<int:id>', remover_parceiro, name='removerparceiro'),
    path('criarbanco/', criar_banco,name='criarbanco'),
    path('bancos/', ler_banco, name='bancos'),
    path('alterarbanco/<int:id>', alterar_banco, name='alterarbanco'),
    path('removerbanco/<int:id>', remover_banco, name='removerbanco')

    #path('/', core),

]
