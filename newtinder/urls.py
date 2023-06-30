from django.urls import path, include


from newtinder.views import UserDetailAPI, get_match, UserListAPI

urlpatterns = [
    path('clients/create/registration/', include('dj_rest_auth.registration.urls')),
    path('client/<int:pk>/', UserDetailAPI.as_view()),
    path('clients/<int:user_id>/match/', get_match, name='get_match'),
    path('list/', UserListAPI.as_view({'get': 'list'})),
]
