# 16) Uma universidade deseja fazer um levantamento a respeito de seu processo de seleção.
# Para cada curso, é fornecido um arquivo texto com o seguinte conjunto de valores:
# Nome do curso;
# Código do curso;
# Número de vagas;
# Número de candidatos do sexo masculino;
# Número de candidatos do sexo feminino
# Fazer um programa em Python que:
# • Calcule e escreva, para cada curso, o número de candidatos por vaga e a porcentagem de
# candidatos do sexo feminino (escreva também o código correspondente do curso);
# • Determine o maior número de candidatos por vaga e escreva esse número juntamente
# com o código do curso correspondente (supor que não haja empate);
# • Calcule e escreva o total de candidatos.

# Versão sem função
cursos = [
    {"nome": "Engenharia", "codigo": 101, "vagas": 50, "masculino": 80, "feminino": 20},
    {"nome": "Medicina", "codigo": 102, "vagas": 30, "masculino": 40, "feminino": 60},
    {"nome": "Direito", "codigo": 103, "vagas": 40, "masculino": 30, "feminino": 70},
]

total_candidatos = 0
maior_candidatos_por_vaga = 0
codigo_maior_candidatos_por_vaga = 0

for curso in cursos:
    total_candidatos_curso = curso["masculino"] + curso["feminino"]
    candidatos_por_vaga = total_candidatos_curso / curso["vagas"]
    porcentagem_feminino = (curso["feminino"] / total_candidatos_curso) * 100

    print(f"Curso: {curso['nome']}, Código: {curso['codigo']}")
    print(f"Candidatos por vaga: {candidatos_por_vaga:.2f}")
    print(f"Porcentagem de candidatas do sexo feminino: {porcentagem_feminino:.2f}%\n")

    if candidatos_por_vaga > maior_candidatos_por_vaga:
        maior_candidatos_por_vaga = candidatos_por_vaga
        codigo_maior_candidatos_por_vaga = curso["codigo"]

    total_candidatos += total_candidatos_curso

print(f"Maior número de candidatos por vaga: {maior_candidatos_por_vaga:.2f}, Código do curso: {codigo_maior_candidatos_por_vaga}")
print(f"Total de candidatos: {total_candidatos}")

# Versão com função
def calcular_estatisticas(cursos):
    total_candidatos = 0
    maior_candidatos_por_vaga = 0
    codigo_maior_candidatos_por_vaga = 0

    for curso in cursos:
        total_candidatos_curso = curso["masculino"] + curso["feminino"]
        candidatos_por_vaga = total_candidatos_curso / curso["vagas"]
        porcentagem_feminino = (curso["feminino"] / total_candidatos_curso) * 100

        print(f"Curso: {curso['nome']}, Código: {curso['codigo']}")
        print(f"Candidatos por vaga: {candidatos_por_vaga:.2f}")
        print(f"Porcentagem de candidatas do sexo feminino: {porcentagem_feminino:.2f}%\n")

        if candidatos_por_vaga > maior_candidatos_por_vaga:
            maior_candidatos_por_vaga = candidatos_por_vaga
            codigo_maior_candidatos_por_vaga = curso["codigo"]

        total_candidatos += total_candidatos_curso

    print(f"Maior número de candidatos por vaga: {maior_candidatos_por_vaga:.2f}, Código do curso: {codigo_maior_candidatos_por_vaga}")
    print(f"Total de candidatos: {total_candidatos}")

cursos = [
    {"nome": "Engenharia", "codigo": 101, "vagas": 50, "masculino": 80, "feminino": 20},
    {"nome": "Medicina", "codigo": 102, "vagas": 30, "masculino": 40, "feminino": 60},
    {"nome": "Direito", "codigo": 103, "vagas": 40, "masculino": 30, "feminino": 70},
]

calcular_estatisticas(cursos)