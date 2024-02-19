# Caso simples:
def str_endereco(endereco):
    parte_endereco = endereco.split()  # Divide o endereço
    nome_rua = ''
    numero_rua = ''

    for i in parte_endereco:
        if i.isdigit():  # Se o i for um número 
            numero_rua = i
        else:  # Se o i não for um número 
            nome_rua += i + ' '

    return nome_rua.strip(), numero_rua

testes = ["Miritiba 339", "Babaçu 500", "Cambuí 804B"]

for teste in testes:
    rua, numero = str_endereco(teste)
    print(f"'{teste}' = '{rua}', '{numero}'")


# Caso complicado
def str_endereco(endereco):
    parte_endereco = endereco.split()  # Divide o endereço
    nome_rua = ''
    numero_rua = ''

    for i, parte in enumerate(parte_endereco):
          if parte_endereco.isdigit() or (parte_endereco[0].isdigit() and i > 0 and not parte_endereco[i-1].isdigit()):  # Espaço núm/letra
            