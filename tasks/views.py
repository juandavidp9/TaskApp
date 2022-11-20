from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks import serializers
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def getTask(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

    
@api_view(['POST'])
def postTask(request):
    data = request.data
    task = Task.objects.create(
        description = data['description'],
        date = data['date_limited'],
        prioridad = data['prioridad']
    )
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def putTask(request, pk):
    data= request.data
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task eliminated')