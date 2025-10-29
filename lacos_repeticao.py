# Os laços permitem repetir um bloco de código várias vezes. Existem dois tipos principais:

# Laço for

# O laço for é utilizado quando você sabe o número de iterações ou quer iterar sobre uma sequência (como uma lista, tupla, string, etc.).

# Exemplo de uso com uma lista:

for i in [1, 2, 3, 4, 5]:
    print(i)

# Este código imprime os números de 1 a 5. O laço percorre cada valor na lista e executa o bloco de código para cada item.

# Laço while

# O laço while é utilizado quando você deseja repetir um bloco de código enquanto uma condição for verdadeira.

# Exemplo de uso com uma condição:

contador = 0

while contador < 5:
    print(contador)
    contador += 1

# Neste caso, o laço continuará executando enquanto contador for menor que 5. A cada iteração, contador é incrementado em 1.

# Controle de Fluxo Adicional

# break: Utilizado para sair de um laço, interrompendo sua execução.

for i in range(10):
    if i == 5:
        break 
    print(i)

# continue: Utilizado para pular a iteração atual do laço e continuar para a próxima.

for i in range(5):
    if i == 3:
        continue  
    print(i)

# Resumo:

# Condicionais (if, elif, else) controlam o fluxo do programa com base em condições.

# Laços (for, while) repetem blocos de código.

# break e continue ajudam a controlar o fluxo dentro dos laços.