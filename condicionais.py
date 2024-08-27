# Enquanto determinada condição for verdadeira, o processo se repete.

x = 0

while x <= 5:
  print(x)
  x = x + 1
  
# Enquanto o usuário não digitar a palavra específica o código não é executado.

validador = input('Digite "Brasil" para continuar:')

while validador != 'Brasil':
    print('Palavra-chave não confere, digite novamente:')
    validador = input('Digite "Brasil" para continuar:')

    if validador == 'Brasil':
        print('Agora você digitou Brasil corretamente.')

     
