from rest_framework import serializers
from .models import User, Location
from .container import location_dao, user_dao


class UserSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        if 'location' in self.initial_data:
            self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)
    
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)

        if hasattr(self, '_location'):
            location  = location_dao.get_by_name(self._location)
            user = user_dao.save_location(user.id, location)
        
        return user

    
class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'