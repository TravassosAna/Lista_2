print()
print("TABELA DE CORES:")
print("Verde: 10,00")
print("Azul: 20,00")
print("Amarelo: 30,00")
print("Vermelho: 40,00")
print()
tabela_precos = { 
    "Verde": "R$ 10,00",
    "Azul": "R$ 20,00",
    "Amarelo": "R$ 30,00",
    "Vermelho": "R$ 40,00"
}

cor = input("Digite a cor do jogo: ")

valor = tabela_precos.get(cor, "Cor inválida")

print("Preço:", valor)