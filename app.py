
from random import randint

inicio = 'INICIANDO O JOGO'
endgame =' FIM DE JOGO'
print(f'{inicio:#^40}\n')

random = randint(0,100) #vai gerar um numero pra gente entre 0 a 100
chute = 0
chances = 10


while chute != random:
    chute = input("Chute um número entre 0 a 100: ")
    if chute.isnumeric():
        chute = int(chute)
        chances = chances-1
        if chute ==random:
            print('')
            print('Parabéns, Você venceu! O número era {} e você ainda tinha {} chances.'.format(random,chances))
            print('')
            break
        else:
            print('')
            if chute> random:
                print('Você errou!! Dica: É um numero menor.')
            else:
                print('Você errou!! Dica: É um numero maior.')
            print('Você ainda possui {} chances'.format(chances))
            print('')
        if chances==0:
            print('')
            print('Suas chances acabaram, você perdeu!')
            print('')
            break
print(f'{endgame:#^40}\n')
