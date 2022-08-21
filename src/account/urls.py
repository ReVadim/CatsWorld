from django.urls import path, include
from .views import (
    index,
    profile,
    RegisterUserView,
    RegisterDoneView,
    user_activate,
    CatsUserLoginView,
    AccountLogoutView,
    AccountPasswordChangeView,
    DeleteUserView,
    ChangeUserInfoView,
)

app_name = 'src.account'
urlpatterns = [
    path('accounts/', include([
        path('register/', include([
            path('activate/<str:sign>/', user_activate, name='register_activate'),
            path('done/', RegisterDoneView.as_view(), name='register_done'),
            path('', RegisterUserView.as_view(), name='register'),
        ])),
        path('login/', CatsUserLoginView.as_view(), name='login'),
        path('logout/', AccountLogoutView.as_view(), name='logout'),
        path('password/change', AccountPasswordChangeView.as_view(), name='password_change'),
        path('profile/', include([
            path('delete/', DeleteUserView.as_view(), name='profile_delete'),
            path('change/', ChangeUserInfoView.as_view(), name='profile_change'),
            path('', profile, name='profile'),
        ])),
    ])),
    path('', index, name='index'),
]
