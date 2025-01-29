from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Convidado, Presente, Compra
from .serializers import ConvidadoSerializer, PresenteSerializer, CompraSerializer

class ConvidadoViewSet(ModelViewSet):
    queryset = Convidado.objects.all()
    serializer_class = ConvidadoSerializer

    @action(detail=False, methods=['get'], url_path='buscar-por-convite')
    def buscar_por_convite(self, request):
        """
        Busca convidados por número do convite
        URL: /api/convidados/buscar-por-convite/?numero_convite=123
        """
        print(request.query_params)
        numero_convite = request.query_params.get('numero_convite')
        if numero_convite:
            convidados = self.queryset.filter(codigo_convite=numero_convite)
            serializer = self.serializer_class(convidados, many=True)
            return Response(serializer.data)
        return Response({'error': 'Número do convite não fornecido'}, status=400)

    @action(detail=False, methods=['get'], url_path='buscar-por-nome') 
    def buscar_por_nome(self, request):
        """
        Busca convidados por nome
        URL: /api/convidados/buscar-por-nome/?nome=João
        """
        nome = request.query_params.get('nome')
        if nome:
            convidados = self.queryset.filter(nome__icontains=nome)
            serializer = self.serializer_class(convidados, many=True)
            return Response(serializer.data)
        return Response({'error': 'Nome não fornecido'}, status=400)

class PresenteViewSet(ModelViewSet):
    queryset = Presente.objects.all()
    serializer_class = PresenteSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
