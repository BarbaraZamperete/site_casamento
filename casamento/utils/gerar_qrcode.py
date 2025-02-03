from .pyloadpixgen_edit import PayloadPixGen
import qrcode
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()



def gerar_qrcode(valor, textId):
    '''
    Gera um QRCode a partir de um payload Pix
    O payload tem que ser um dicionário com os seguintes campos:
    -valor: str (XX.XXX)
    -textId: str
    '''
    # Obtém os valores das variáveis de ambiente
    nome = os.getenv('QR_CODE_NOME')
    chave = os.getenv('QR_CODE_CHAVE')
    cidade = os.getenv('QR_CODE_CIDADE')
    save_path = os.getenv('QR_CODE_SAVE_PATH')

    # Verifica se as variáveis de ambiente estão definidas
    if not all([nome, chave, cidade]):
        raise ValueError("As variáveis de ambiente QR_CODE_NOME, QR_CODE_CHAVE e QR_CODE_CIDADE devem estar definidas.")

    payload_pix_gen = PayloadPixGen(valor, nome, chave, cidade, textId, save_path, f'{textId}')
    return payload_pix_gen.QrCodGen(payload_pix_gen.PayloadFull)  # Passa o payload completo para gerar o QR Code



if __name__== '__main__':
    valor = '1.00'
    textId = 'TESTE'
    save_path = 'media/qrcode'
    gerar_qrcode(valor, textId, save_path)  # Chama a função para gerar o QR Code