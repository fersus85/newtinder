from django.urls import path, include

from newtinder.views import UserDetailAPI

urlpatterns = [
    path('clients/create/registration/', include('dj_rest_auth.registration.urls')),
    path('client/<int:pk>/', UserDetailAPI.as_view()),
]
