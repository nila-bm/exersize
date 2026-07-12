from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index),
    path('archive/',views.index_archive),
    path('new_ticket/',views.index_ticket),
]
