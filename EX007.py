#MÉDIA ARITIMETICA

name = str(input(f'Digite seu nome: '))

nota01 = int(input('Digite a primeira nota:'))
nota02 = int(input('Digite a sugunda nota:'))
nota03 = int(input('Digite a terceira nota: '))
media= (nota01+nota03+nota02)/3

print(f'Primeira prova = {nota01}, Segunda Prova = {nota02} Terceira Prova = {nota03}')
if media ==5:
    print('#' * 70)
    print(f'{name}, Você tem outra chance!, Sua Média final foi: {media}, Recuperação!')
    print('#' * 70)
elif media <5:
    print('#' * 70)
    print(f'Que pena {name}, Sua Média final foi: {media}, Reprovado')
    print('#' * 70)
else:
    print('#' * 70)
    print(f'Parabéns {name}, Sua Média final foi: {media}, Aprovado')
    print('#' * 70)