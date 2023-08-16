#Gerador de senhas automatico.

import random

letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "@!#$%ˆ&*()"

soma_caracteres = letras_minusculas + letras_maiusculas + numeros + simbolos

tamanho_da_senha = 12

senha = "".join(random.sample(soma_caracteres,tamanho_da_senha))

print("Minha senha: ",senha)


