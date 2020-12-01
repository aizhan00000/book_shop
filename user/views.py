from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated  # типы прав
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# используйте декоратор @permission_classes() для ограничения обределенной классификации пользователей к функциям
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username, password = [request.data.get(key) for key in ['username', 'password']]
    if User.objects.filter(username=username).exists():
        return Response('пользователь с таким логином уже существует')
    user = User.objects.create(username=username,
                               email='asds@asdasd/asd',
                               password=password)
    user.save()

    token = Token.objects.create(user=user)
    return Response(token.key, 200)


@api_view(['POST'])
@permission_classes([AllowAny])
def log_in(request):
    username, password = [request.data.get(key) for key in ['username', 'password']]
    user = authenticate(username=username, password=password)

    # если необходимо обновлять токен при каждом входе

    # token = Token.objects.get(user=user)
    # token.key = token.generate_key()
    # token.save()

    login(request=request, user=user)
    return Response('login success', 200)


@api_view(['POST'])
@permission_classes([AllowAny])
def change_password(request):
    username, password, new_password = [request.data.get(key) for key in ['username', 'password', 'new_password']]
    user = authenticate(username=username, password=password)
    user.set_password(new_password)
    user.save()
    return Response('change success', 200)


