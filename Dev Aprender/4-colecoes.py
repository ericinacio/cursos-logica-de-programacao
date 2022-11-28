# Coleções(lsita)
preco_1 = 20
preco_2 = 50
preco_3 = 200
precos = [20,50,200]
#Index    0, 1,  2
print(precos[0])
print(precos.index(200))



diversidades = [15,'Jhonatan', True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])

#Laços em iteráveis
for preco in precos:
  print(preco)



# Exemplo 5 - Some os valores
# Dados uma coleção de dados "idades" [15,46,75,34,23] imprima na tela a soma destes valores
'''
idades = [15,46,75,34,23]
total = 0
loop idade em idades
  total = total + idade
print total
'''
idades = [15,46,75,34,23]
total = 0
for idade in idades:
  total = total + idade
print(total)