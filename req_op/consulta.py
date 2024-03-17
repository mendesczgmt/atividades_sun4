import requests
from bs4 import BeautifulSoup

class BuscaNick:
    
    def buscar_o_nick(self, nickname:str):
        cookies = {
            '_ga': 'GA1.2.1891831128.1710648253',
            '_gid': 'GA1.2.2075584635.1710648253',
            '_gat': '1',
            '_ga_VR22Y0JWSQ': 'GS1.2.1710648253.1.0.1710648253.60.0.0',
        }

        headers = {
            'authority': 'wol.gg',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': '_ga=GA1.2.1891831128.1710648253; _gid=GA1.2.2075584635.1710648253; _gat=1; _ga_VR22Y0JWSQ=GS1.2.1710648253.1.0.1710648253.60.0.0',
            'referer': 'https://wol.gg/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

        response = requests.get(f'https://wol.gg/stats/br/{nickname}/', cookies=cookies, headers=headers)
        return response

    def _validar_nick_buscado(self, response):
        site = BeautifulSoup(response.content, 'html.parser')
        textos = site.find_all('div', {'class': 'text'})
        for texto in textos:
            print(texto.text)
            if "erro" in texto.text:
                return False
            else:
                continue
        return True

    def encontrar_minutos(self, response):
        if self._validar_nick_buscado(response):
            try:
                site = BeautifulSoup(response.content, 'html.parser')
                minutos = site.find('div', {'id': 'time-minutes'})
                minutos = minutos.text.split('m')
                minutos_formatados = float(minutos[0].replace(',', '.'))
                print(f'Você passou {minutos_formatados} minutos jogando LoL')
                return minutos_formatados
            except:
                print('erro ao validar os minutos jogados')
                return -1
        else:
            print('Erro ao validar nickname')
    
    def encontrar_horas(self, response):
        if self._validar_nick_buscado(response):
            try:
                site = BeautifulSoup(response.content, 'html.parser')
                horas = site.find('div', {'id': 'time-hours'})
                horas = horas.text.split('h')
                horas_formatadas = float(horas[0].replace(',', '.'))
                print(f'Você passou {horas_formatadas} horas jogando LoL')
                return horas_formatadas
            except:
                print('erro ao validar as horas jogadas')
                return -1
        else:
            print('Erro ao validar nickname')
    
    def encontrar_dias(self, response):
        if self._validar_nick_buscado(response):
            try:
                site = BeautifulSoup(response.content, 'html.parser')
                dias = site.find('div', {'id': 'time-days'})
                dias = dias.text.split('d')
                dias_formatados = float(dias[0].replace(',', '.'))
                print(f'Você passou {dias_formatados:.0f} dias jogando LoL')
                return dias_formatados
            except:
                print('erro ao validar os dias jogados')
                return -1
        else:
            print('Erro ao validar nickname')
    
    def encontrar_tudo(self, response):
        minutos = self.encontrar_minutos(response)
        horas = self.encontrar_horas(response)
        dias = self.encontrar_dias(response)
        