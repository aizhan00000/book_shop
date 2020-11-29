from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryDetailView,

)

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
]