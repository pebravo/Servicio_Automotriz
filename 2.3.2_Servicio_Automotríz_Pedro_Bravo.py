rut=input('Ingrese Rut: ')
nombre_completo=input('Ingrese Nombre completo: ')
marca=input('Ingrese Marca del automovil: ')
modelo=input('Ingrese Modelo: ')

print('los servicios posibles para contratar son los sigte: ')
print('---------------------------------------------------------')
print('|servicio \t\t\t tiempo de espera \t|')
print('---------------------------------------------------------')
print('|Revision de 1.000Km \t\t\t 2 horas \t|')
print('|Cambio de aceite \t\t\t 1 hora \t|')
print('|Revision de frenos \t\t\t 0.5 horas \t|')
print('|Revision de correas \t\t\t 0.5 horas \t|')
print('|Revision de luces \t\t\t 0.2 horas \t|')
print('|Revision de direccion \t\t\t 0.5 horas \t|')
print('|Lavado de tapis (sin costo) \t\t 0.5 horas \t|')
print('---------------------------------------------------------')


opcion=0
arreglo=[]
while(opcion !=8):
    opcion=int(input('Eliga su opcion y presione enter(8 para salir):'))
    arreglo.append(opcion)
               


tiempo=0.0

for op in arreglo:
    if op ==1:
        tiempo +=2.0
    elif op ==2:
        tiempo +=1.0
    elif op ==3:
        tiempo +=0.5
    elif op ==4:
        tiempo +=0.5
    elif op ==5:
        tiempo +=0.2
    elif op ==6:
        tiempo +=0.5
    elif op ==7:
        tiempo +=0.5

cantidad=0
for op in arreglo:
    if op ==1:
        cantidad +=1
    elif op ==2:
        cantidad +=1
    elif op ==3:
        cantidad +=1
    elif op ==4:
        cantidad +=1
    elif op ==5:
        cantidad +=1
    elif op ==6:
        cantidad +=1
    elif op ==7:
        cantidad +=1


servicio=''
for op in arreglo:
    if op ==1:
        servicio +='Revision de 1.000Km, '
    elif op ==2:
        servicio +='Cambio de aceite, '
    elif op ==3:
        servicio +='Revision de frenos, '
    elif op ==4:
        servicio +='Revision de correas, '
    elif op ==5:
        servicio +='Revision de luces, '
    elif op ==6:
        servicio +='Revision de direccion, '
    elif op ==7:
        servicio +='Lavado de tapis (sin costo), '

estado=''
val=False
while(val==False):
    print('seleccione el estado del trabajo: ')
    print('1.-Trabajando')
    print('2.-Terminado')
    print('3.-Entregado')
    estado_int=int(input(''))
    if estado_int==1:
        estado='Trabajando'
        val=True
    elif estado_int==2:
        estado='Terminado'
        val=True
    elif estado_int==3:
        estado='Entregado'
        val=True
    else:
        print('Opcion no valida, vuelva a intentarlo')
        



        
print('---------------------------------------------------------')
print('\t\t SERVICIO AUTOMOTRIZ')
print('---------------------------------------------------------')
print('Cliente: ',nombre_completo)
print('Servicios: ',servicio[:-2])
print('Cantidad: ',cantidad)
print('Tiempo de espera: ',tiempo)
print('Estado: ',estado)
print('---------------------------------------------------------')


