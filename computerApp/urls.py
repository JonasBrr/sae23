from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machines/',views.machine_list_view, name='machines'),
    path('machine/<pk>',views.machine_detail_view,name='machine-detail'),
    path('persos/',views.personnel_list_view, name='persos'),
    path('perso/<pk>',views.personnel_detail_view,name='perso-detail'),
    path('add-machine',views.machine_add_form,name='add-machine'),
]