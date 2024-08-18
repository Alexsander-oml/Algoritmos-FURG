# Manipulação de Strings em Python

Este documento fornece uma lista abrangente de métodos para manipulação de strings em Python, juntamente com exemplos práticos e dicas para casos em que você não possa usar algum desses métodos.

## Métodos de Strings

### Conversão de Maiúsculas e Minúsculas

- **`str.upper()`**: Converte todos os caracteres da string para maiúsculas.
  ```python
  "texto".upper()  # 'TEXTO'
str.lower(): Converte todos os caracteres da string para minúsculas.

python
Copiar código
"TEXTO".lower()  # 'texto'
str.title(): Converte a primeira letra de cada palavra em maiúscula.

python
Copiar código
"texto de exemplo".title()  # 'Texto De Exemplo'
str.capitalize(): Converte a primeira letra da string para maiúscula e o restante para minúsculas.

python
Copiar código
"texto".capitalize()  # 'Texto'
Manipulação de Espaços
str.strip([chars]): Remove espaços em branco (ou caracteres específicos) do início e do fim da string.

python
Copiar código
"  texto  ".strip()  # 'texto'
str.lstrip([chars]): Remove espaços em branco (ou caracteres específicos) do início da string.

python
Copiar código
"  texto  ".lstrip()  # 'texto  '
str.rstrip([chars]): Remove espaços em branco (ou caracteres específicos) do fim da string.

python
Copiar código
"  texto  ".rstrip()  # '  texto'
Substituição e Localização
str.replace(old, new[, count]): Substitui todas (ou as primeiras count ocorrências de) instâncias de uma substring por outra.

python
Copiar código
"texto velho".replace("velho", "novo")  # 'texto novo'
str.find(sub[, start[, end]]): Retorna o menor índice onde a substring sub é encontrada. Retorna -1 se não encontrado.

python
Copiar código
"texto".find("e")  # 1
str.rfind(sub[, start[, end]]): Retorna o maior índice onde a substring sub é encontrada. Retorna -1 se não encontrado.

python
Copiar código
"texto texto".rfind("e")  # 6
str.index(sub[, start[, end]]): Retorna o menor índice onde a substring sub é encontrada. Levanta uma exceção ValueError se não encontrado.

python
Copiar código
"texto".index("e")  # 1
str.rindex(sub[, start[, end]]): Retorna o maior índice onde a substring sub é encontrada. Levanta uma exceção ValueError se não encontrado.

python
Copiar código
"texto texto".rindex("e")  # 6
Divisão e Junção
str.split([sep[, maxsplit]]): Divide a string em uma lista de substrings usando o delimitador sep. Se maxsplit for especificado, divide em no máximo maxsplit partes.

python
Copiar código
"texto de exemplo".split()  # ['texto', 'de', 'exemplo']
str.rsplit([sep[, maxsplit]]): Divide a string em uma lista de substrings usando o delimitador sep, mas começa a dividir a partir do fim da string.



"texto de exemplo".rsplit(' ', 1)  # ['texto de', 'exemplo']
str.splitlines([keepends]): Divide a string em uma lista de linhas. Se keepends for True, inclui os caracteres de nova linha nas linhas resultantes.



"linha 1\nlinha 2".splitlines()  # ['linha 1', 'linha 2']
Preenchimento e Alinhamento
str.zfill(width): Preenche a string com zeros à esquerda para atingir a largura especificada.


 
"42".zfill(5)  # '00042'
str.ljust(width[, fillchar]): Alinha a string à esquerda em um campo de largura width preenchido com o caractere fillchar (padrão é espaço).


"texto".ljust(10, '-')  # 'texto-----'
str.rjust(width[, fillchar]): Alinha a string à direita em um campo de largura width preenchido com o caractere fillchar (padrão é espaço).


"texto".rjust(10, '-')  # '-----texto'
str.center(width[, fillchar]): Centraliza a string em um campo de largura width preenchido com o caractere fillchar (padrão é espaço).

"texto".center(10, '-')  # '--texto---'
Verificação de Propriedades
str.startswith(prefix[, start[, end]]): Retorna True se a string começar com o prefixo especificado.

 
"texto".startswith("te")  # True
str.endswith(suffix[, start[, end]]): Retorna True se a string terminar com o sufixo especificado.


 
"texto".endswith("to")  # True
str.isdigit(): Retorna True se todos os caracteres na string forem dígitos.


"123".isdigit()  # True
str.isalpha(): Retorna True se todos os caracteres na string forem letras.


"texto".isalpha()  # True
str.isalnum(): Retorna True se todos os caracteres na string forem letras ou dígitos.



"texto123".isalnum()  # True
str.isspace(): Retorna True se todos os caracteres na string forem espaços em branco.

"   ".isspace()  # True
str.islower(): Retorna True se todos os caracteres na string estiverem em minúsculas.


"texto".islower()  # True
str.isupper(): Retorna True se todos os caracteres na string estiverem em maiúsculas.


"TEXTO".isupper()  # True
str.istitle(): Retorna True se a string estiver em formato de título (primeira letra de cada palavra em maiúscula).


"Texto De Exemplo".istitle()  # True
Outros Métodos Úteis
str.swapcase(): Retorna uma nova string com todos os caracteres em maiúsculas trocados por minúsculas e vice-versa.


"TeXtO".swapcase()  # 'tExTo'
str.expandtabs(tabsize=8): Substitui os caracteres de tabulação (\t) na string por espaços. O parâmetro tabsize define a largura da tabulação em espaços.


"texto\tmais texto".expandtabs(4)  # 'texto   mais texto'
Dicas e Macetes
Inversão de String: Se precisar inverter uma string, você pode usar o fatiamento:


"texto"[::-1]  # 'otxet'
Verificação de Substrings: Se in não estiver disponível, você pode usar o método find() e verificar se o resultado é diferente de -1:


if "sub" in "string":  # Com 'in'
    print("
