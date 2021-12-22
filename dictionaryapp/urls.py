
from django.urls import path
from . import views

urlpatterns = [
    # This url for 1 table Dictionary
    path('', views.apiOverview, name="api-overview"),
    path('dictionary-list', views.dictionaryList, name="dictionary-list"),
    path('dictionary-item/<str:pk>/', views.dictionaryItem, name="dictionary-item"),
    path('dictionary-create/', views.dictionaryCreate, name="dictionary-create"),
    path('dictionary-update/<str:pk>/', views.dictionaryUpdate, name="dictionary-update"),
    path('dictionary-delete/<str:pk>/', views.dictionaryDelete, name="dictionary-delete"),

    # This url for 2 table Language
    path('', views.apiOverview, name="api-overview"),
    path('language-list', views.languageList, name="language-list"),
    path('language-item/<str:pk>/', views.languageItem, name="language-item"),
    path('language-create/', views.languageCreate, name="language-create"),
    path('language-update/<str:pk>/', views.languageUpdate, name="language-update"),
    path('language-delete/<str:pk>/', views.languageDelete, name="language-delete"),
]