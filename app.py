from funcoes.funcoes import *
from funcoes.time import *

exibir_boas_vindas()

opcao = 0

while opcao != 6:
    esperar_tempo_curto()
    exibir_menu_dinamico()
    opcao = int(input("Digite sua opção: "))

    if opcao < 1 or opcao > 6:
        print("Opção inválida!")
        esperar_tempo_medio()

    elif opcao == 1:
        mensagem_setor_verificar_saldo()
        verificar_saldo()
        esperar_tempo_medio()

    elif opcao == 2:
        mensagem_setor_depositar_valor()
        valor = float(input("Digite o valor a depositar: "))
        deposita_valor(valor)
        esperar_tempo_medio()

    elif opcao == 3:
        mensagem_setor_sacar_valor()
        valor = float(input("Digite o valor a ser sacado: "))
        sacar_valor(valor)
        esperar_tempo_medio()

    elif opcao == 4:
        mensagem_setor_transferir_valor()
        valor = float(input("Digite o valor a ser transferido: "))
        transferir_um_valor(valor)
        esperar_tempo_medio()

    elif opcao == 5:
        mensagem_setor_avaliar_aplicativo()
        nota = int(input("Digite sua avaliação (1 a 10): "))
        avaliar_aplicativo(nota)
        esperar_tempo_medio()

esperar_tempo_longo()
print("Saindo do aplicativo. Obrigado por usar nosso banco digital!")
esperar_tempo_medio()
print("Estamos com você! ❤")