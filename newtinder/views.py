from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import BadHeaderError
from rest_framework import generics, status, mixins, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config import settings
from .filters import UserFilter
from .serializers import UserListSerializer


class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserListSerializer
    queryset = get_user_model().objects.all()


def send_sympathy(recipient, name, email):
    try:
        send_mail(
            subject='Новая симпатия', recipient_list=[recipient],
            from_email=settings.DEFAULT_FROM_EMAIL,
            message='Вы понравились пользователю {email}'.format(email=email),
            fail_silently=False
        )
    except BadHeaderError as error:
        raise BadHeaderError(f'Email не отправлен {error}')


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_match(request, user_id):
    user = request.user
    like = get_object_or_404(get_user_model(), id=user_id)
    if like in user.like.all():
        return Response({'Предупреждение': 'вы уже лайкнули этого пользователя'})
    user.like.set(get_user_model().objects.filter(id=user_id))
    likes = like.like.all()
    if user not in likes:
        return Response(status=status.HTTP_200_OK)
    name_user = user.first_name
    email_user = user.email
    name_matching = like.first_name
    email_matching = like.email
    send_sympathy(email_matching, name_user, email_user)
    send_sympathy(email_user, name_matching, email_matching)
    data = {'Email вашего совпадения': email_matching}
    return Response(data, status=status.HTTP_200_OK)


class UserListAPI(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserListSerializer
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = (UserFilter,)
    filterset_fields = ('gender', 'first_name', 'last_name')
