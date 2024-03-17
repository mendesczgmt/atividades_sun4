from consulta import BuscaNick

bot = BuscaNick()

response = bot.buscar_o_nick('lkz')
#bot.encontrar_minutos(response)
#bot.encontrar_dias(response)
bot.encontrar_tudo(response)