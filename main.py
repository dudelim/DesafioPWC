# Caso simples:
def str_endereco(endereco):
  parte_endereco = endereco.split()
  nome_rua = ''
  numero_rua = ''

  for i in parte_endereco:
      if i.isdigit():  
          numero_rua = parte_endereco
      else:  
          nome_rua += parte_endereco + ' '  

  
