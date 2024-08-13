nome = input('Digite o seu nome:')

if nome == 'Fernando':
  print('Bem vindo de volta Fernando!!!')

print(f'Você é novo(a) aqui, olá {nome}!!!')

# Se a condição for atingida, o bloco indentado a ela é
# executado, caso contrario é simplesmente ignorado.

# Também chamadas de estruturas de controle de fluxo.

     

num = 51

if num < 50:
  print('Menor que 50')
else:
  print('Maior que 50')

# Se o valor de num for menor que 50, exiba em tela 'Menor que 50',
# caso contrário, exiba em tela 'Maior que 50'.


nome = input('Digite o seu nome:')

if nome == 'Fernando':
  print('Bem vindo de volta Fernando!!!')
if nome == 'Maria':
  print('Bem vinda de volta Maria!!!')

# Sendo a primeira proposição verdadeira, a execução desse bloco
# de código é encerrada.

     

nome = input('Digite o seu nome:')

if nome == 'Fernando':
  print('Bem vindo de volta Fernando!!!')
if nome == 'Maria':
  print('Bem vinda de volta Maria!!!')

# Quando a primeira proposição não é validada como verdadeira, o
# interpretador irá para a segunda proposição, e assim por diante
# até encontrar uma proposição verdadeira.

     

nome = input('Digite o seu nome:')

if nome == 'Fernando':
    print('Bem vindo de volta Fernando!!!')
if nome == 'Carlos':
    print('Bem vindo de volta Carlos!!!')
if nome == 'Maria':
    print('Bem vinda de volta Maria!!!')
if nome == 'Tânia':
    print('Bem vinda de volta Tânia!!!')
else:
    print('Você não é Fernando nem Maria...')
    print(f'Você é novo(a) aqui, olá {nome}!!!')

# Quando nenhuma proposição for verdadeira, é possível por meio
# de else criar um retorno padrão para esses casos.

     


# Usando elif a partir da segunda proposição, uma proposição sendo verdadeira
# já encerra o processo naquele ponto.

num1 = float(input('Digite um número: '))

if num1 <= 49:
    print('Menor que 50')
elif num1 == 50:
    print('Igual a 50')
elif num1 >= 51 and num1 < 100:
    print('Maior que 50')
else:
    print('Número Inválido')

     

num1 = float(input('Digite um número: '))

if num1 <= 49:
    print('Menor que 50')
elif num1 == 50:
    print('Igual a 50')
elif num1 >= 51 and num1 < 100:
    print('Maior que 50')
else:
    print('Número Inválido')

     


nome1 = 'Fernando'
nome2 = 'Maria'

if nome1 == 'Fernando':
  print('Bem-vindo Fernando!!!')
if nome2 == 'Maria':
  print('Bem-vinda Maria!!!')
else:
  print('Erro: Nome Desconhecido.')

# Usando de ifs, mais de uma proposição pode ser considerada verdadeira,
# nesse caso, retornando Bem-vindo Fernando!!! e Bem-vinda Maria!!!

nome1 = 'Fernando'
nome2 = 'Maria'

if nome1 == 'Fernando':
  print('Bem-vindo Fernando!!!')
elif nome2 == 'Maria':
  print('Bem-vinda Maria!!!')
else:
  print('Erro: Nome Desconhecido.')

# Usando de elif, o retorno seria apenas Bem-vindo Fernando!!!
# pois uma proposição sendo verdadeira já encerra o processo.

     


num1 = 12
num2 = 44
nome1 = 'Fernando'
nome2 = 'Maria'

if num1 >= 10 and nome1 == 'Fernando':
  print('Número maior que 10 e o usuário é Fernando')
if num1 <= 10 and nome1 == 'Fernando':
  print('Número menor que 10 e o usuário é Fernando')
if num1 == num2 and nome2 == 'Maria':
  print('Número 1 e número 2 são iguais, assim como o usuário é Maria')
if num1 != num2 and nome2 == 'Maria':
  print('Número 1 e número 2 são diferentes, assim como o usuário é Maria')

# Operador and exige que as duas condições sejam verdadeiras (uma condição e outra).


num1 = 12
num2 = 44
nome1 = 'Fernando'
nome2 = 'Maria'

