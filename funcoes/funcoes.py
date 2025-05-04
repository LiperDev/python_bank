from funcoes.time import *

saldo = 0
avaliacoes = []
transferidos = []
contador_valor_depositado = 0
contador_valor_sacado = 0
contador_valor_transferido = 0

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
    global contador_valor_depositado

    if valor <= 0:
        print("Valor impossível de transferir!")
    else:
        saldo = saldo + valor
        contador_valor_depositado = contador_valor_depositado + 1
        print(contador_valor_depositado, ": depósito bem sucedido!")
        temporizador(1)
        print("você depositou: R$", valor)
        temporizador(1)
        print("saldo atual: R$", saldo)

def sacar_valor(valor):
    global saldo
    global contador_valor_sacado

    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo = saldo - valor
        contador_valor_sacado = contador_valor_sacado + 1
        print(contador_valor_sacado, ": saque bem sucedido!")
        temporizador(1)
        print("você sacou: R$", valor)
        temporizador(1)
        print("saldo atual: R$", saldo)

def transferir_um_valor(valor):
    global saldo
    global contador_valor_transferido

    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo = saldo - valor
        transferidos.append(valor)
        exibir_valores_transferidos()
        contador_valor_transferido = contador_valor_transferido + 1
        print(contador_valor_transferido, ": transferência bem sucedida!")
        temporizador(1)
        print("você transferiu: R$", valor)
        temporizador(1)
        print("saldo atual: R$", saldo)

def valores_validos_avaliacao():
    print("Por favor, digite um valor de 1 a 10")

def avaliar_aplicativo(valor):
    if valor <= 0 or valor > 10:
        print("Valor inválido!")
        valores_validos_avaliacao()

    else:
        avaliacoes.append(valor)
        soma = sum(avaliacoes)
        media = soma / len(avaliacoes)
        print("Média das avaliações: ", media)


def exibir_valores_transferidos():
    print("Exibindo valores transferidos... ")
    print(transferidos)