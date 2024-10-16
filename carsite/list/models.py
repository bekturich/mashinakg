from django.db import models
from django.contrib.auth.models import User
from django.db.models import PositiveSmallIntegerField, DecimalField
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    country = models.CharField(max_length=33)
    age = models.IntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(region='KG', blank=True)


class Category(models.Model):
    category_name = models.CharField(max_length=33, unique=True)

    def str(self):
        return f'{self.category_name}'


class CarMake(models.Model):
    car_make_name = models.CharField(max_length=33, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def str(self):
        return f'{self.car_make_name}'


class Model(models.Model):
    model_name = models.CharField(max_length=33, unique=True)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def str(self):
        return f'{self.car_make} - {self.model_name}'


class Contact(models.Model):
    city = models.CharField(max_length=33)
    country = models.CharField(verbose_name='Страна', max_length=33)
    number = PhoneNumberField(region='KG', blank=True)

    def __str__(self):
        return f"{self.country} - {self.number}"


class Car(models.Model):
    car_name = models.CharField(max_length=33)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Car_Make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.ForeignKey(Contact, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    add_date = models.DateField(verbose_name='Время', auto_now_add=True)
    mileage = models.PositiveSmallIntegerField(verbose_name='Пробег', default=0)
    image = models.ImageField(upload_to='машины/', blank=True, null=True)
    with_photo = models.BooleanField(default=True)
    color = models.CharField(max_length=33)
    CHOICES_DRIVE = (
        ("задний", "ЗАДНИЙ"),
        ("передний", "ПЕРЕДНИЙ"),
        ("полный", "ПОЛНЫЙ"),
    )
    drive = models.CharField(verbose_name='Привод', max_length=33, choices=CHOICES_DRIVE)
    CHOICES_ENGINE = (
        ("бензин", "БЕНЗИН"),
        ("газ", "ГАЗ"),
        ("дизель", "ДИЗЕЛЬ"),
        ("электро", "ЭЛЕКТРО"),
        ("гибрид", "ГИБРИД"),
    )
    engine = models.CharField(verbose_name='Топливо', max_length=33, choices=CHOICES_ENGINE)
    CHOICES_TRANSMISSION = (
        ("механика", "МЕХАНИКА"),
        ("автомат", "АВТОМАТ"),
        ("вариатор", "ВАРИАТОР"),
        ("робот", "РОБОТ"),
    )
    transmission = models.CharField(verbose_name='Коробка', max_length=33, choices=CHOICES_TRANSMISSION)
    volume = models.FloatField(default=0.8)

    CHOICES_RUDDER = (
        ("справа", "Справа"),
        ("слева", "Слева")
    )
    rudder = models.CharField(verbose_name='руль', max_length=33, choices=CHOICES_RUDDER)
    CHOICES_STATE = (
        ("хорошее", "Хорошее"),
        ("идеальное", "Идеальное"),
        ("аварийное", "Аварийное"),
        ("новое", "Новое",)
    )
    state = models.CharField(verbose_name='состояние', max_length=33, choices=CHOICES_STATE)

    def str(self):
        return f'{self.car_name}'


class Comment(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.author} - {self.car}'


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class FavoriteCar(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart} - {self.car}'
