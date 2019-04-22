#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, random


def jogar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("lista.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)
    arquivo.close()

    select = random.randrange(0,len(palavras))
    palavra_secreta = palavras[select]

    #palavra_secreta = input("Digite a palavra secreta:\n").upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print("Com {} letras:".format(len(palavra_secreta)))
    print(letras_acertadas)
    print("")

    while not enforcou and not acertou:
        chute = input("Qual letra?\n").strip().upper()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == chute:
                    letras_acertadas[index] = letra
                index += 1
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            erros += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        print("Você venceu!")
    elif enforcou:
        print("Você perdeu!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
