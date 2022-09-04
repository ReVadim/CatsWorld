from django.urls import path, include
from .views import detail, RegisterPetView


app_name = 'src.cats'
urlpatterns = [
    path('pets/', detail, name='detail'),
    path('pets/add/', RegisterPetView.as_view(), name='register_pet')
]
