from django.db.models import Model
from django.db.models.manager import BaseManager
from .models import User, Location
from typing import  Generic, TypeVar, Type, List

T = TypeVar("T")

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
    
class UserDao(Dao[User]):
    def __init__(self, ordering=None):
        super().__init__(User, ordering)

    def get_all(self):
        return super().get_all().prefetch_related('locations')
    
    def save_location(self, id: int, location: Location):
        user = self.get_by_id(id)

        user.locations.add(location)
        user.save()

        return user
    
class LocationDao(Dao[Location]):
    def __init__(self):
        super().__init__(Location)

    def get_by_name(self, name: str):
        return self.query.get(name=name)