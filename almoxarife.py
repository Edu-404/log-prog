import csv

with (open('02.arquivo.csv', 'r', encoding='utf-8') as arquivo,
    open('pedidos_reposicao.csv', 'w', encoding='utf-8') as arq_saida):

    leitor = csv.DictReader(arquivo, delimiter=';')
    escritor = None

    for produto in leitor:
        id = produto['id']
        item = produto['produto']
        estoqueMinimo = int(produto['estoque_minimo'])
        saldoAtual = int(produto['saldo_atual'])

        if saldoAtual < estoqueMinimo:
            qnt_comprar = estoqueMinimo - saldoAtual

            vendas_filtradas = {
                'id': id,
                'produto': item,
                'saldo_atual': saldoAtual,
                'estoque_minimo': estoqueMinimo,
                'qnt_comprar': qnt_comprar
            }

            if escritor == None:
                cabecalhos = list(vendas_filtradas.keys())
                escritor = csv.DictWriter(arq_saida, delimiter=';', fieldnames=cabecalhos)
                escritor.writeheader()
            escritor.writerow(vendas_filtradas)