from django.http import HttpRequest, JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .container import ads_dao, categories_dao
from .serializers import (AdListSerializer, CategoryListSerializer,
                          CreateAdSerializer, CreateCategorySerializer,
                          DeleteAdSerializer, DeleteCategorySerializer,
                          DetailAdSerializer, DetailCategorySerializer,
                          UpdateAdSerializer, UpdateCategorySerializer)


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
    lookup_field = 'pk'

class UpdateAdView(UpdateAPIView):
    queryset = ads_dao.get_all()
    serializer_class = UpdateAdSerializer
    lookup_field = 'pk'


class UpdateCategoryView(UpdateAPIView):
    queryset = categories_dao.get_all()
    serializer_class = UpdateCategorySerializer
    lookup_field = 'pk'


class DeleteAdView(DestroyAPIView):
    queryset = ads_dao.get_all()
    serializer_class = DeleteAdSerializer
    lookup_field = 'pk'


class DeleteCategoryView(DestroyAPIView):
    queryset = categories_dao.get_all()
    serializer_class = DeleteCategorySerializer
    lookup_field = 'pk'

    