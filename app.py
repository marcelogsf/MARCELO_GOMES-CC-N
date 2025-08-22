# listas de variaveis
alturas = []
soma_homens = 0
qtd_homens = 0
qtd_mulheres = 0

# coletar os dados e repeti-los
for i in range(1, 16):
    print(f"nPessoa {i}:")
    altura = float(input("Qual sua altura? (em metros): "))
    genero = input("Qual seu gênero? (M/F): ").strip().upper()

    # guardar as alturas na lista
    alturas.append(altura)

    # verificar os gêneros
    if genero == "M":
        soma_homens += altura
        qtd_homens += 1
    elif genero == "F":
        qtd_mulheres += 1
    else:
        print("Gênero inválido, considere apenas M ou F.")

# resultados
maior_altura = max(alturas)
menor_altura = min(alturas)

if qtd_homens > 0:
    media_homens = soma_homens / qtd_homens
else:
    media_homens = 0

print("\n--- RESULTADOS ---")
print(f"A maior altura do grupo: {maior_altura:.2f} m")
print(f"A menor altura do grupo: {menor_altura:.2f} m")
print(f"A Média de altura dos homens: {media_homens:.2f} m")
print(f"Número de mulheres no grupo: {qtd_mulheres}")