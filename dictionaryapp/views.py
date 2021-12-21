from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from .models import Dictionary
from .serializer import DictionarySerializer

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverview(request):
    api_urls = {
        'List': '/dictionary-list/',
        'Create': '/dictionary-create/',
        'Update': '/dictionary-update/<str:pk>/',
        'Delete': '/dictionary-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def dictionaryList(request):
    dictionary = Dictionary.objects.all()
    serializer = DictionarySerializer(dictionary, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def dictionaryCreate(request):
    serializer = DictionarySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def dictionaryUpdate(request, pk):
    dictionary = Dictionary.objects.get(id=pk)
    serializer = DictionarySerializer(instance=dictionary, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def dictionaryDelete(request, pk):
    dictionary = Dictionary.objects.get(id=pk)
    dictionary.delete()
    return Response("Task Deleted Successfully")