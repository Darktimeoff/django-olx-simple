from django.db.models import Count, Q
from rest_framework.viewsets import ModelViewSet

from .container import location_dao
from .models import User
from .serializers import LocationDetailSerializer, UserSerializer


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
