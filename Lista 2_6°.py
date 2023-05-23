codigo = int(input("Digite o código do operário: "))
horas_t = float(input("Digite o número de horas trabalhadas: "))

salario = horas_t * 10.00

if horas_t > 50:
    horas_e = horas_t - 50
    pagamento_e= horas_e * 20.00
else:
    horas_e = 0
    pagamento_e = 0

print("Salário total:", salario)
print("Salário excedente:", pagamento_e)