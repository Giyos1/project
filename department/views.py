from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import DepartmentSerializers, DepartmentSectionSerializers
from .models import Department, DepartmentSection
from users.serializers import EmployeeSerializers, Employee


class DepartmentView(generics.GenericAPIView):
    serializer_class = DepartmentSerializers
    queryset = Department.objects.all()

    def get(self, request):
        department = Department.objects.all()
        serializers = self.serializer_class(instance=department, many=True)

        return Response(data=serializers.data, status=status.HTTP_200_OK)


class DepartmentSectionView(generics.RetrieveAPIView):
    serializer_class = DepartmentSectionSerializers
    queryset = Department.objects.all()

    def get(self, request, pk):
        department = Department.objects.get(id=pk)
        departmentsection = DepartmentSection.objects.filter(department=department)

        serializers = self.serializer_class(instance=departmentsection, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)


class DepartmentSectionEmployeeView(generics.ListAPIView):
    serializer_class = EmployeeSerializers
    queryset = Employee.objects.all()

    def get(self, request, pk, id):
        department = Department.objects.get(id=pk)
        departmentsection = DepartmentSection.objects.filter(department=department)
        section = departmentsection.get(id=id)
        employees = Employee.objects.filter(section=section)

        serializers = self.serializer_class(instance=employees, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
