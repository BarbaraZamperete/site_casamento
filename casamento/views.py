from rest_framework.viewsets import ModelViewSet
from .models import Convidado, Presente, Compra
from .serializers import ConvidadoSerializer, PresenteSerializer, CompraSerializer

class ConvidadoViewSet(ModelViewSet):
    queryset = Convidado.objects.all()
    serializer_class = ConvidadoSerializer

class PresenteViewSet(ModelViewSet):
    queryset = Presente.objects.all()
    serializer_class = PresenteSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
