from django.urls import path


from .views import ShopAPIView

urlpatterns = [
    path('', ShopAPIView.as_view()),
]