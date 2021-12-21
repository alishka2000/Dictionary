from rest_framework import serializers
from .models import Dictionary
from .models import Language

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
