# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime, timedelta

data_do_emprestimo = datetime.strptime('20/12/2020', '%d/%m/%Y')
valor_de_cada_parcela = round(1000000/(5*12), 2)
data_atual = data_do_emprestimo + timedelta(days=1)
parcela = 1
valor_pago = 0


while valor_pago <= 1000000:
    
    if data_atual.day == 20:
        print(f"{parcela}--{data_atual.strftime('%d/%m/%Y')} valor: {valor_de_cada_parcela}")
        valor_pago += valor_de_cada_parcela
        parcela += 1

    data_atual += timedelta(days=1)


