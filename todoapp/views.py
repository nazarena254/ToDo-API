from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

#We import the serializers module from the rest_framework package. 
# We then create MerchSerializer class that inherits from the ModelSerializer class.

# Create your views here.
"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls={
        "Delete":"/task-delete/<str:pk>/"
    }
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

"""
Below Function going to display all the tasks store in the data base.
"""
# @api_view wrapper provide some functionality: aking sure you receive Request instancesin ur view
#  & adding context to Response objects so that content negotiation can be performed.
# It also provides behaviour such as returning '405 Method Not Allowed' responses when appropriate,
# & handling any ParseError exceptions tht occur when accessing request.data with malformed input
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

"""
This Function going to display Detailed view of one perticuler task with the help of pk.
"""
@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk) #Query the database for all Tasks
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Taks deleted successfully.")