if num1 >= 10 and nome1 == 'Fernando':
  # Se o valor de num1 for igual ou maior que 10 e nome1 for igual a Fernando...
  print('Número maior que 10 e o usuário é Fernando')
if num1 <= 10 and nome1 == 'Fernando':
  # Se o valor de num1 for igual ou menor que 10 e nome1 for igual a Fernando
  print('Número menor que 10 e o usuário é Fernando')
if num1 == num2 and nome2 == 'Maria':
  # Se o valor de num1 for igual ao valor de num2 e nome2 for igual a Maria
  print('Número 1 e número 2 são iguais, assim como o usuário é Maria')
if num1 != num2 and nome2 == 'Maria':
  # Se o valor de num1 for diferente de num2 e nome2 for igual a Maria
  print('Número 1 e número 2 são diferentes, assim como o usuário é Maria')

     

num1 = 2
num2 = 15

if (num1 + num2) > 20:
    print('O resultado da soma é MAIOR do que 20')
elif (num1 + num2) == 20:
    print('O resultado da soma é IGUAL a 20')
else:
    print('O resultado da soma é MENOR do que 20')
  
     


num1 = 2
num2 = 15

if (num1 + num2) > 20:
    # Se o resultado da soma de num1 e num2 for maior que 20...
    print('O resultado da soma é MAIOR do que 20')
elif (num1 + num2) == 20:
    # Se o resultado da soma de num1 e num2 for igual a 20
    print('O resultado da soma é IGUAL a 20')
else:
    # Caso nenhuma das condições anteriores seja válida
    print('O resultado da soma é MENOR do que 20')
  
     


nomes = ['Fernando', 'Maria', 'Carlos']
login = input('Digite o seu nome: ')

if login in nomes:
  # Se o nome atribuído a login for um dos elementos da lista nomes...
  print(f'Bem-vindo(a) {login}')
else:
  print('Usuário não cadastrado.')
  
     



num1 = 15
num2 = 40
num3 = 2
soma = num1 + num2 + num3

if (num1 + num2) >= 0:
  print('O número é positivo')
if (num1 + num2) > 50 and soma < 100:
  print('O número é maior que 50 e menor que 100')
  
     


num1 = 15
num2 = 40
num3 = 2
soma = num1 + num2 + num3

if (num1 + num2) >= 0:
  # Se o resultado da soma de num1 e num2 for um número igual ou maior que zero...
  print('O número é positivo')
if (num1 + num2) > 50 and soma < 100:
  # Se o resultado da soma de num1 e num2 for maior que 50 e o valor de soma,
  # que por sua vez é a soma dos valores das variáveis num1, num2 e num3 for
  # menor que 100...
  print('O número é maior que 50 e menor que 100')
  
     


nome = input('Digite o seu nome: ')

if nome == 'Fernando':
  print('Olá Fernando, você é o administrador do sistema!!!')
elif nome in 'Ana Bárbara Carlos José Maria Paulo Tatiana':
  print(f'Bem vindo(a) {nome}, você é um(a) usuário(a) registrado no sistema.')
else:
  print('Olá, você não está logado no sistema, suas permissões são restritas.')
  
     


nome = input('Digite o seu nome: ')

if nome == 'Fernando':
  # Se o nome atribuído a variável nome for Fernando...
  print('Olá Fernando, você é o administrador do sistema!!!')
elif nome in 'Ana Bárbara Carlos José Maria Paulo Tatiana':
  # Se o nome atribuído a variável nome for um dos nomes em 'Ana Bárbara
  # Carlos José Maria Paulo Tatiana'...
  print(f'Bem vindo(a) {nome}, você é um(a) usuário(a) registrado no sistema.')
else:
  # Caso contrário
  print('Olá, você não está logado no sistema, suas permissões são restritas.')
  

nome = input('Digite o seu nome: ')

if nome == 'Fernando':
  print('Olá Fernando, você é o administrador do sistema!!!')
elif nome in 'Ana Bárbara Carlos José Maria Paulo Tatiana':
  print(f'Bem vindo(a) {nome}, você é um(a) usuário(a) registrado no sistema.')
else:
  print('Olá, você não está logado no sistema, suas permissões são restritas.')
  
     
