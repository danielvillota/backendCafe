from django.urls import path
from .views import cafeView

urlpatterns = [path('miproyecto',cafeView.as_view(), name="Lista cafe")]