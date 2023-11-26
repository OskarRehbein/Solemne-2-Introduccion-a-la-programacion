
import random

numero_colaboradores = int(input("Ingrese el numero de colaboradores: "))
dias_del_mes = 30
turnos_colaboradores = [[False]*dias_del_mes for _ in range(numero_colaboradores)]
pago_por_hora = int(input("Ingrese el pago por hora en CLP: "))
horas_por_turno = int(input("Ingrese la duracion de un turno laborar: "))

lista_de_turno = []
backup_lista_de_turno = []
matriz_paga = []

def informacion_fin_de_mes():
    for i in range(numero_colaboradores):
        print(f"El colaborador {i+1} trabajara los dias: ", end=" ")
        pago = horas_por_turno * pago_por_hora * turnos_trabajados[i]
        for j in range(dias_del_mes):
            if turnos_colaboradores[i][j] == True:
                print(f"{j+1} ", end="")
        print(f"del mes ({turnos_trabajados[i]} turnos / {turnos_trabajados[i] * horas_por_turno} horas trabajadas) para una paga de {pago} CLP")
        matriz_paga.append(pago)

for dia in range(dias_del_mes):
    if dia == 6:
        continue
    elif dia == 13:
        continue
    elif dia == 20:
        continue
    elif dia == 27:
        continue

    while True:
        x = random.randint(0, numero_colaboradores-1)
        if not x in lista_de_turno:
            lista_de_turno.append(x)
            break
        
    turnos_colaboradores[lista_de_turno[len(lista_de_turno)-1]][dia] = True

    if len(lista_de_turno) == numero_colaboradores:
        lista_de_turno.clear()

turnos_trabajados = []
suma_turnos = 0
for colaboradores in range(0,numero_colaboradores):
    for dias in range(0,dias_del_mes):
        suma_turnos += turnos_colaboradores[colaboradores][dias]
    turnos_trabajados.append(suma_turnos)
    suma_turnos = 0

informacion_fin_de_mes()
pago_final = 0
for i in range(len(matriz_paga)):
    pago_final += matriz_paga[i]

print(f"El costo final del mes es de {pago_final} CLP")

