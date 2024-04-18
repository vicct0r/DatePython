
# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime, timedelta
from pytz import timezone

# Definindo o formato que será exibido da data/hora
# Existem mais formatos de exibição, para uma melhor compreensão:
# Ler a documentação no topo do módulo; Lá você terá os detalhes da função.
fmt = '%d/%m/%Y %H:%M:%S'

# Criando as variáveis data_inicio e data_fim
# Lembrando que a estrutura da data é no padrão US, ou seja:
# Dia/Mês/Ano - Horas/Minutos/Segundos
# O método strptime só aceita as informações no formato str;
# Tem uma outra função encarregada somente para valores numéricos.

data_inicio = datetime.strptime('01/01/2024 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2024 09:30:30', fmt)

# Utilizando timezone juntamente com o horario na minha máquina;
# Na saída dessa variável, temos o seguinte:
# 2024-04-18 07:13:55.482914+09:00
# Data (2024-04-18) Horario (07:13:55 milisegundos(.482914)) 
# E o timezone me trouxe: +09:00 que é a diferença do meu horário com o horário em Tokyo.

data_agora = datetime.now(timezone('Asia/Tokyo')) # A hora exata na minha máquina.


# Definindo o delta:
# --OBS.: O delta (timedelta) não é uma data, mas sim a diferença entre duas datas; 
# Logo, timedelta representa um valor, seja ele em milisegundos, horas, meses ou até mesmo anos.

# Unix Timestamp
# É a contagem de segundos de 01/01/1970 até o dia de hoje;
# Isso se torna útil para trabalhar com datas, pois com isso,
# Pode-se trabalhar com datas apenas usando um valor inteiro.

data = datetime.now()
valor_unix_segundos = data.timestamp()

# O valor resultante de timestamp() para o dia de hoje foi: 1713392523.594176
# Esse valor equivale aos segundos exatos do dia 01/01/1970, até hoje 18/04/2024

print('Data hoje: ')
print(datetime.fromtimestamp(1713392523))


delta_diferenca = data_fim - data_inicio
metodo_delta = timedelta(days=10, hours=5, seconds=50)


