from rest_framework import serializers
from .models import Ad, Category, Selection
from .container import selection_dao, categories_dao

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

class SelectionSerializer(serializers.ModelSerializer):
    # items = serializers.SlugRelatedField(many=True)

    class Meta:
        model = Selection
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        if 'items' in self.initial_data:
            self._items: list[int] = self.initial_data.pop('items')

        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        selection = super().create(validated_data)

        if hasattr(self, '_items'):
            selection = selection_dao.add_items(selection.id, self._items)

        return selection

class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdListSerializer(many=True, read_only=True)
    class Meta:
        model = Selection
        fields = ['id', 'items']
    
class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id', 'name']