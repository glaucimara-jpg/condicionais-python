

num = 0
total = 10

while num <= 10:
  # Enquanto o valor de num for igual ou menor que 10
  print(num)
  num += 1
  # num é atualizado, incrementado em 1 unidade
  if num == 5:
    # Se o valor de num for igual a 5
    print('50% computado')
  if num == 10:
    # Se o valor de num for igual a 10
    print('100%, processo encerrado')





    while True:
       
     validador = input('Digite "Brasil" para continuar:')
    
    if validador == 'Brasil':
        print('Você digitou Brasil corretamente!!!')
        break # interrompe o processo / loop
    else:
        print('Palavra-chave não confere, digite novamente:')

# while True nesse caso simula um ciclo "infinito", sendo necessário que quando
# a condição for atingida, o marcador break interrompe o ciclo.






# Laço de repetição simples

compras = ['Arroz', 'Feijão', 'Massa', 'Carne', 'Pão']

for i in compras:
  print(i)

# A variável temporária i a cada ciclo irá ler um dos elementos da lista
# compras, sendo que a cada ciclo lê e retorna o elemento subsequente.
