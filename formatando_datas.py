# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime

# fmt é uma variável contendo o formato para exibição da data;
# Podemos usa-lo de forma direta como parâmetro para o método de criação de data;
# Ou inserindo este formato em uma variável; Como está sendo feito em fmt.

# %d (day)/ %m (month)/ %Y (year)
fmt = '%d/%m/%Y'

# Para fazer a formatação devemos ter uma data base para formatar
# Nesta data estamos criando no mesmo formato em que a data está sendo passada;
# Ou seja, primeiramente é passado a data, e posteriormente o horário:
# '%Y-%m-%d %H:%M:%S' --> ([Y]ear-[m]onth-[d]ay [H]our:[M]inute:[S]econds) 
data = datetime.strptime('2024-05-18 15:05:00', '%Y-%m-%d %H:%M:%S')

# Agora que temos uma data, podemos criar uma outra variável para guardar 
# sua versão formatada; (fmt contém a formatação apresentando apenas a data no formato Dia/Mês/Ano)
data_formatada = data.strftime(fmt)
print(f'\nVariável data: {data}\nVariável data_formatada: {data_formatada}\n')

# Mas é possível apresentar a data formatada de outras formas como:
# Apenas a data Hora/Minuto
print(f"Apenas a Data com Hora/Minuto: {data.strftime('%d/%m/%Y %H:%M')}\n")

#Apenas Dia e Hora 
print(f"Apenas o Dia e a Hora: {data.strftime('%d %H:%M')}\n")

#Apenas a Hora
print(f"Apenas o Horario: {data.strftime('%H:%M:%S')}\n")

# Repare que, o tipo da variável é str
print(type(data_formatada))

# Para exibir no tipo int, pode ser feito o seguinte:
# A diferença, além do tipo da saída, também percebe-se na forma de exibição:
# em str 2024/05/18  
# em int 2024/5/18
print(data.year, data.month, data.day)

# É útil saber isso, pois de acordo com a saída você pode manipular de acordo com seu tipo;
# A data no tipo 'str' pode ser formatada de diferentes formas (de acordo com a diretiva do método datetime)
# Já em 'int' ela pode ser usada para outros tipos de manipulação, levando em consideração que é um valor inteiro.