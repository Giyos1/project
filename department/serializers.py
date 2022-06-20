from rest_framework import serializers
from .models import Department, DepartmentSection
from users.serializers import DeputySerializers


class DepartmentSerializers(serializers.ModelSerializer):
    deputy = DeputySerializers()

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentSectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepartmentSection
        fields = '__all__'
