from rest_framework import serializers
from ads.models import Ad, Category

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
