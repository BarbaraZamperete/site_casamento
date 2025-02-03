import crcmod
import qrcode
import os

class PayloadPixGen:
    def __init__(self, valor, name, key, city, txtid="***", save_path=".", save_name=""):
        
        # self.valor = valor.replace(",", ".")
        self.valor = valor
        self.name = name
        self.key = key
        self.city = city
        self.txtid = txtid
        self.save_path = save_path  # New attribute for save path
        self.save_name = save_name
        
        valorsize = len(self.valor) 
        namesize = len(self.name)
        keysize = len(self.key)
        citysize = len(self.city)
        
        
        self.merchantinfo = f"0014br.gov.bcb.pix01{keysize:02}{key}"
        self.FieldTemplate = f'0503{txtid}'
        self.txtidsize = f'00{txtid}'
        
        merchantsize = len(self.merchantinfo)
        idsize = len(self.txtid)
        fieltemplatesize = len(self.FieldTemplate)
        txtidsize = len(self.txtidsize)
        
        
        self.payloadindcator = "000201" 
        self.merchantcatinfo = f"26{merchantsize:02}0014BR.GOV.BCB.PIX01{keysize:02}{key}"
        self.merchantcatcod = "52040000"
        self.transactionCurrency = f"5303986"
        self.transactionAmount = f"54{valorsize:02}{self.valor}"
        self.CountryCode = "5802BR"
        self.MerchantName = f"59{namesize:02}{name}"
        self.MerchantCity = F"60{citysize:02}{city}"
        self.DataFieldTemplate = f"62{fieltemplatesize:02}05{idsize:02}{self.txtid}"
        self.Crc16 = "6304"
        self.PayloadBuild = f'{self.payloadindcator}{self.merchantcatinfo}{self.merchantcatcod}{self.transactionCurrency}{self.transactionAmount}{self.CountryCode}{self.MerchantName}{self.MerchantCity}{ self.DataFieldTemplate}{self.Crc16}'
        self.crc16Gen(self.PayloadBuild)
        
        
    def crc16Gen(self, payloadBuild):
        
        crc16 = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)

        self.crc16Code = hex(crc16(str(payloadBuild).encode('utf-8')))

        self.crc16f = str(self.crc16Code).replace('0x', '').upper().zfill(4)

        self.PayloadFull = f'{payloadBuild}{self.crc16f}'
        
        self.QrCodGen(self.PayloadFull)

    
    def QrCodGen(self, payload):
        path_img = os.path.join(self.save_path, f'{self.save_name}.png')
        
        # Verifica se o arquivo já existe
        if os.path.exists(path_img):
            return path_img  # Retorna o caminho se o arquivo já existir
        
        img = qrcode.make(payload)
        img.save(path_img)  # Use save_path for saving
        return path_img  # Return the path where the image was saved
    


