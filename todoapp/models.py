from typing_extensions import Self
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    # A Manager is interface thru which database query operations are provided to Django models. 
    # At least one Manager exists for every model in a Django application.
    # By default, Django adds a Manager with the name objects to every Django model class. 
    # However, if you want to use objects as a field name it ok 
    objects = models.Manager()

    #__str__ is a special method of python to determine what to print when
    #  it needs to print out an instance of the Task model
    def __str__(self):
        return self.title