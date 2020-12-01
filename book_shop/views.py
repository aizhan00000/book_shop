from rest_framework import generics, permissions
from .models import Bookss
from .serializers import ShopSerializer


class ShopAPIView(generics.ListAPIView):
    queryset = Bookss.objects.all()
    serializer_class = ShopSerializer


class ListApiShop(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Bookss.objects.all()
    serializer_class = ShopSerializer

class DetailApiShop(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Bookss.objects.all()
    serializer_class = ShopSerializer