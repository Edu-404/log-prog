from datetime import datetime

def registrar_evento(usuario, acao, status):
    with open('auditoria_sistema.log', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{usuario}, {acao}, {status}, {datetime.now()}' + '\n')

registrar_evento('Laura', 'Saque', 'Sucesso')
registrar_evento('Miguel', 'Transferência', 'Falha')

