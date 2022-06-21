import random
escolha = 'S'
while escolha == 'S':
  print('\nBem vindo ao jogo da adivinhação!')
  num = random.randint(0,101)
  adiv = int(input('\n● Escolha um número entre 0 e 100: '))
  qtd_tenta = 1
  while adiv != num:
    qtd_tenta+=1
    if adiv > num:
      print('\nO palpite é maior que o número secreto. Tente novamente!')
    else:
      print('\nO palpite é menor que o número secreto. Tente novamente!')
    adiv = int(input('\n● Escolha um número entre 0 e 100: '))
  else:
    print('\n****************************************\nParabéns!!! O número correto é:',num,'\nQuantidade de tentativas:',qtd_tenta,'\n****************************************')
  escolha = input('\n● Jogar novamente? S ou N: ')
else:
  print('\nJogo encerrado.')
