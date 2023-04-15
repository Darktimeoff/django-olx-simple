from django.db.models import Model
from django.db.models.manager import BaseManager
from ads.models import Category, Ad, User, Location

class Dao:
    query: BaseManager[Model]

    def __init__(self, model, ordering=None):
        self.query = model.objects.all()
        if ordering:
            self.query = self.query.order_by(ordering)
        

    def get_all(self):
        return self.query.all()
    
    def get_by_id(self, id: int):
        """raise DoesNotExist exception if not found"""
        return self.query.get(pk=id)
    

class CategoriesDao(Dao):
    def __init__(self):
        super().__init__(Category)

class AdsDao(Dao):
    def __init__(self):
        super().__init__(Ad)

    def DoesNotExistError(self):
        return Ad.DoesNotExist

    def get_all(self):
        return super().get_all().select_related('category', 'author')
    
    def save_image(self, id: int, image):
        ad: Ad = self.get_by_id(id)

        ad.image = image
        ad.save()

        return ad
    
class UserDao(Dao):
    def __init__(self, ordering=None):
        super().__init__(User, ordering)

    def get_all(self):
        return super().get_all().select_related('location')
    
    def save_location(self, id: int, location: Location):
        user: User = self.get_by_id(id)

        user.location = location
        user.save()

        return user
    
class LocationDao(Dao):
    def __init__(self):
        super().__init__(Location)

    def get_by_name(self, name: str):
        return self.query.get(name=name)