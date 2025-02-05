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

    @action(detail=False, methods=['put'], url_path='confirmar-presenca')
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

    @action(detail=True, methods=['get'], url_path='lojas')
    def get_lojas(self, request, pk=None):
        """
        Retorna as lojas associadas a um presente específico
        URL: /api/presentes/{id}/lojas/
        """
        try:
            presente = self.get_object()  # Obtém o presente pelo ID (pk)
            lojas = presente.lojas.all()  # Obtém todas as lojas associadas ao presente

            if lojas.exists():  # Verifica se há lojas associadas
                # Serializa as lojas
                lojas_data = [{'id': loja.id, 'nome': loja.nome, 'endereco': loja.endereco, 'tipo': loja.tipo} for loja in lojas]
                return Response(lojas_data, status=status.HTTP_200_OK)
            else:
                # Retorna uma mensagem informativa se não houver lojas
                return Response({'message': 'Não há lojas associadas a este presente.'}, status=status.HTTP_200_OK)

        except Presente.DoesNotExist:
            return Response({'error': 'Presente não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    @action(detail=False, methods=['post'], url_path='gerar-compra')
    def gerar_compra(self, request):
        """
        Cria uma nova compra com status pendente
        URL: /api/compras/gerar-compra/
        Body: {
            "convidadoId": "1",
            "presenteId": "1",
            "valor": 100.00
        }
        """
        convidado_id = request.data.get('convidadoId')
        presente_id = request.data.get('presenteId')
        valor = request.data.get('valor')

        if not all([convidado_id, presente_id, valor]):
            return Response({'error': 'Convidado ID, Presente ID e valor são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

        # Verifica se já existe uma compra pendente com os mesmos dados
        compra_existente = self.queryset.filter(
            convidado_id=convidado_id,
            presente_id=presente_id,
            valor_pago=valor,
            status_pagamento='pendente'
        ).first()

        if compra_existente:
            # Retorna o caminho do QR Code existente
            qr_code_path = f'/media/qrcode/{compra_existente.presente.id}-{compra_existente.presente.nome}.png'
            return Response({'message': 'Uma compra pendente já existe para este convidado e presente.', 'qrCodeUrl': qr_code_path}, status=status.HTTP_200_OK)

        try:
            # Cria uma nova instância de Compra com status pendente
            nova_compra = Compra(
                convidado_id=convidado_id,  # Usando o ID do convidado
                presente_id=presente_id,    # Usando o ID do presente
                valor_pago=valor,
                status_pagamento='pendente'
            )
            nova_compra.save()  # Salva a nova compra no banco de dados

            # Gera o caminho do QR Code
            qr_code_path = f'/media/qrcode/{nova_compra.presente.id}-{nova_compra.presente.nome}.png'

            return Response({'message': 'Compra criada com sucesso', 'compraId': nova_compra.id, 'qrCodeUrl': qr_code_path}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
