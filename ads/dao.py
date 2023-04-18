from django.db.models import Model
from django.db.models.manager import BaseManager
from ads.models import Category, Ad, Selection
from django.db.models import Q
from typing import TypeVar, Generic, Type

T = TypeVar('T')

class Dao(Generic[T]):
    query: BaseManager[T]

    def __init__(self, model: Type[T], ordering=None):
        self.query = model.objects.all()
        if ordering:
            self.query = self.query.order_by(ordering)
        

    def get_all(self) -> BaseManager[T]:
        return self.query.all()
    
    def get_by_id(self, id: int) -> T:
        """raise DoesNotExist exception if not found"""
        return self.query.get(pk=id)
    

class CategoriesDao(Dao[Category]):
    def __init__(self):
        super().__init__(Category)

class AdsDao(Dao[Ad]):
    def __init__(self):
        super().__init__(Ad)

    def DoesNotExistError(self):
        return Ad.DoesNotExist

    def get_all(self):
        return super().get_all().select_related('category', 'author')
    
    def get_by_categories(self, categories: list[int]):
        return self.query.filter(category_id__in=categories).select_related('category', 'author')
    
    def search_by_name(self, name: str):
        return self.query.filter(name__icontains=name).select_related('category', 'author')
    
    def get_by_location(self, location: str):
        return self.query.filter(author__location__name__icontains=location).select_related('category', 'author')
    
    def get_by_price(self, price_from: int = 0, price_to: int = 0):
        price_q = None

        if price_from and not price_to:
            price_q = Q(price__gte=price_from)

        if price_to and not price_from:
            price_q = Q(price__lte=price_to)

        if price_from and price_to:
            price_q = Q(price__gte=price_from, price__lte=price_to)

        return self.query.filter(price_q).select_related('category', 'author')

    def save_image(self, id: int, image):
        ad: Ad = self.get_by_id(id)

        ad.image = image
        ad.save()

        return ad
    
class SelectionDao(Dao[Selection]):
    def __init__(self, ordering = None):
        super().__init__(Selection, ordering)

    def get_all(self):
        return super().get_all().select_related('owner').prefetch_related('items')

    def add_items(self, id: int, items: list[int]):
        selection  = self.get_by_id(id)
        selection.items.add(*items)

        selection.save()

        return selection

    def add_item(self, id: int, item: int):
        selection  = self.get_by_id(id)
        selection.items.add(item)

        selection.save()

        return selection