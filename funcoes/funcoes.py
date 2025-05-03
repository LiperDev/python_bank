saldo = 0
avaliacoes = []

def exibir_boas_vindas():
    print("Seja bem-vindo(a) à sua conta bancária!")

def exibir_menu_dinamico():
    print("1- verificar saldo atual\n"
          "2- depositar valor\n"
          "3- sacar valor\n"
          "4- transferir valor\n"
          "5- avaliar banco digital\n"
          "6- sair do aplicativo"
          )

def mensagem_setor_verificar_saldo():
    print("Você selecionou: verificar saldo!")

def mensagem_setor_depositar_valor():
    print("Você selecionou: depositar valor!")

def mensagem_setor_sacar_valor():
    print("Você selecionou: sacar valor!")

def mensagem_setor_transferir_valor():
    print("Você selecionou: transferir valor!")

def mensagem_setor_avaliar_aplicativo():
    print("Você selecionou: avaliar aplicativo!")

def verificar_saldo():
    global saldo
    print("Seu saldo atual é igual a: R$", saldo, ".")

def deposita_valor(valor):
    global saldo

    if valor <= 0:
        print("Valor impossível de transferir!")
    else:
        saldo = saldo + valor
        print("Valor depositado com sucesso!")

def sacar_valor(valor):
    global saldo

    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo = saldo - valor
        print("Valor sacado com sucesso!")

def transferir_um_valor(valor):
    global saldo

    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo = saldo - valor
        print("Transferência bem sucedida!")

def valores_validos_avaliacao():
    print("Por favor, digite um valor de 1 a 10")

def avaliar_aplicativo(valor):
    if valor <= 0:
        print("Valor inválido!")
        valores_validos_avaliacao()

    else:
        avaliacoes.append(valor)
        soma = sum(avaliacoes)
        media = soma / len(avaliacoes)
        print("Média das avaliações: ", media)