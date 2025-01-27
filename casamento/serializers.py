from rest_framework import serializers
from .models import Convidado, Presente, Compra

class ConvidadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convidado
        fields = '__all__'

class PresenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presente
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
