from django.http import HttpRequest, JsonResponse
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter

from .container import ads_dao, categories_dao
from .serializers import (AdListSerializer, CategoryListSerializer,
                          CreateAdSerializer, CreateCategorySerializer,
                          DeleteAdSerializer, DeleteCategorySerializer,
                          DetailAdSerializer, DetailCategorySerializer,
                          UpdateAdSerializer, UpdateCategorySerializer,
                        )


def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})

@api_view(['POST'])
def upload_image(request: HttpRequest, pk: int) -> JsonResponse:
    image = request.FILES.get('image', None)

    if not image:
        return JsonResponse({"status": "error", "message": "No image"})
    
    try:
        ad = ads_dao.save_image(pk, image)

        return JsonResponse(DetailAdSerializer(ad).data)
    except ads_dao.DoesNotExistError():
        return JsonResponse({"status": "error", "message": "Ad does not exist"})




class AdsListView(ListAPIView):
    queryset = ads_dao.get_all()
    filter_backends = [OrderingFilter]
    ordering = '-price'
    serializer_class = AdListSerializer

    def get(self, request: HttpRequest, *args, **kwargs):
        categories = request.GET.getlist('category', None)
        text = request.GET.get('text', None)
        location = request.GET.get('location', None)
        price_from  = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)

        if price_from:
            price_from = int(price_from)

        if price_to:
            price_to = int(price_to)


        if categories:
            categories = list(map(int, categories))
            self.queryset = ads_dao.get_by_categories(categories)

        if text:
            self.queryset = ads_dao.search_by_name(text)

        if location:
            self.queryset = ads_dao.get_by_location(location)

        if price_from or price_to:
            self.queryset = ads_dao.get_by_price(price_from, price_to)
        

        return super().get(request, *args, **kwargs)


class CategoriesListView(ListAPIView):
    queryset = categories_dao.get_all()
    serializer_class = CategoryListSerializer
    filter_backends = [OrderingFilter]
    ordering = 'name'


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