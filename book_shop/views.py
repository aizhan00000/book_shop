from rest_framework import generics
from .models import Bookss
from .serializers import ShopSerializer


class ShopAPIView(generics.ListAPIView):
    queryset = Bookss.objects.all()
    serializer_class = ShopSerializer




