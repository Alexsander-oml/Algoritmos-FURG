# 21) Crie uma função em Python que receba por parâmetro uma string e uma letra. Retorne a
# string equivalente à enviada como parâmetro, mas sem a letra informada. Por exemplo:
# retira(“Antonia Piedade”,”a”) —> “ntoni Piedde”
# ● Crie a função usando qualquer recurso Python, como split, search e etc;
# ● Crie a função usando apenas recursos básicos, sem as funções para manipulação de
# strings.

def retira(string, letra):
    return string.replace(letra, '').replace(letra.upper(), '')

# Exemplo de uso
resultado = retira("Antonia Piedade", "a")
print(resultado)  # Output: "ntoni Piedde"

# Versão sem usar funções de manipulação de strings
def retira_basico(string, letra):
    resultado = ""
    for char in string:
        if char != letra and char != letra.upper():
            resultado += char
    return resultado

# Exemplo de uso
resultado_basico = retira_basico("Alexsander", "a")
print(resultado_basico)  # Output: "lexsnder"