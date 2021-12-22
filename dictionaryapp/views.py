from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from .models import Dictionary
from .models import Language
from .serializer import DictionarySerializer
from .serializer import LanguageSerializer

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverview(request):
    api_urls = {
        'List': '/dictionary-list/ ''or'' /language-list/',
        'Create': '/dictionary-create/ ''or'' /language-create/',
        'Update': '/dictionary-update/<str:pk>/ ''or'' /language-update/<str:pk>/',
        'Delete': '/dictionary-delete/<str:pk>/ ''or'' /language-delete/<str:pk>/',
        'Item': '/dictionary-item/<str:pk>/ ''or'' /language-item/<str:pk>/',
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

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def dictionaryItem(request, pk):
    dictionary = Dictionary.objects.get(id=pk)
    serializer = DictionarySerializer(dictionary)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def languageList(request):
    language = Language.objects.all()
    serializer = LanguageSerializer(language, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def languageCreate(request):
    serializer = LanguageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def languageUpdate(request, pk):
    language = Language.objects.get(id=pk)
    serializer = LanguageSerializer(instance=language, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def languageDelete(request, pk):
    language = Language.objects.get(id=pk)
    language.delete()
    return Response("Task Deleted Successfully")

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def languageItem(request, pk):
    language = Language.objects.get(id=pk)
    serializer = LanguageSerializer(language)
    return Response(serializer.data)