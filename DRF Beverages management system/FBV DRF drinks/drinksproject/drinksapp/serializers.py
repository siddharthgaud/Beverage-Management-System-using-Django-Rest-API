from rest_framework import serializers
from .models import Drinks


# class DrinksSerializers(serializers.Serializer):
class DrinksSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200)
    # description = serializers.CharField(max_length=500)


    # def create(self,validated_data):
    #     return Drinks.objects.create(**validated_data)
    
    # def update(self,drinks,validated_data):
    #     newdrinks = Drinks(**validated_data)
    #     newdrinks.id = drinks.id
    #     newdrinks.save()
    #     return newdrinks

    class Meta:
        model = Drinks
        fields = '__all__'