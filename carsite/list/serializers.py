from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'last_name', 'first_name', 'email', 'password', 'phone_number', 'age']
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
        fields = ['first_name', 'last_name', 'age', 'phone_number']

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = ['car_make_name']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['model_name']


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car_name', 'price', 'image', 'year', 'city']


class CommentSerializer(serializers.ModelSerializer):
    car = CarListSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Comment
        fields = ['author', 'text', 'car', 'parent_review', 'created_date']

class CarSerializer(serializers.ModelSerializer):
    Car_Make = CarMakeSerializer()
    model = ModelSerializer()
    class Meta:
        model = Car
        fields = ['car_name', 'add_date', 'Car_Make', 'model', 'price',
                  'year', 'mileage', 'color', 'volume', 'transmission', 'drive', 'rudder', 'state', 'country', 'city', 'description',
                  'image', 'with_photo', 'engine']

class FavoriteSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    user = UserProfileSerializer()
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteCarSerializer(serializers.ModelSerializer):
    cart = FavoriteSerializer()
    car = CarListSerializer()
    class Meta:
        model = FavoriteCar
        fields = ['cart', 'car']
