from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField(null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"


class Employee(AbstractUser):
    phone_number = models.CharField(max_length=25, null=True, blank=True)


class Service(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"


class Appointment(models.Model):
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.client} {self.service} {self.start_date_time} {self.employee}"


