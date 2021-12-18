from authentication.models import*
from rest_framework import serializers
from django.contrib.auth.models import User
from authentication.models import user

class Userserializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')

class userserializer (serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('user','credits','ssn','address','tax_no')
