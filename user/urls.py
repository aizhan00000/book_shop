from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


app_name = 'orders'

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('register/', views.register),
    path('login/', views.log_in),
    path('register/', views.register),
    path('change_pass/', views.change_password),
]


