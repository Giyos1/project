from django.contrib.auth.models import User
from department.models import Department, DepartmentSection
from django.db import models
from django.core.exceptions import ValidationError


def validate_deputy(value):
    user = User.objects.get(id=value)
    if user.is_staff and not user.is_superuser:
        return value
    else:
        raise ValidationError("This field unavailable")


def validate_director(value):
    user = User.objects.get(id=value)

    if user.is_superuser:
        return value
    else:
        raise ValidationError("This field don't have director")


class Deputy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, validators=[validate_deputy])
    department = models.OneToOneField(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Director(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, validators=[validate_director])

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    TYPE_CHOICE_POS = (
        ('LABORATORY ASSISTANT', 'Laboratory assistant'),
        ('TECHNICIAN', 'Technician'),
        ('SCIENTIST', 'Scientist'),
    )
    TYPE_CHOICE_STA = (
        (0.5, 0.5),
        (1, 1)
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ForeignKey(DepartmentSection, on_delete=models.CASCADE, related_name='employee')
    type = models.CharField(choices=TYPE_CHOICE_POS, max_length=100)
    stafka = models.FloatField(choices=TYPE_CHOICE_STA)

    # validators = [validate_staff(id=section.id)]

    def clean(self):
        open_pos = float(self.section.open_position[self.type])
        if self in Employee.objects.all():
            open_pos += self.stafka

        if not (self.type in self.section.open_position and open_pos >= self.stafka):
            raise ValidationError("don't have open position sorry !!!")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
