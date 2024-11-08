from django.shortcuts import render
from rest_framework.views import APIView
from .models import Drinks,DrinksSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import mixins,generics
from rest_framework.viewsets import ViewSet,ModelViewSet



# ModelViewSet
class DrinksViewSet(ModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer


# viewset
'''
class DrinksViewSet(ViewSet):
    def list(self,request):
        drinks = Drinks.objects.all()
        serializer = DrinksSerializer(drinks, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = DrinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors)

    
    def retrieve(self,request,pk):
        try:
            drinks = Drinks.objects.get(pk=pk)
        except Drinks.DoesNotExist:  
            return Response(status=status.HTTP_404_NOT_FOUND)  
        serializer = DrinksSerializer(drinks)
        return Response(serializer.data)
    
    def update(self,request,pk):
        try:
            drinks = Drinks.objects.get(pk=pk)
        except Drinks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DrinksSerializer(drinks,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors)
    
    def destroy(self,request,pk):
        try:
            drinks = Drinks.objects.get(pk=pk)
        except Drinks.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        drinks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


# Generics
'''
class DrinksListView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
'''
'''
class DrinksDetailView(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
'''

class DrinksDetailView(generics.ListCreateAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer


'''
class DrinksDetailView(generics.RetrieveUpdateAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
'''

'''
class DrinksDetailView(generics.RetrieveDestroyAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
'''

'''
class DrinksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
'''



# Mixins (non primary based and primary based)
'''
class DrinksListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    

class DrinksDetailView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,self)
'''





# Class Based View (Non Primary Based and Primary based)
'''
class DrinksListView(APIView):
    def get(self,request):
        drinks = Drinks.objects.all()
        serializer = DrinksSerializer(drinks,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = DrinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(DrinksSerializer.errors)
    

class DrinksDetailView(APIView):
    def get_drinks(self,pk):
        try:
            return Drinks.objects.get(pk=pk)    
        except Drinks.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        drinks = self.get_drinks(pk)
        serializers = DrinksSerializer(drinks)
        return Response(serializers.data)
    
    def delete(self,request,pk):
        drinks = self.get_drinks(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,pk):
        drinks = self.get_drinks(pk)
        serializer = DrinksSerializer(drinks,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(DrinksSerializer.errors)

'''        