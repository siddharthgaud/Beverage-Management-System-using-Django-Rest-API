from django.db import models
from rest_framework import serializers

class Drinks(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = '__all__' 


    


    