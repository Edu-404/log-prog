import csv

with (open('04.arquivo.csv', 'r', encoding='utf-8') as arquivo,
    open('boletim_final.csv', 'w', encoding='utf-8') as arq_saida):

    leitor = csv.DictReader(arquivo, delimiter=';')
    escritor = None

    for aluno in leitor:
        matricula = aluno['matricula']
        estudante = aluno['aluno']

        media = 0
        soma = float(aluno['nota1']) + float(aluno['nota2'])
        media = soma / 2

        situacao = 'indefinida'
        if media >= 7.0:
            situacao = 'APROVADO'
        else:
            situacao = 'REPROVADO'

        notasComMedia = {
            'matricula': matricula,
            'aluno': estudante,
            'nota1': aluno['nota1'],
            'nota2': aluno['nota2'],
            'media': media,
            'situacao': situacao
        }

        if escritor == None:
            cabecalhos = list(notasComMedia.keys())
            escritor = csv.DictWriter(arq_saida, delimiter=';', fieldnames=cabecalhos)
            escritor.writeheader()
        escritor.writerow(notasComMedia)


