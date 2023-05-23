peso_peix = float(input("Digite o peso de peixes (em kg): "))

excs = max(0, peso_peix - 50)

mult= excs * 4.00

print("Excesso:", excs)
print("Multa:", mult)