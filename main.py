# Caso simples:
def str_endereco(endereco):
  parte_endereco = endereco.split() # Divide o endereço
  nome_rua = ''
  numero_rua = ''

  for i in parte_endereco:
      if i.isdigit():  # Se o i for um número 
          numero_rua = parte_endereco
      else:  # Se o i não for um número 
          nome_rua += parte_endereco + ' '  
      return nome_rua.strip(), numero_rua
  
