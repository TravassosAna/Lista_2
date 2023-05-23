num= int(input("Digite um número inteiro: "))

primo = True
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
else:
    primo = False

if primo:
    print(num, "é primo.")
else:
    print(num, "não é primo.")
