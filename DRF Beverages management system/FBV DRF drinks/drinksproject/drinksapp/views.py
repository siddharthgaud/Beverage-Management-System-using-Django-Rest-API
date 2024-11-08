from django.shortcuts import render
from .models import Drinks
from .serializers import DrinksSerializers
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response




# @csrf_exempt
@api_view(['GET','POST'])
def drinks_list(request):
    if request.method == 'GET':    
        drinks = Drinks.objects.all()
        serializers= DrinksSerializers(drinks,many=True)
        return Response(serializers.data)
    elif request.method == "POST":
        # jsonData = JSONParser().parse(request)
        serializers = DrinksSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response({"message": "Error"}, status=400)


# @csrf_exempt
@api_view(['GET','DELETE','PUT'])
def drinksDetailView(request,pk):
    try:
        drinks = Drinks.objects.get(pk=pk)
    except:
        return HttpResponse("Drink not found")

    if request.method == "DELETE":
       drinks.delete()
       return HttpResponse("Drink deleted")

    elif request.method == "GET":
        serializer = DrinksSerializers(drinks)
        return Response(serializer.data)

    elif request.method == "PUT":
        # jsonData = JSONParser().parse(request)
        serializers = DrinksSerializers(drinks,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response({"message": "Error"}, status=400)

