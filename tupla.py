#ESTE programa lê TRÉS valores pelo teclado e guarde-os em uma tupla.
#No final mostrará quantas vezes apareceu o valor 9, em que posição foi digitado o primeiro valor 3 e quais foram os números pares.
cont = 0
while True:
    try:
        seq = ((int(input("VALOR DA POSIÇÃO 1:"))),
                 (int(input("VALOR DA POSIÇÃO 2:"))),
                 (int(input("VALOR DA POSIÇÃO 3:"))))
        break
    except ValueError:
        print("DIGITE APENAS NÚMEROS INTEIROS.Vamos começar novamente...")
print("\n1)Quantas vezes o número 9 aparece nessa tupla?")
if 9 in seq:
    print(f"O número 9 aparece {seq.count(9)} vez (vezes) nesta sequência.")
else:
    print(f"O número 9 não aparece nesta tupla.")
print("\n2)Em que posição foi digitado o primeiro valor 3?")
if 3 in seq:
    print(f"O número 3 aparece pela primeira vez na posição {seq.index(3)+1}.")
else:
    print(f"Nenhum número 3 aparece nesta tupla.")
print(f"\nQuais foram os números pares?")
for c in seq:
    if c % 2 == 0:
        print(f"{c} - ", end=(""))
    elif c % 2 == 1:
        cont += 1
        if cont == 3:
            print("Não há nenhum número par nesta sequência.")
