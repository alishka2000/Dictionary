from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from .models import Dictionary
from .models import Language
from .serializer import DictionarySerializer
from .serializer import LanguageSerializer
from django.shortcuts import render
from django.views import View

# This 'GET' method give to client information about site's URL. And which URL we have.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverview(request):
    api_urls = {
        'List': '/dictionary-list/ ''or'' /language-list/',
        'Create': '/dictionary/ ''or'' /language/',
        'Update': '/dictionary/<str:pk>/ ''or'' /language/<str:pk>/',
        'Delete': '/dictionary/<str:pk>/ ''or'' /language/<str:pk>/',
        'Item': '/dictionary/<str:pk>/ ''or'' /language/<str:pk>/',
    }
    return Response(api_urls)

class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def dictionaries(request):
    if request.method == 'GET':
        dictionary = Dictionary.objects.all()
        serializer = DictionarySerializer(dictionary, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DictionarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
def languages(request):
    if request.method == 'GET':
        language = Language.objects.all()
        serializer = DictionarySerializer(language, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def dictionary(request, pk):
    try:
        dictionary = Dictionary.objects.get(id=pk)
    except:
        print('No item')

    if request.method == 'GET':
        serializer = DictionarySerializer(dictionary)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DictionarySerializer(instance=dictionary, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        dictionary.delete()
        return Response("Task Deleted Successfully")

@permission_classes((permissions.AllowAny,))
def language(request, pk):
    try:
        language = Language.objects.get(id=pk)
    except:
        print('No item')

    if request.method == 'GET':
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LanguageSerializer(instance=language, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        language.delete()
        return Response("Task Deleted Successfully")



#
# # This 'GET' method give to client information about site's URL. And which URL we have.
#
# # Giving list of our table values
# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def dictionaryList(request):
#     dictionary = Dictionary.objects.all()
#     serializer = DictionarySerializer(dictionary, many=True)
#     return Response(serializer.data)
#
# # Creating new values
# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def dictionaryCreate(request):
#     serializer = DictionarySerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# # Updating our value
# @api_view(['PUT'])
# @permission_classes((permissions.AllowAny,))
# def dictionaryUpdate(request, pk):
#     dictionary = Dictionary.objects.get(id=pk)
#     serializer = DictionarySerializer(instance=dictionary, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# # Deleting value
# @api_view(['DELETE'])
# @permission_classes((permissions.AllowAny,))
# def dictionaryDelete(request, pk):
#     dictionary = Dictionary.objects.get(id=pk)
#     dictionary.delete()
#     return Response("Task Deleted Successfully")
#
# # Showing 1 item of our table
# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def dictionaryItem(request, pk):
#     dictionary = Dictionary.objects.get(id=pk)
#     serializer = DictionarySerializer(dictionary)
#     return Response(serializer.data)

#
# # After this comment we done 'CRUD' for 2 table 'Language'
#
#
# # Giving list of our table values
# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def languageList(request):
#     language = Language.objects.all()
#     serializer = LanguageSerializer(language, many=True)
#     return Response(serializer.data)
#
# # Creating new values
# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def languageCreate(request):
#     serializer = LanguageSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# # Updating our value
# @api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
# def languageUpdate(request, pk):
#     language = Language.objects.get(id=pk)
#     serializer = LanguageSerializer(instance=language, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# # Deleting value
# @api_view(['DELETE'])
# @permission_classes((permissions.AllowAny,))
# def languageDelete(request, pk):
#     language = Language.objects.get(id=pk)
#     language.delete()
#     return Response("Task Deleted Successfully")
#
# # Showing 1 item of our table
# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def languageItem(request, pk):
#     language = Language.objects.get(id=pk)
#     serializer = LanguageSerializer(language)
#     return Response(serializer.data)