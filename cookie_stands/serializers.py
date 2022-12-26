from rest_framework import serializers
from .models import CookieStands


class CookieStandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookieStands
        fields = "__all__"
