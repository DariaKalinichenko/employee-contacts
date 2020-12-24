from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Client, Employee, DateContact


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Client


class EmployeeSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.name')

    class Meta:
        fields = '__all__'
        read_only_fields = ('client', )
        model = Employee


class ContactSerializer(serializers.ModelSerializer):

    def validate(self, data):
        client = data['client']
        employee = data['employee']
        date = data['date']
        contact = DateContact.objects.filter(client=client, employee=employee, date=date)
        if contact.exists():
            raise ValidationError('Вы уже создали контакт')
        return data

    class Meta:
        fields = '__all__'
        model = DateContact