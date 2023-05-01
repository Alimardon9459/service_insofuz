from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class Worker__ViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = Worker__Serializer


class User__ViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User__Serializer


class OrderForUser__ViewSet(ModelViewSet):
    queryset = OrderForUser.objects.all()
    serializer_class = OrderForUser__Serializer


class WorkerReport__ViewSet(ModelViewSet):
    queryset = WorkerReport.objects.all()
    serializer_class = WorkerReport__Serializer
