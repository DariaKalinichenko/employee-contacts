from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Client, Employee, DateContact
from .serializers import ClientSerializer, EmployeeSerializer, ContactSerializer


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def retrieve(self, request, pk=None):
        queryset = Client.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ClientSerializer(user)
        return Response(serializer.data)




class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ContactView(viewsets.ModelViewSet):
    queryset = DateContact.objects.all()
    serializer_class = ContactSerializer