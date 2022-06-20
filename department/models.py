from django.db import models


# from users.models import Deputy, Employee, Director


class Department(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class DepartmentSection(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='section')
    name = models.CharField(max_length=200)
    num_emp_per_position = models.JSONField()
    # created_at = models.DateTimeField(auto_now_add=True)
    employee_capability = models.IntegerField()

    @property
    def employee_capability(self):
        # count = 0
        # if self.num_emp_per_position:
        #     for key, value in self.num_emp_per_position.items():
        #         count += int(value)
        return self.num_emp_per_position

    @property
    def number_employee(self):
        count = self.employee.count()
        return count

    @property
    def close_stafka(self):
        dict1 = {}
        for i in self.employee.all():
            if i.type not in dict1:
                dict1[i.type] = float(i.stafka)
            else:
                dict1[i.type] = float(dict1[i.type]) + float(i.stafka)
        return dict1

    @property
    def open_position(self):
        dict_open_pos = {}
        for key, value in self.close_stafka.items():
            if key in self.employee_capability:
                dict_open_pos[key] = float(self.employee_capability[key]) - float(value)

        for key, value in self.employee_capability.items():
            if not key in dict_open_pos:
                dict_open_pos[key] = value

        return dict_open_pos

    def __str__(self):
        return self.name

from department.models import DepartmentSection
section = DepartmentSection.objects.all().first()
# section.employee_capability
