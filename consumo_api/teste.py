from apis import ApiDolar, ApiAdvice

api_dolar = ApiDolar()
api_advice = ApiAdvice()

alta = api_dolar.buscar_alta_brl()
#print(f'A alta foi de {alta}')

baixa = api_dolar.buscar_baixa_brl()
#print(f'A baixa foi de {baixa}')

frase = api_advice.buscar_frase()
print(f'a frase é: {frase}')

frase = api_advice.buscar_frase_id(71)
print(f'a frase é por id é: {frase}')