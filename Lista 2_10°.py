dist = float(input("Digite a distância percorrida (em quilômetros): "))
comb = float(input("Digite a quantidade de combustível gasta (em litros): "))

consumo_m = dist / comb

gasto_comb = 4.50 * comb

print(f"Consumo médio: {consumo_m:.2f} km/l")
print(f"Gasto com combustível: R$ {gasto_comb:.2f}")