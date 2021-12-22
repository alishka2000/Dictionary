
from django.urls import path
from . import views

urlpatterns = [
    # This url for 1 table Dictionary
    path('', views.apiOverview, name="api-overview"),
    path('dictionary-list', views.dictionaries, name="dictionary-list"),
    path('dictionary/', views.dictionary, name="dictionary-create"),
    path('dictionary/<str:pk>/', views.dictionaries, name="dictionary-item"),
    path('dictionary/<str:pk>', views.dictionary, name="dictionary-update"),
    path('dictionary/<str:pk>', views.dictionary, name="dictionary-delete"),

    # This url for 2 table Language
    path('', views.apiOverview, name="api-overview"),
    path('language-list', views.languages, name="language-list"),
    path('language/<str:pk>/', views.languages, name="language-item"),
    path('language/', views.language, name="language-create"),
    path('language/<str:pk>', views.language, name="language-update"),
    path('language/<str:pk>', views.language, name="language-delete"),
]