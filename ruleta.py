import numpy as np

#Ruleta sin ceros
total_casillas = 38
rojos = [x for x in range(1,total_casillas+1) if x % 2 == 1]
negros = [x for x in range(1,total_casillas+1) if x % 2 == 0]

ruleta_sin_ceros = rojos + negros

def girar_ruleta(ruleta,rojos,negros):
    ruleta = ruleta + ['0','00']
    numero_ganador = np.random.choice(ruleta)
    if numero_ganador in rojos:
        color_ganador = 'Rojo'
    elif numero_ganador in negros:
        color_ganador = 'Negro'
    else:
        color_ganador = 'Verde'
    return color_ganador

#simulacion de 1000 ruletas
simulaciones = []
n_sim = 1000
for i in range(n_sim):
    simulaciones.append(girar_ruleta(ruleta_sin_ceros,rojos,negros))

#conocer el número de ROJO
num_rojo = simulaciones.count('Rojo')
print(f'Número de Rojos: {num_rojo}')

#conocer el número de NEGRO
num_negro = simulaciones.count('Negro')
print(f'Número de Negros: {num_negro}')

num_verde = simulaciones.count('Verde')
print(f'Número de Verdes: {num_verde}')

#Esperanza
apuesta = 50
balance_final = 50*num_rojo + (-1*50)*num_negro + (-1*50)*num_verde
print(f'Balance Final: {balance_final}')


