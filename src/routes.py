from django.urls import path, include


urlpatterns = [
    path('', include('src.account.urls')),
    path('cats/', include('src.cats.urls')),
]