# Mesmo exemplo que o anterior, mas diferenciando gêneros

nome = input('Digite o seu nome: ')

if nome == 'Fernando':
  print('Olá Fernando, você é o administraor do sistema!!!')
elif nome in 'Ana Bárbara Maria Tatiana':
  print(f'Bem vinda {nome}, você é uma usuária registrada no sistema.')
elif nome in 'Carlos José Paulo':
  print(f'Bem vindo {nome}, você é um usuário registrado no sistema.')
else:
  print('Olá, você não está logado no sistema, suas permissões são restritas.')
  
     

nome = input('Digite o seu nome: ')

if nome == 'Fernando':
  # Se nome for igual a Fernando
  print('Olá Fernando, você é o administraor do sistema!!!')
elif nome in 'Ana Bárbara Maria Tatiana':
  # Se nome for um dos nomes em 'Ana Bárbara Maria Tatiana'
  print(f'Bem vinda {nome}, você é uma usuária registrada no sistema.')
elif nome in 'Carlos José Paulo':
  # Se nome for um dos nomes em 'Carlos José Paulo'
  print(f'Bem vindo {nome}, você é um usuário registrado no sistema.')
else:
  # Caso contrário
  print('Olá, você não está logado no sistema, suas permissões são restritas.')
  
     

# Mesmo exemplo anterior, aprimorado

nome = input('Digite o seu nome: ')

funcionarios_homens = ['Carlos', 'José', 'Paulo']
funcionarias_mulheres = ['Ana', 'Bárbara', 'Maria', 'Tatiana']

if nome == 'Fernando':
  print('Olá Fernando, você é o administrador do sistema!!!')
elif nome in funcionarias_mulheres:
  print(f'Bem vinda {nome}, você é uma usuária registrada no sistema.')
elif nome in funcionarios_homens:
  print(f'Bem vindo {nome}, você é um usuário registrado no sistema.')
else:
  print('Olá, você não está logado no sistema, suas permissões são restritas.')
  
     

nome = input('Digite o seu nome: ')

funcionarios_homens = ['Carlos', 'José', 'Paulo']
funcionarias_mulheres = ['Ana', 'Bárbara', 'Maria', 'Tatiana']

if nome == 'Fernando':
  # Se nome for igual a Fernando
  print('Olá Fernando, você é o administrador do sistema!!!')
elif nome in funcionarias_mulheres:
  # Se nome for um dos elementos da lista funcionarias_mulheres
  print(f'Bem vinda {nome}, você é uma usuária registrada no sistema.')
elif nome in funcionarios_homens:
  # Se nome for um dos elementos da lista funcionarios_homens
  print(f'Bem vindo {nome}, você é um usuário registrado no sistema.')
else:
  # Caso contrário
  print('Olá, você não está logado no sistema, suas permissões são restritas.')
  
     



veiculo1 = 'Gol'
veiculo2 = 'Corsa'
veiculo3 = 'Onibus'

cor1 = 'Branco'
cor2 = 'Vermelho'

if veiculo1 == 'Gol' or veiculo2 == 'Celta':
  print('Carro')
if veiculo1 == 'Gol' and cor1 == 'Branco':
  print('Gol Branco')
if veiculo1 == 'Onibus' and cor2 == 'Vermelho':
  print('Onibus Vermelho')

# Condição em or apenas uma das condicionais precisa ser verdadeira.
# Condicão em and as duas condicionais precisam serem verdadeiras.

     


veiculo1 = 'Gol'
veiculo2 = 'Corsa'
veiculo3 = 'Onibus'

cor1 = 'Branco'
cor2 = 'Vermelho'

if veiculo1 == 'Gol' or veiculo2 == 'Celta':
  # Se veiculo1 for igual a Gol ou veiculo2 for igual a Celta
  print('Carro')
if veiculo1 == 'Gol' and cor1 == 'Branco':
  # Se veiculo1 for igual a gol e cor1 for igual a Branco
  print('Gol Branco')
if veiculo1 == 'Onibus' and cor2 == 'Vermelho':
  # Se veiculo1 for igual a Onibus e cor2 for igual a Vermelho
  print('Onibus Vermelho')

     
