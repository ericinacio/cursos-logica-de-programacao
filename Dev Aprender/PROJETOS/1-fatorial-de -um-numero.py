# Projeto 1 - Fatorial de um número
'''
Crie um programa que recebe um número e imprime o seu fatorial.

#Método 5Q´s para montar um algorítimo:

Analise cirticamente o problema e descubra:(Tente explicar este problema para você mesmo em voz alta e peça mais informaçôes/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- Número.
2. O que devo fazer com estes dados?
- Calcular o numero que for pasado e exibir o seu fatorial na tela.
3. Quais são as restrições deste problema?
- O número deve ser Inteiro e Positivo
4. Qual é o resultado esperado?
- O resultado esperado deve ser exibido.
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?

input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop 1 a numero
  fatorial = fatorial * numero
print(fatorial)
'''

numero = int(input('Digite um número:'))

if numero > 0:
  fatorial = 1
  for item in range(1,numero + 1):
    fatorial = fatorial * item
  print(fatorial)