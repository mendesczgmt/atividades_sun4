import requests

class ApiDolar:

    def buscar_alta_brl(self):
        resposta = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        return resposta.json()['USDBRL']['high']

    def buscar_baixa_brl(self):
        resposta = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        return resposta.json()['USDBRL']['low']

class ApiAdvice:

    def buscar_frase(self):
        resposta = requests.get('https://api.adviceslip.com/advice')
        return resposta.json()['slip']['advice']
    
    def buscar_frase_id(self, id:int):
        resposta = requests.get(f'https://api.adviceslip.com/advice/{id}')
        return resposta.json()['slip']['advice']