from django.contrib.auth import get_user_model
from rest_framework import generics


from .serializers import UserListSerializer


class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserListSerializer
    queryset = get_user_model().objects.all()

