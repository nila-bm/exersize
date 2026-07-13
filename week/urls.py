from django.urls import path
from . import views

urlpatterns = [
    path('<week_id>/',views.weekly),
]
