def conversor_bytes_megabytes(espaco):
    return espaco / (1024 ** 2)

def calcular_percentual_uso(espaco, espaco_total):
    return (espaco / espaco_total) * 100

def main():
    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()

    espacos = [int(usuario.split()[1]) for usuario in usuarios]
    espaco_total = sum(espacos)
    espaco_medio = espaco_total / len(usuarios)

    with open("relatorio.txt", "w") as arquivo:
        arquivo.write("Furg Uso do espaço em disco pelos usuários\n")
        arquivo.write("------------------------------------------------------------------------\n")
        arquivo.write("Nr. Usuário Espaço utilizado % do uso\n")

        for i, usuario in enumerate(usuarios, start=1):
            nome, espaco = usuario.split()
            espaco = int(espaco)
            espaco_mb = conversor_bytes_megabytes(espaco)
            percentual_uso = calcular_percentual_uso(espaco, espaco_total)

            arquivo.write(f"{i} {nome.ljust(15)} {espaco_mb:.2f} MB {percentual_uso:.2f}%\n")

        arquivo.write("\n")
        arquivo.write("Espaço total ocupado: {:.2f} MB\n".format(conversor_bytes_megabytes(espaco_total)))
        arquivo.write("Espaço médio ocupado: {:.2f} MB\n".format(conversor_bytes_megabytes(espaco_medio)))

main()
