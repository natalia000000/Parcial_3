#Creacion de una lista vacia
reservas = []

#Creacion de un bucle en donde una vez ingresado los datos solicitados el usuario decide si desea ingresar mas datos
while True:
    #Creacion de variables segun los datos ingresados por el usuario
    Nombre_cliente = input("Ingresar nombre : ")
    Ciudad_Origen = input("Ingrese su ciudad de origen : ")
    Ciudad_Tour = input("Seleccione una de las opciones disponibles de destino : \n1.Torres del Paine \n2.Carretera Austral \n3.Chiloe\n")


    #Si el usuario no ingresa los datos solicitados el programa le envia un mensaje y le pide ingresar los datos nuevamente
    if Nombre_cliente == "" and Ciudad_Origen== "" and Ciudad_Tour == "":
        print("Debe completar todos los datos")

        Nombre_cliente = input("Ingresar nombre : ")
        Ciudad_Origen = input("Ingrese su ciudad de origen : ")
        Ciudad_Tour = input("Seleccione una de las opciones disponibles de destino : \n1.Torres del Paine \n2.Carretera Austral \n3.Chiloe\n")

    else:
        
        reserva = {
            "Nombre del cliente":Nombre_cliente,
            "Ciudad de origen":Ciudad_Origen,
            "Ciudad de Tour":Ciudad_Tour,
        }




    reservas.append(reserva)
    #Se le pregunta al usuario si desea continuar realizando reservas.
    #Si el usuario SI desea seguir con el registro entonces se le pedira ingresar los datos anteriormente solicitados.
    #Si el usuario NO desea seguir con el registro entonces el programa se cerrara y mostrara las reservas realizadas por el usuario.
    continuar = input("¿Desea registrar otra reserva? (si/no)\n")
    if continuar=="no":
        break


#Aqui se imprimen todas las reservas ingresadas
print(reservas)

#Aqui se crea el archivo de texto de las reservas
archivo= open("reservas.txt","w")


for reserva in reservas:
    archivo.write(f"Nombre del cliente : {reserva['Nombre del cliente']}\n")
    archivo.write(f"Ciudad de origen : {reserva['Ciudad de origen']}\n")
    archivo.write(f"Ciudad de Tour : {reserva['Ciudad de Tour']}\n")


print("El documento se creo exitosamente : reservas.txt")


archivo.close()