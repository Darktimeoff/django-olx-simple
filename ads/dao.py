from django.db.models import Model
from django.db.models.manager import BaseManager
from ads.models import Category, Ad

class Dao:
    query: BaseManager[Model]

    def __init__(self, model):
        self.query = model.objects.all()

    def get_all(self):
        return self.query.all()
    
    def get_by_id(self, id: int):
        """raise DoesNotExist exception if not found"""
        return self.query.get(id)
    

class CategoriesDao(Dao):
    def __init__(self):
        super().__init__(Category)

class AdsDao(Dao):
    def __init__(self):
        super().__init__(Ad)

    def get_all(self):
        return super().get_all().select_related('category', 'author')