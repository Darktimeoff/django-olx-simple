from django.http import HttpRequest, JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.decorators import api_view

from .container import ads_dao, categories_dao
from .serializers import (AdListSerializer, CategoryListSerializer,
                          CreateAdSerializer, CreateCategorySerializer,
                          DeleteAdSerializer, DeleteCategorySerializer,
                          DetailAdSerializer, DetailCategorySerializer,
                          UpdateAdSerializer, UpdateCategorySerializer)


def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})

@api_view(['POST'])
def upload_image(request: HttpRequest, pk: int) -> JsonResponse:
    image = request.FILES.get('image', None)
    print('upload_image', image)
    if not image:
        return JsonResponse({"status": "error", "message": "No image"})
    
    try:
        ad = ads_dao.save_image(pk, image)

        return JsonResponse(DetailAdSerializer(ad).data)
    except ads_dao.DoesNotExistError():
        return JsonResponse({"status": "error", "message": "Ad does not exist"})




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

    