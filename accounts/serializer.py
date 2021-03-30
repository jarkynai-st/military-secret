from django.core.mail import EmailMessage
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *

class DossierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dossier
        fields = ['id','image','full_name','address',
                  'department','date_birth','phone','experience']


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    dossier = DossierSerializer()
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password','dossier']

    def create(self, validated_data):
        dossier = validated_data.pop('dossier')
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if confirm_password == password:
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.is_active = False
            user.save()
            subject = 'New user'
            body = f"Now user with username: {user.username} and selected departament: {dossier['department']}"
            to_list = []
            super_list = User.objects.filter(is_superuser=True)
            for super in super_list:
                to_list.append(super.email)
            email = EmailMessage(subject=subject,body=body,to=to_list)
            email.send()
            Dossier.objects.create(user=user,**dossier)
            return user
        else:
            raise ValidationError("Passwords don't match!")