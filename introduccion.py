#requerimientos mínmos 
minimo_dinero = 20000
minimo_regalos = 15000
minimo_viajes = 2

#crear aplucacion para que las sugar mommies compitan por nosotros
input_dinero = input("¿Cuánto dinero dispuesta al mes?: ")
input_regalos = input("¿Cuánto dinero en regalos dispuesta al mes?: ")
input_viajes = input("¿Cuántos viajes dispuesta al semestre?: ")

if(int(input_dinero) >= minimo_dinero or int(input_regalos) >= minimo_regalos or int(input_viajes) >= minimo_viajes):
    print('¡Puedes ser mi Sugar Mommy!')
else:
    print('No puedes ser mi mamasita.. tacaña')