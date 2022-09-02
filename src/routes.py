from django.urls import path, include


urlpatterns = [
    # path('', include('src.cats.urls')),
    path('', include('src.account.urls')),
]
