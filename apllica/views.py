from django.http import Http404
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MyModel
from .serializers import MonModeldeSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import serializers,mixins
# class List(generics.ListCreateAPIView):
    
#     queryset = MyModel.objects.all()
#     serializer_class = MonModeldeSerializer
#     def perform_create(self, serializer):
#         serializer.save()



class Meth(generics.GenericAPIView,mixins.CreateModelMixin):
    queryset = MyModel.objects.all()
    serializer_class = MonModeldeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class ApiList(APIView):
    
    def get(self, request):  # Modified to accept the 'request' parameter
        toutRecupe = MyModel.objects.all()
        serializeur = MonModeldeSerializer(toutRecupe, many=True)
        return Response(serializeur.data)
    
    def post(self, request):
        serializeur = MonModeldeSerializer(data=request.data)
        if serializeur.is_valid():
            serializeur.save()
            return Response(serializeur.data, status=status.HTTP_201_CREATED)
        return Response(serializeur.errors, status=status.HTTP_400_BAD_REQUEST)



class ApiSimple(APIView):
    def get_object(self, pk):
        if MyModel :
            return MyModel.objects.get(pk=pk)
        
        return 'ya pas de b\d'

    def get(self, pk):
        element = self.get_object(pk)
        serializeur = MonModeldeSerializer(element)
        return Response(serializeur.data)

    def put(self, request, pk):
        element = self.get_object(pk)
        serializeur = MonModeldeSerializer(element, data=request.data)
        if serializeur.is_valid():
            serializeur.save()
            return Response(serializeur.data)
        return 'erreur de modification'

    def delete(self, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


