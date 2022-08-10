"""etudiants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.EtudiantsView.as_view(), name='etudiants'),
    # path('etudiants/', views.EtudiantsView.as_view(), name='etudiants'),
    path('etudiant/', views.etudiant, name='etudiant'),
    path('etudiant/<int:id>', views.etudiant, name='etudiant'),
    path('parent/', views.display_base, name='parent'),
    path('child/', views.display_child, name='child'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('update-form/<int:id>', views.form_update, name='update-form'),
    path('update/<int:id>', views.update, name='update'),
    path('ajout-etudiant/', views.ajout_form, name='ajout-form')
    #    chemin                      vue              nom
    ]
