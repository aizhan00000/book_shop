from rest_framework import serializers
from .models import Bookss


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookss
        fields = (
            'category', 'name', 'image', 'description', 'price',
            'available', 'created', 'updated',
        )



