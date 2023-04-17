from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.http import HttpRequest
from django.db.models import Count, Q
from .models import User
from .serializers import UserSerializer, LocationDetailSerializer
from .container import user_dao, location_dao

class LocationViewSet(ModelViewSet):
    queryset = location_dao.get_all()
    serializer_class = LocationDetailSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        annotate = {
            'total_ads': Count('ads', filter=Q(ads__is_published=True), distinct=True),
        }

        self.queryset = self.queryset.annotate(**annotate)

        return super().list(request, *args, **kwargs)