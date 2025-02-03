from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Convidado, Presente, Compra
from .serializers import ConvidadoSerializer, PresenteSerializer, CompraSerializer
from .utils.gerar_qrcode import gerar_qrcode
import os
from rest_framework import status

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

    @action(detail=False, methods=['post'], url_path='confirmar-presenca')
    def confirmar_presenca(self, request):
        """
        Confirma a presença de um ou mais convidados
        URL: /api/convidados/confirmar-presenca/
        Body: {
            "convidados": [
                {"id": 1, "presenca_confirmada": true},
                {"id": 2, "presenca_confirmada": false}
            ]
        }
        """
        convidados_data = request.data.get('convidados', [])
        if not convidados_data:
            return Response({'error': 'Nenhum convidado fornecido'}, status=400)

        for convidado_data in convidados_data:
            convidado_id = convidado_data.get('id')
            presenca_confirmada = convidado_data.get('presenca_confirmada')
            
            try:
                convidado = self.queryset.get(id=convidado_id)
                convidado.presenca_confirmada = presenca_confirmada
                convidado.save()
            except Convidado.DoesNotExist:
                return Response({'error': f'Convidado com ID {convidado_id} não encontrado'}, status=404)

        return Response({'message': 'Presenças atualizadas com sucesso'})

class PresenteViewSet(ModelViewSet):
    queryset = Presente.objects.all()
    serializer_class = PresenteSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    @action(detail=False, methods=['post'], url_path='gerar-qrcode')
    def gerar_qrcode_view(self, request):
        """
        Gera um QR Code para pagamento
        URL: /api/compras/gerar-qrcode/
        Body: {
            "id": "1",
            "nome": "Produto Exemplo",
            "valor": 100.00
        }
        """
        id = request.data.get('id')
        nome = request.data.get('nome')
        valor = request.data.get('valor')
        convidado_id = request.data.get('convidadoId')

        if not all([id, nome, valor, convidado_id]):
            return Response({'error': 'ID, nome e valor são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Chama a função de utilitários para gerar o QR Code
            qr_code_path = gerar_qrcode(valor, f'{id}-{nome}')
            print(qr_code_path)
            # Cria uma nova instância de Compra
            nova_compra = Compra(
                convidado_id=convidado_id,
                presente_id=id,
                valor_pago=valor
            )
            nova_compra.save()  # Salva a nova compra no banco de dados

            return Response({'qrCodeUrl': qr_code_path}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
