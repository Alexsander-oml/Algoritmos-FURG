# 22) Crie uma função em Python que receba por parâmetro uma lista e uma letra. Retorne
# uma lista equivalente à enviada como parâmetro, mas sem a letra informada. A ordem dos
# elementos deve ser mantida. Por exemplo:
# retira([a,b,c,a,f,a,a,k],a) —> [b,c,f,k]

# Lista e letra a serem usadas
lista = ['a', 'b', 'c', 'a', 'f', 'a', 'a', 'k']
letra = 'a'

# Lista resultante sem a letra informada
resultado = [elemento for elemento in lista if elemento != letra] # significa que o elemento será adicionado na lista resultado se ele for diferente da letra informada

# Exibindo o resultado
print(resultado)  # Saída: ['b', 'c', 'f', 'k']