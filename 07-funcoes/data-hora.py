# from datetime import datetime

# data_especial = datetime(2024, 12, 14)
# print(f"Data Especial: {data_especial}")

# hoje = datetime.now()
# print(f"Hoje: {hoje.strftime("%d/%m/%Y")}")

# meses = [ "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

# dia = hoje.day
# mes = meses[hoje.month - 1]
# ano = hoje.year

# print(f"Hoje, dia {dia} de {mes} de {ano}")

# # data por extenso
# # alternativa com módulo nativo 'locale'
# from locale 
# import calendar
# import locale

# try:
#     locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
# except locale.Error:
# # 	# windows
#     locale.setlocale(locale.LC_TIME, 'portuguese') 

# data = datetime.now()
# print(data.strftime('%d de %B de %Y'))

# # define o primeiro dia da semana como domingo
# calendar.setfirstweekday(calendar.SUNDAY)
# calendar.prmonth(2026, 10)

# print(f"Último dia do mês? {calendar.monthrange(2026, 10)[1]}")
# print(f"Ano bissexto? {calendar.isleap(2026)}")

# # define 
# cal = calendar.TextCalendar(calendar.SUNDAY)
# print(cal.formatyear(2026))
