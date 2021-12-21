
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('dictionary-list', views.dictionaryList, name="dictionary-list"),
    path('dictionary-create/', views.dictionaryCreate, name="dictionary-create"),

    path('dictionary-update/<str:pk>/', views.dictionaryUpdate, name="dictionary-update"),
    path('dictionary-delete/<str:pk>/', views.dictionaryDelete, name="dictionary-delete"),
]