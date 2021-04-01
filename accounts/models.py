from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Dossier(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,related_name='dossier')
    image = models.ImageField(blank=True,null=True)
    full_name = models.CharField(max_length=50)
    phone = PhoneNumberField()
    address = models.CharField(max_length=200)
    department = models.CharField(choices=(
        ('SF','security_forces'),
        ('AF','air_forces'),
        ('SpF','space_force'),
        ('MF','marine_forces')
    ),max_length=20)
    experience = models.PositiveIntegerField(default=0)
    date_birth = models.DateField()
    date_join = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name + '' + self.department


class Car(models.Model):
    car_model = models.CharField(max_length=20)
    year = models.IntegerField()
    country = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    mark = models.CharField(max_length=15)
    wheel_type = models.CharField(choices=(
        ('RH','right_hand'),
        ('LH','left_hand')
    ),max_length=10)
    car_type = models.CharField(choices=(
        ('private','private'),
        ('service','service')
    ),max_length=10)
    car_number = models.IntegerField()
    dossier = models.ForeignKey(Dossier,on_delete=models.CASCADE,blank=True,null=True,related_name='cars')