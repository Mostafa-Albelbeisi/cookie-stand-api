from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStands
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandsSerializer


class CookieStandsList(ListCreateAPIView):
    queryset = CookieStands.objects.all()
    serializer_class = CookieStandsSerializer


class CookieStandsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStands.objects.all()
    serializer_class = CookieStandsSerializer
