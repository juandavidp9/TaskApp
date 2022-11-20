from django.db import models
from authentication.models import CustomUser

Priorities = (
    (1, 'high'),
    (2,'medium'),
    (3,'low')   
)


class Priority(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=50, blank=True)
    date = models.DateField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, 
                                on_delete=models.DO_NOTHING,
                                default=Priorities[2])


    def __str__(self) -> str:
        return f"{self.title}, {self.user}"