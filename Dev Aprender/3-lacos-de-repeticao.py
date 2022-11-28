# Laços de Repetição + Listas
'''
  for item in coleção
'''


for palavra in range(1, 4):
  print('Carregando')

for item in range(1, 20):
  print(item)

for item in range(1, 20,2):
  print(item)

nomes = ['jhonatan','cristian', 'roberto','camila']

for nome in nomes:
  print(nome)



#1 a N - imprima os valores de 1 a N
'''
  input numero maximo
  valor inicial = 1
  loop de valor_inicial a numero_maximo
  print valor
'''
valor_maximo = int(input('Digite o valor máximo'))
valor_inicial = 1

for numero in range(valor_inicial,valor_maximo + 1):
  print(numero)