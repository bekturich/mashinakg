from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'phone_number', 'age']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

<<<<<<< HEAD
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']
=======
>>>>>>> b0e9459585686b4d6deb42d662de8d1152aca38b

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
<<<<<<< HEAD
        fields = ['car_make_name']
=======
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
>>>>>>> b0e9459585686b4d6deb42d662de8d1152aca38b


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['model_name']


class CarSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    Car_Make = CarMakeSerializer()
    model = ModelSerializer()
    class Meta:
        model = Car
        fields = ['car_name', 'category', 'Car_Make', 'model', 'description', 'price', 'year', 'add_date', 'mileage',
                  'image', 'with_photo', 'color', 'drive', 'engine', 'transmission', 'volume', 'rudder', 'state']

class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car_name', 'price', 'image', 'year']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCar
        fields = '__all__'
