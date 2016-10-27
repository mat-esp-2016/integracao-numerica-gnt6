#Bibliotecas
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

N = list(range(10,1001,10))

#Retangulos

inicio = 0
fim = math.pi/2
areas = []
variação = []
verdadeira = math.sin(fim) - math.sin(inicio)

for numeros in N:
    
    intervalo = (fim - inicio)/(numeros - 1)
    dados = []
    for i in range(numeros):
        t = inicio + i*intervalo
        dados.append(math.cos(t))
        
    areas_do_retangulo = []

    for ponto in dados:
        areas_do_retangulo.append (ponto * intervalo)
    areas.append (sum(areas_do_retangulo))
    
for area in areas:
    variação.append (abs(area - verdadeira))
	
#Trapézios

inicio = 0
fim = math.pi/2
areas2 = []
variação2 = []
for numeros in N:
    
    intervalo = (fim - inicio)/(numeros - 1)
    dados = []
    for i in range(numeros):
        t = inicio + i*intervalo
        dados.append(math.cos(t))
        
    areas_do_trapezio = []

    a = 0

    for ponto in dados[:-1]:
        c = ((dados[a] + dados [a + 1])/2) * intervalo
        a = a + 1
        areas_do_trapezio.append (c)
        
    areas2.append (sum (areas_do_trapezio))
    
for area in areas2:
    variação2.append (1-area)

    
plt.plot (N, variação)
plt.plot (N, variação2 , c = "red")

red_patch = mpatches.Patch (color = 'red', label = 'Trapézios')
blue_patch = mpatches.Patch (color = 'blue', label = 'Retângulos')
plt.legend (handles = [blue_patch, red_patch])


plt.ylabel ("Erros")
plt.xlabel ("numero de dados")
plt.title("Erro de integração numérica")
plt.yscale('log')

#Salvando em png
plt.savefig("Erro de integração numérica.png", format = "png")