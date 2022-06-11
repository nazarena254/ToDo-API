from rest_framework import serializers
from .models import Task

# A serializer is a component that will convert Django models to JSON objects and vice-versa
# The ModelSerializer class provides a shortcut that lets you automatically create 
# a Serializer class with fields that correspond to the Model fields
class TaskSerializer(serializers.ModelSerializer):
    class  Meta:
        model: Task
        fields='__all__'
