from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Client, Employee, DateContact


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', 'client', )
        model = Employee


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', )
        model = Client


class ContactSerializer(serializers.ModelSerializer):

    def validate(self, data):
        client = data['client']
        employee = data['employee']
        date = data['date']
        contact = DateContact.objects.filter(employee=employee,
                                             date=date, client=client, )
        if contact.exists():
            raise ValidationError('Вы уже создали контакт')
        return data

    class Meta:
        fields = '__all__'
        model = DateContact


class ContactCSVSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        fields = ('employee', 'date', 'client', )
        model = DateContact
