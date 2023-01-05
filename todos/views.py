from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.views import APIView
from .serializers import *
from .models import *


# Create your views here.
def home(request):
    return HttpResponse("<h1>Andy Hua Todo List</h1>")


class TodoListCreate(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # def perform_create(self, serializer):
    #     serializer.save(user = self.request.user)


class TodoGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


@api_view(["GET"])
def todos_get(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def todos_add(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
