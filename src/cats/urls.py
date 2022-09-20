from django.urls import path
from .views import detail, RegisterPetView, pet_detail, ChangePetDetailView, AddPhotoToAlbumView


app_name = 'src.cats'
urlpatterns = [
    path('pets/', detail, name='detail'),
    path('pets/add/', RegisterPetView.as_view(), name='register_pet'),
    path('pets/add_photo/<int:pet_id>/', AddPhotoToAlbumView.as_view(), name='add_photo'),
    path('detail/<int:pk>/', pet_detail, name='pet_detail'),
    path('detail/change/<int:pk>/', ChangePetDetailView.as_view(), name='change_info'),
]
