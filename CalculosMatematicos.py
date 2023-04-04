import math

#Formula do Teorema de Pitágoras Fórmula do Teorema de Pitágoras: a² + b² = c², onde a e b são os comprimentos dos catetos de um triângulo retângulo
# e c é o comprimento da hipotenusa.
a = 3
b = 4
c = ((a ** 2) + (b ** 2)) ** 0.5
print(c) # saída: 5.0


#Fórmula do Perímetro de um círculo:
r = 5
perimetro = 2 * math.pi * r
print(perimetro) # saída: 31.41592653589793


#Fórmula da Área do círculo:

r = 5
area = math.pi * (r ** 2)
print(area) # saída: 78.53981633974483


#Fórmula do Volume de uma esfera:
r = 3
volume = (4 / 3) * math.pi * (r ** 3)
print(volume) # saída: 113.09733552923254

#Fórmula de Bhaskara:
a = 1
b = -5
c = 6
delta = (b ** 2) - (4 * a * c)
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(x1, x2) # saída: 3.0, 2.0

#Fórmula da Regra de Três Simples:
a = 2
b = 4
c = 5
d = (b * c) / a
print(d) # saída: 10.0


#Fórmula da Média Aritmética:

notas = [7, 8, 6, 9, 10]
media = sum(notas) / len(notas)
print(media) # saída: 8.0

#Fórmula do Juros Simples:
P = 1000
i = 0.05
t = 2
juros = P * i * t
print(juros) # saída: 100.0


#Fórmula do Juros Compostos:
P = 1000
i = 0.05
t = 2
juros = P * ((1 + i) ** t - 1)
print(juros) # saída: 105.12762815624996

#Fórmula da Conversão de unidades:
celsius = 30
fahrenheit = (9 / 5) * celsius + 32
print(fahrenheit) # saída: 86.0
