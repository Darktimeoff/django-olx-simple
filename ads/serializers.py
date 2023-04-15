from rest_framework import serializers
from ads.models import Ad, Category, User
from .container import location_dao

class AdListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(
        source='author.first_name', 
        read_only=True,
    )

    author_id = serializers.IntegerField()

    category = serializers.CharField(
        source='category.name', 
        read_only=True,
    )

    category_id = serializers.IntegerField()

    class Meta:
        model = Ad
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CreateAdSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True, required=False)

    class Meta:
        model = Ad
        fields = '__all__'

class CreateCategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True, required=False)

    class Meta:
        model = Category
        fields = '__all__'

class DetailAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

class DetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UpdateCategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True, required=False)

    class Meta:
        model = Category
        fields = '__all__'

class UpdateAdSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True, required=False)

    class Meta:
        model = Ad
        fields = '__all__'

class DeleteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DeleteAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

user_exclude = ['password']
class UserSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='location.name', read_only=True)

    class Meta:
        model = User
        exclude = user_exclude
    

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        if 'location' in self.initial_data:
            self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)
    
    def create(self, validated_data):
        user = super().create(validated_data)
        print('create', user)

        if hasattr(self, '_location'):
            location  = location_dao.get_by_name(self._location)
            user.location = location
            user.save()
        
        return user
    
class UpdateUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    location = serializers.CharField(source='location.name', read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        if 'location' in self.initial_data:
            self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)
    
    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)

        if hasattr(self, '_location'):
            location  = location_dao.get_by_name(self._location)
            user.location = location
            user.save()
        
        return user