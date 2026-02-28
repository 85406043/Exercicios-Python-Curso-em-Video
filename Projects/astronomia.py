import os
from time import sleep
import webbrowser as wbr

#VARIAVEIS
contando = 0

#FUNCTIONS
def limpar_tela():
    os.system('clear')#Windows: cls & Linux: clear

def sair():
    os.system('exit')

#def resposta == if de 'Que legal'
def escolha2():
    while True:
        limpar_tela()
        escolha1 = input('''\nVou começar te mostrando algumas opções disponiveis:

    [ 1 ] Buracos negros
    [ 2 ] Nebulosas
    [ 3 ] Galaxias
    [ 4 ] Estrelas de Neutron

=> ''')
        remover = escolha1.strip()
        if remover == '1':
            print('Buraco negro')
            print('Redirecionando...')
            wbr.open('https://pt.wikipedia.org/wiki/Buraco_negro')
            #quit()
        elif remover == '2':
            print('Nebulosas')
            print('Redirecionando...')
            wbr.open('https://pt.wikipedia.org/wiki/Nebulosa')
            #quit()
        elif remover == '3':
            print('Galáxias')
            print('Redirecionando...')
            wbr.open('https://pt.wikipedia.org/wiki/Gal%C3%A1xia')
            #quit()
        elif remover == '4':
            print('estrelas de neutron')
            print('Redirecionando...')
            wbr.open('https://pt.wikipedia.org/wiki/Estrela_de_n%C3%AAutrons')
            #quit()
        else:
            erro_escolha2()
# def == resposta if 'Que legal'
def erro_escolha2():
    while True:
        limpar_tela()
        sleep(1)
        print('\033[1;31mOpção Inválida\033[m\n')
        sleep(1)
        temcer = input('Deseja sair ? [\033[1;32mS\033[m/\033[1;31mN\033[m]')
        remover = temcer.strip()
        capitalizar = remover.upper()
        if capitalizar == 'S':
            print('Saindo...')
            sleep(3)
            quit()
        elif capitalizar == 'N':
            print('Retornando...')
            sleep(2)
            escolha2()
        else:
            sleep(1)
            print('Digite \033[1;32mS\033[m ou \033[1;31mN\033[m !')
            sleep(4)

#primeiro if de resposta == 'Que legal'
def astro_universo():
    contando2 = 0
    while True:
        limpar_tela()
        sleep(1)
        pergunta1 = input('''Então você gosta do Universo ?

    [ 1 ] Sim
    [ 2 ] Não

=> ''')
        remover = pergunta1.strip()
        if remover == '1':
            sleep(1)
            print('Então você está no lugar certo')
            sleep(1)
            #def escolha2()
            escolha2()

        elif remover == '2':
            sleep(1)
            print('\nSinto muito, esse script não é pra você !\n')
            sleep(1)
            print('Saindo...')
            sleep(2)
            exit()
        elif contando2 == 2 :
            sleep(1)
            print('Está teimando, estou saindo !')
            sleep(1)
            print('Saindo...')
            sleep(2)
            quit()
        else:
            #contando2 += 1
            sleep(1)
            print('\n\033[1;31mEscolha uma opção valida !\033[m')
            sleep(3)
            limpar_tela()

#segundo elif == tentativa_2() == 'Melhoras'
def tentativa_2():
    while True:
        sleep(1)
        limpar_tela()
        tentativa2 = input('Não quer tentar ficar melhor\naprendendo um pouco sobre o Universo ? [\033[1;32mS\033[m/\033[1;31mN\033[m]\n=> ')
        remover = tentativa2.strip()
        capitalizar = remover.capitalize()
        if capitalizar == 'S':
            sleep(1)
            print('Então vamos lá')
            sleep(3)
            astro_universo()
        elif capitalizar == 'N':
            sleep(1)
            erro_tentativa2()
        else:
            print('Escolha uma opção válida !')

#segundo elif == tentativa_2() == 'Melhoras'
def erro_tentativa2():
    while True:
        limpar_tela()
        sleep(1)
        pergunta = input('Deseja sair ? [S/N]')
        remover = pergunta.strip()
        capitalizar = remover.capitalize()
        if capitalizar == 'S':
            sleep(1)
            print('Até logo !')
            sleep(0.5)
            print('Saindo...')
            sleep(3)
            quit()
        elif capitalizar == 'N':
            sleep(1)
            print('Retornando...')
            sleep(2.5)
            tentativa_2()
        else:
            sleep(1)
            print('Escolha uma alternativa válida !\n')
            sleep(2)

# LAÇO WHILE, JUNTO COM OS IFS INICIAIS

while True :
    limpar_tela()
    print("\033[1;34mASTRONOMIA\033[m\n")
    sleep(1)
    nome = input('''Como Estás?

    { 1 } Estou bem!
    { 2 } Não estou bem!

=> ''')
    remover = nome.strip()
    if remover == "1":
        sleep(1)
        print("\n\033[1;32mQue legal !\033[m")
        sleep(3)
        astro_universo()


    elif remover == "2":
        sleep(1)
        print("\nMelhoras !")
        sleep(1)
        tentativa_2()


    elif contando == 2:
        sleep(1)
        print('\nVocê não tem interesse no assunto')
        sleep(1)
        print('\n\033[1;31mSaindo...\033[m')
        sleep(3)
        quit()

    else:
        #contando += 1
        sleep(1)
        print("\n\033[1;31mPor favor, escolha uma opção !\n\033[m")
        sleep(3)
        limpar_tela()
        