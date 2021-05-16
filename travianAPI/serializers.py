from rest_framework import serializers
from .models import Materials, Troops

class MaterialsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materials
        fields = ('name','size')

class TroopsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Troops
        fields = ('name','size')