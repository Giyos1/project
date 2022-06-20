from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Deputy, Director, Employee


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class DeputySerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Deputy
        fields = '__all__'


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
