# Em Python, funções são blocos de código reutilizáveis que podem ser definidos para realizar uma tarefa específica.
# A modularização é o processo de dividir o código em partes menores e mais gerenciáveis, 
# chamadas de funções ou módulos. Isso torna o código mais organizado, reutilizável e fácil de entender.

# Funções em Python

# Uma função em Python é definida usando a palavra-chave def, seguida pelo nome da função e 
# parênteses contendo os parâmetros (se houver).
# O bloco de código da função é indentado.

def nome_da_funcao(parâmetros):
    # Corpo da função
    # Código a ser executado
    return valor

# Parâmetros: São valores que você passa para a função quando a chama.
# Return: A palavra-chave return é usada para retornar um valor da função 
# (não é obrigatória, se você não usar, a função retornará None por padrão).

# Exemplo de Função Simples:

def saudacao(nome):
    return f"Olá, {nome}!"

# Chamando a função
resultado = saudacao("Carlos")
print(resultado)  # Saída: Olá, Carlos!

# Neste exemplo:

# A função saudacao recebe um parâmetro nome e retorna uma mensagem personalizada.
# O valor retornado pela função é armazenado na variável resultado e impresso.

# Função com Vários Parâmetros:
def soma(a, b):
    return a + b

# Chamando a função
resultado = soma(5, 3)
print(resultado)  # Saída: 8

# Funções com Parâmetros Opcionais e Padrão
# Você pode definir valores padrão para os parâmetros de uma função, caso o usuário não forneça um valor.

def saudacao(nome="Visitante"):
    return f"Olá, {nome}!"

print(saudacao())  # Saída: Olá, Visitante!
print(saudacao("João"))  # Saída: Olá, João!

# No exemplo, o parâmetro nome tem um valor padrão de "Visitante", que será usado se a função for chamada sem argumentos.

# Funções com Número Variável de Argumentos

# Em Python, você pode passar um número variável de argumentos usando o operador * para uma lista de argumentos ou ** 
# para um dicionário de argumentos.

# Exemplo com *args (Argumentos Posicionais Variáveis):

def somar(*args):
    return sum(args)

# Chamando a função
resultado = somar(1, 2, 3, 4)
print(resultado)  # Saída: 10

# Neste caso, *args permite passar qualquer número de argumentos para a função.

# Exemplo com **kwargs (Argumentos Nomeados Variáveis):

def apresentar(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função
apresentar(nome="Maria", idade=25)
# Saída:
# nome: Maria
# idade: 25

# Aqui, **kwargs permite passar argumentos nomeados para a função como um dicionário.



# Modularização

# Modularização significa dividir o código em módulos ou arquivos separados para que ele se torne mais organizado e reutilizável.

# Como Funciona a Modularização:

# Definir funções em um módulo: Você pode criar um arquivo Python (por exemplo, mimodulo.py) e colocar funções ou classes nele.

# Importar e usar o módulo: Em outro arquivo Python, você pode importar o módulo usando a palavra-chave import.

# Exemplo de Modularização:

# Arquivo matematica.py:

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

# Arquivo principal programa.py:

import matematica  # Importando o módulo

resultado_soma = matematica.soma(10, 5)
resultado_subtracao = matematica.subtrai(10, 5)

print(f"Soma: {resultado_soma}")
print(f"Subtração: {resultado_subtracao}")



# Funções Lambda (Funções Anônimas)

# As funções lambda são funções simples e anônimas (sem nome) que podem ser criadas com a palavra-chave lambda. 
# Elas são úteis quando você precisa de uma função pequena e de uso temporário.

# Exemplo de Função Lambda:

multiplicar = lambda x, y: x * y

print(multiplicar(3, 4))
# A função lambda é definida com a sintaxe lambda argumentos: expressão, e retorna o valor da expressão.

# Resumo:

# Funções: Permitem encapsular blocos de código que podem ser reutilizados. São definidas com def e podem ter parâmetros e um valor de retorno.

# Modularização: Dividir o código em módulos para tornar o programa mais organizado. Você pode importar funções de outros arquivos para reutilizá-las.

# Funções Lambda: Funções curtas e anônimas, úteis para tarefas simples.

# Parâmetros Variáveis: Permitem passar um número flexível de argumentos.