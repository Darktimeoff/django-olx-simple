from django.http import HttpRequest, JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from ads.container import ads_dao, categories_dao
from ads.serializers import (AdListSerializer, CategoryListSerializer,
                             CreateAdSerializer, CreateCategorySerializer,
                             DetailAdSerializer, DetailCategorySerializer)

# Create your views here.


def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})


class AdsListView(ListAPIView):
    queryset = ads_dao.get_all()
    serializer_class = AdListSerializer


class CategoriesListView(ListAPIView):
    queryset = categories_dao.get_all()
    serializer_class = CategoryListSerializer


class CreateAdView(CreateAPIView):
    queryset = ads_dao.get_all()
    serializer_class = CreateAdSerializer


class CreateCategoryView(CreateAPIView):
    queryset = categories_dao.get_all()
    serializer_class = CreateCategorySerializer


class DetailAdView(RetrieveAPIView):
    queryset = ads_dao.get_all()
    serializer_class = DetailAdSerializer

class DetailCategoryView(RetrieveAPIView):
    queryset = categories_dao.get_all()
    serializer_class = DetailCategorySerializer