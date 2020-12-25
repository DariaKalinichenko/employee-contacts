from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework_csv.renderers import CSVRenderer

from .models import Client, Employee, DateContact, Filter
from .serializers import ClientSerializer, EmployeeSerializer, ContactSerializer, ContactCSVSerializer


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ContactView(viewsets.ModelViewSet):
    queryset = DateContact.objects.all()
    serializer_class = ContactSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = Filter


class CSVRenderView(viewsets.ModelViewSet):
    renderer_classes = [CSVRenderer]
    queryset = DateContact.objects.all()
    serializer_class = ContactCSVSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = Filter
