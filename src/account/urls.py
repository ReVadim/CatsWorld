from django.urls import path
from .views import (
    index,
    RegisterUserView,
    RegisterDoneView,
    user_activate,
    CatsUserLoginView,
)

app_name = 'src.account'
urlpatterns = [
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', CatsUserLoginView.as_view(), name='login'),
    path('', index, name='index'),
]
