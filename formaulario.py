with (open('03.arquivo.txt', 'r', encoding='utf-8') as arquivo,
    open('emails_padronizados.txt', 'a', encoding='utf-8') as arq_saida):

    for email in arquivo:
        emailFormatado = email.strip().lower()
        arq_saida.write(emailFormatado + '\n')
        