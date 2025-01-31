from PixPayloadGen import PayloadPixGen
import qrcode

def gerar_qrcode(valor, nome, chave, cidade, textId, save_path):
    '''
    Gera um QRCode a partir de um payload Pix
    O payload tem que ser um dicionário com os seguintes campos:
    -valor: float
    -nome: str
    -chave: str
    -cidade: str
    -textId: str
    '''
    payload_pix_gen = PayloadPixGen(valor, nome, chave, cidade, textId, save_path)
    payload_pix_gen.QrCodGen(payload_pix_gen.PayloadFull)  # Passa o payload completo para gerar o QR Code


if __name__== '__main__':
    valor = 100.00
    nome = 'João da Silva'
    chave = 'joaodasilva@gmail.com'
    cidade = 'São Paulo'
    textId = '1234567890'
    save_path = 'media/qrcode'
    gerar_qrcode(valor, nome, chave, cidade, textId, save_path)  # Chama a função para gerar o QR Code