from rest_framework import serializers
from .models import Materials, Troops

class MaterialsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materials
        fields = ('name','size')

class TroopsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Troops
        fields = ('name','attack', 'defence_infantry', 'defence_cavalry', 'speed', 'carrying_capacity', 'crop_consumption', 'troops_size')