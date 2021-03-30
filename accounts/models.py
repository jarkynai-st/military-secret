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
