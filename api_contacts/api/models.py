from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО клиента')
    age = models.IntegerField(verbose_name='Возраст')
    address = models.CharField(max_length=200, verbose_name='Адрес проживания')

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО сотрудника')
    position = models.CharField(max_length=100, verbose_name='Должность сотрудника')
    client = models.ManyToManyField(
        Client,
        through='DateContact')

    def __str__(self):
        return self.name


class DateContact(models.Model):
    date = models.DateTimeField(verbose_name='Дата контактирования')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 related_name='employee')
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               related_name='client')
