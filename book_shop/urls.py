from django.urls import path


from .views import ShopAPIView
from .views import ListApiShop, DetailApiShop


urlpatterns = [
    path('', ShopAPIView.as_view()),
    path('<int:pk>/', DetailApiShop.as_view()),
    path('', ListApiShop.as_view()),
]
