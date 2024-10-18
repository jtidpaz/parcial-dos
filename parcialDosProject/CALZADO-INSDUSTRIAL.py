# se crea las variables
def calcularBonificacion(salario,desempeno,nivel):
 if nivel=='directivo':
    if desempeno =='alto':
        bonificacion= 0.20 * salario
    elif desempeno == 'medio':
        bonificacion= 0.10 * salario
    else:
        bonificacion= 0
 elif nivel =='operativo':
     if desempeno =='alto':
         bonificacion = 0.15 * salario
     elif desempeno == 'medio':
          bonificacion = 0.05 * salario
     else: bonificacion= 0
 else:bonificacion=0
 total = salario+bonificacion
 return total,bonificacion

salario=float (input("Salario Base Mensual $: "))
nivel= input("Cargo  empleado: ")
desempeno= input("Nivel de desempeño : ")


total, bonificacion=calcularBonificacion(salario,desempeno,nivel)
print("-------Resumen del Pago---------")
print(f"Cargo : .{nivel}".lower())
print(f"Nivel de Desempeño : {desempeno}".lower())
print(f"Salario Base : ${salario}")
print(f"Bonificacion : ${bonificacion}")
print(f"Total a Recibir: ${total}"),print("-------------------------")


